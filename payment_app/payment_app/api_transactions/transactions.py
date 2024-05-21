import random
from datetime import datetime
import frappe
import string 
import json
from ..middleware.auth import auth
from ..utils.response import generate
from ..middleware.request_log import request_logss
from ..repositories.after_transactions import get_transaction_by_phone

@frappe.whitelist(allow_guest=True, methods=['POST'])
def create_transactions():
    try:
        response_auth = auth()
        if response_auth ["statusCode"] != 200:
            return response_auth
        
        request_data = frappe.form_dict
        request_get = frappe.db.get_value
        
        phone = request_data.get("phone")
        store_name = request_data.get("store_name")
        product_name = request_data.get("product_name")
        qty = request_data.get("qty")
        wallet_name = request_data.get("wallet_name")
        timestamp = datetime.now()

        # Validasi
        if not phone or not store_name or not product_name:
            request_logss()
            return generate(400, "Bad request")

        store_id = request_get("Store", {"store_name": store_name}, "name")
        if not store_id:
            request_logss()
            return generate(404, f"Toko dengan nama '{store_name}' tidak ditemukan")

        customer_id = request_get("Customers", {"phone": phone}, "name")
        if not customer_id:
            request_logss()
            return generate(404, f"Pelanggan dengan nomor telepon '{phone}' tidak ditemukan")
        
        product_id = request_get("Product", {"product_name": product_name, "store_name": store_name}, "name")
        if not product_id:
            request_logss()
            return generate(404, "Product Id tidak ditemukkan")
       
        try:
            qty = int(qty)
            if qty <= 0:
                request_logss()
                return generate(404,"Kuantitas harus lebih besar dari 0")
        except ValueError:
            return generate(404,"Kuantitas harus berupa bilangan bulat")

        price = request_get("Product", {"product_name": product_name, "store_name": store_name}, "price")
        if price is None:
            request_logss()
            return generate(404, "Harga tidak ditemukan untuk produk ini")

        price = int(price)

        total_price = qty * price

        invoice_reference_no = generate_reference_number(timestamp)

        new_invoice = frappe.get_doc({
            "doctype": "Invoice",
            "reference_no": invoice_reference_no,
            "product_name": product_name,
            "qty": qty,
            "price": price,
            "total_price": total_price,
            "wallet_name": wallet_name,
            "customer_id": customer_id,
            "store_id": store_id,
            "updated_at": timestamp,
            "created_at": timestamp
        })

        new_invoice.insert()
        frappe.db.commit()
        
        transactions(request_get, request_data)
        transactions_logs(request_data, request_get)

        request_logss()

        return generate(402 ,"Payment Required!",get_transaction_by_phone(invoice_reference_no))
    
    except Exception as e:
        return {"message": str(e)}
######################################## CREATE TRANSACTIONS END ############################################


######################################## GREFERENCE NUMBER ##################################################
def generate_reference_number(timestamp):
    tanggal = str(timestamp.day).zfill(2)
    bulan = str(timestamp.month).zfill(2)
    tahun = str(timestamp.year)[-2:]

    nomor_acak = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

    reference_no = f"IIVV{tanggal}{bulan}{tahun}{nomor_acak}5"

    return reference_no
######################################## GREFERENCE NUMBER END ##################################################


# ######################################## TRANSACTION ####################################################
def transactions(request_get, request_data):
    try:
        customer_name = request_get("Customers", {"phone": request_data.get("phone")}, "name1")
        get_customer_id = request_get("Customers", {"phone": request_data.get("phone")}, "name")

        get_invoice_reference_no = request_get("Invoice",{"customer_id": get_customer_id}, "reference_no")
        get_total_price = request_get("Invoice",{"customer_id": get_customer_id}, "total_price")


        timestamp = datetime.now()
        tanggal = str(timestamp.day).zfill(2)
        bulan = str(timestamp.month).zfill(2)
        tahun = str(timestamp.year)[-2:]

        nomor_acak = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

        transactions_reference_no = f"IIIV{tanggal}{bulan}{tahun}{nomor_acak}4"

        new_transactions = frappe.get_doc({
            "doctype": "Transactions",
            "invoice_reference_no": get_invoice_reference_no,
            "reference_no": transactions_reference_no,
            "store_name": request_data.get("store_name"),
            "customer_name": customer_name,
            "product_name": request_data.get("product_name"),
            "qty": request_data.get("qty"),
            "total_price": get_total_price, 
            "transaction_status": "pending",
            "created_at": timestamp,
            "updated_at": timestamp
        })

        new_transactions.insert()
        frappe.db.commit()

    except Exception as e:
        return {"message": str(e)}

# ######################################## TRANSACTION END ####################################################



# ######################################## TRANSACTION_LOGS ####################################################
def transactions_logs(request_data, request_get):
    try:
        request_get = frappe.db.get_value
        event_name = "Create_Transactions"
        payload = {
            "phone": request_data.get("phone"),
            "store_name": request_data.get("store_name"),
            "product_name": request_data.get("product_name"),
            "qty": request_data.get("qty"),
            "wallet_name": request_data.get("wallet_name")
        }

        # Manggil transaction_id
        get_transaction_id = request_get("Transactions",{"invoice_reference_no": request_data.get("invoice_reference_no")}, "name")
        payload_str = json.dumps(payload)

        timestamp = datetime.now()
        new_transaction_logs = frappe.get_doc({
            "doctype": "Transaction Logs",
            "payload": payload_str,
            "transactions_id" : get_transaction_id,
            "created_at": timestamp,
            "event_name" : event_name
        })

        new_transaction_logs.insert()
        frappe.db.commit()

        return {"message": "Logs berhasil disimpan"}
    except Exception as e:
        return {"message": str(e)}