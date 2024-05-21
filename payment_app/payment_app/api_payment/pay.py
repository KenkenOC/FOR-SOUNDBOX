import frappe
from datetime import datetime
import json
import requests
from ..middleware.auth import auth
from ..utils.response import generate
from ..middleware.request_log import request_logss
from ..repositories.pay import after_payment

@frappe.whitelist(allow_guest=True, methods=['POST'])
def pay():
    try:
        response_auth = auth()
        if response_auth ["statusCode"] != 200:
            return response_auth
        
        request_data = frappe.form_dict
        request_get = frappe.db.get_value
        
        transaction_reference_no = request_data.get("transaction_reference_no")
        wallet_name = request_data.get("wallet_name")
        virtual_account = request_data.get("virtual_account")
        total_price = request_data.get("total_price")
        transaction_status = request_data.get("transaction_status")

        # VALIDASI
        if not (transaction_reference_no and wallet_name and virtual_account and total_price and transaction_status):
            return generate(400, "Invalid transaction")
        
        
        get_transaction_reference_no_id = request_get("Transactions", {"reference_no": transaction_reference_no}, "name")
        if not get_transaction_reference_no_id:
            return generate(404, "Transaction reference no exists")
        
        product_check = check_product_stock(transaction_reference_no)
        if not product_check["status"]:
            return generate(400, product_check["message"])
        
        get_invoice_reference_no = request_get("Transactions", get_transaction_reference_no_id, "invoice_reference_no")
        get_wallet_name = request_get("Invoice", {"reference_no": get_invoice_reference_no}, "wallet_name")
        if wallet_name != get_wallet_name:
            return generate(404, "Wallet Name not found")

        get_invoice_id = request_get("Invoice", {"reference_no": get_invoice_reference_no}, "name")
        get_customer_id = request_get("Invoice", get_invoice_id, "customer_id")
        get_virtual_account = request_get("Customers", {"name": get_customer_id}, "virtual_account")
        if virtual_account != get_virtual_account:
            return generate(404,"Virtual Account Not Found")
        
        get_total_price = request_get("Transactions", get_transaction_reference_no_id, "total_price")
        if total_price != get_total_price:
            request_logss()
            return generate(404, "total price yang dimasukkan salah")

        edit_status(request_data, request_get)
        save_transactions_callback(request_data, request_get)
        save_webhook_logs(request_data, request_get)
        transaction_stock_update(request_data, request_get)
        hit_fetch_api_service()

        request_logss()

        return generate(200,"Payment successfully completed!", after_payment(transaction_reference_no))
        
    except Exception as e:
        return {"message": str(e), "p":"p" }
    
def edit_status(request_data, request_get):
    try:
        timestamp = datetime.now()

        new_data_update = {
            "transaction_status": request_data.get("transaction_status"),
            "updated_at": timestamp
        }

        transaction_reference_no_id = request_get("Transactions", {"reference_no": request_data.get("transaction_reference_no")}, "name")
        frappe.db.set_value("Transactions", transaction_reference_no_id, new_data_update)
        frappe.db.commit()

    except Exception as e:
        return {"message": str(e)}


def check_product_stock(transaction_reference_no):
    try:
        request_get = frappe.db.get_value
        get_transaction_id = request_get("Transactions", {"reference_no": transaction_reference_no}, "name")
        get_product_name = request_get("Transactions", get_transaction_id, "product_name")
        get_store_name = request_get("Transactions", get_transaction_id, "store_name")
        
        get_product_id = request_get("Product", {"product_name": get_product_name, "store_name": get_store_name}, "name")
        get_stock = int(request_get("Product", get_product_id, "stock"))
        
        if get_stock == 0:
            return {"status": False, "message": "Product stock is 0. Cannot proceed with the transaction."}
        
        return {"status": True}
    
    except Exception as e:
        return {"status": False, "message": str(e)}



def transaction_stock_update(request_data, request_get):
    try:
        get_transaction_id = request_get("Transactions", {"reference_no": request_data.get("transaction_reference_no")}, "name")
        get_product_name = request_get("Transactions", get_transaction_id, "product_name")
        get_store_name = request_get("Transactions", get_transaction_id, "store_name")
        get_transaction_status = request_get("Transactions", get_transaction_id, "transaction_status")  
        
        if get_transaction_status == "Success!":  
            get_product_id = request_get("Product", {"product_name": get_product_name, "store_name": get_store_name}, "name")
            get_previous_stock = int(request_get("Product", get_product_id, "stock"))
            get_qty = request_get("Transactions", get_transaction_id, "qty")

            qty_int = int(get_qty)
            new_stock = get_previous_stock - qty_int
            new_last_stock_out = datetime.now()

            frappe.db.set_value("Product", get_product_id, "stock", new_stock)
            frappe.db.set_value("Product", get_product_id, "last_stock_out", new_last_stock_out)
            frappe.db.commit()

            return {"message": "Stock updated successfully."}
        else:
            return {"message": "Transaction status is not 'Success!'."}

    except Exception as e:
        return {"message": str(e)}


def save_transactions_callback(request_data, request_get):
    try:
        url = None
        timestamp = datetime.now()

        payload = {
            "wallet_name": request_data.get("wallet_name"),
            "virtual_account": request_data.get("virtual_account"),
            "total_price": request_data.get("total_price"),
        }
        
        payload_str = json.dumps(payload)

        transaction_reference_no = request_data.get("transaction_reference_no")
        transaction_status = request_data.get("transaction_status")
        
        transaction_reference_no_id = request_get("Transactions", {"reference_no": transaction_reference_no}, "name")

        new_transactions_callback = frappe.get_doc({
            "doctype": "Transaction Callback",
            "url": url,
            "response": transaction_status,
            "payload": payload_str,
            "transaction_reference_no": transaction_reference_no_id,
            "created_at": timestamp,
            "updated_at": timestamp
        })
        
        new_transactions_callback.insert()
        frappe.db.commit()

    except Exception as e:
        return {"message": str(e)}
    

def save_webhook_logs(request_data, request_get):
    try:
        path = "http://collab4.test:8000/api/method/payment_app.payment.pay.pay"
        ip = frappe.local.request_ip

        payload = {
            "transaction_reference_no": request_data.get("transaction_reference_no"),
            "wallet_name": request_data.get("wallet_name"),
            "virtual_account": request_data.get("virtual_account"),
            "total_price": request_data.get("total_price"),
            "response": request_data.get("transaction_status")
        }
        payload_str = json.dumps(payload)
        timestamp = datetime.now()

        new_save_webhook_logs = frappe.get_doc({
            "doctype": "Webhook Logs",
            "path": path,
            "ip": ip,
            "payload": payload_str,
            "created_at": timestamp,
            "updated_at": timestamp
        })

        new_save_webhook_logs.insert()
        frappe.db.commit()

    except Exception as e:
        return {"message": str(e)}


@frappe.whitelist(allow_guest=True)
def hit_fetch_api_service():
    url = 'http://service01.test:8000/api/method/service_app.service.service.receive_param'

    request_get = frappe.db.get_value
    request_data = frappe.form_dict

    transaction_reference_no = request_data.get('transaction_reference_no')

    transaction_id = request_get("Transactions", {"reference_no": transaction_reference_no}, "name")

    invoice_reference_no = request_get("Transactions", transaction_id, "invoice_reference_no")
    store_name = request_get("Transactions", transaction_id, "store_name")
    customer_name = request_get("Transactions", transaction_id, "customer_name")
    product_name = request_get("Transactions", transaction_id, "product_name")
    qty = request_get("Transactions", transaction_id, "qty")
    total_price = request_get("Transactions", transaction_id, "total_price")
    transaction_status = request_get("Transactions", transaction_id, "transaction_status")

    try:
        parameters = {
            "invoice_reference_no": invoice_reference_no,
            "partner_reference_no": transaction_reference_no,
            "store_name": store_name,
            "customer_name": customer_name,
            "product_name": product_name,
            "qty": qty,
            "total_price": total_price,
            "transaction_status": transaction_status,
            "transaction_id": transaction_id,
        }
        
        response = requests.get(url, params=parameters)
        response.raise_for_status()  

        data = response.json()
        
        return data
        
    except requests.exceptions.RequestException as e:
        print("Gagal melakukan permintaan:", e)
        return None
