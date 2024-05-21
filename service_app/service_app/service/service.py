import requests
import hashlib
import frappe
from datetime import datetime
import json

# Fungsi untuk mendapatkan token
@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_token():
    try:
        app_secret = "2024bsjEZ665AIF"
        object_map = {
            "appId": "EZ665",
            "timestamp": "2000000000000",
            "requestId": "1",
            "userCode": "EZ665"
        }
        content = ""
        keys = ["appId", "timestamp", "requestId", "userCode"]
        keys.sort()

        for key in keys:
            value = str(object_map.get(key, ''))
            if key.strip() and value.strip():
                content += key + value
            else:
                raise ValueError("key: " + key + " memiliki nilai yang tidak valid")

        print("encrypted string:", content)
        return hashlib.md5((content + app_secret).encode()).hexdigest().upper()
    except Exception as e:
        frappe.log_error(f"Failed to generate token: {str(e)}", "Token Generation Error")



# Fungsi untuk mengambil data dari API
@frappe.whitelist(allow_guest=True, methods=['GET'])
def fetch_api(**kwargs):
    try:
        # Memanggil fungsi get_token
        token = get_token()

        # URL API
        url = 'https://cloud.yxyiot.com/v1/openApi/dev/controlDevice.json'

        total_price = kwargs.get('total_price')

        # Parameter yang diperlukan untuk permintaan API
        params = {
            "appId": "EZ665",
            "timestamp": "2000000000000",
            "requestId": "1",
            "userCode": "EZ665",
            "devName": "EZ6654010101",
            "bizType": "1",
            "money": total_price,
            "content": total_price,
            "broadCastType": "1",
            "token": token
        }

        # Melakukan permintaan GET ke API
        response = requests.get(url, params=params)

        # Mengembalikan respons JSON dari API jika berhasil
        if response.status_code == 200: 
            # Menyimpan data ke doctype "Data Payment"
            return {"status_code": response.status_code, "data": response.json()}
        else:
            return {"status_code": response.status_code, "data": None}
    except Exception as e:
        frappe.log_error(f"Failed to fetch API: {str(e)}", "Fetch API Error")


@frappe.whitelist(allow_guest=True, methods=['GET'])
def receive_param(**kwargs):
    try:
        fetch_api(**kwargs)
        transaction_id = kwargs.get('transaction_id')

        invoice_reference_no = kwargs.get('invoice_reference_no')
        transaction_reference_no = kwargs.get('partner_reference_no')
        store_name = kwargs.get('store_name')
        customer_name = kwargs.get('customer_name')
        product_name = kwargs.get('product_name')
        qty = kwargs.get('qty')
        total_price = kwargs.get('total_price')
        transaction_status = kwargs.get('transaction_status')

        timestamp = datetime.now()

        new_transaction = frappe.get_doc({
            "doctype": "Transactions",
            "partner_reference_no": transaction_reference_no,
            "invoice_reference_no": invoice_reference_no,
            "store_name": store_name,
            "customer_name": customer_name,
            "product_name": product_name,
            "qty": qty,
            "total_price": total_price,
            "transaction_status": transaction_status,
            "transaction_id": transaction_id,
            "created_at": timestamp,
            "updated_at": timestamp
        })

        new_transaction.insert()
        frappe.db.commit()

        new_request_logs(**kwargs)
        new_transaction_logs(**kwargs)

        # Mengembalikan respons
        return {"status": "success", "message": "Data successfully added to Transactions"}

    except requests.exceptions.RequestException as e:
        # Menangani kesalahan jika permintaan gagal atau ada masalah lainnya
        print("Gagal melakukan permintaan:", e)
        return {"status": "failed", "message": str(e)}


def new_transaction_logs(**kwargs):
    try:
        event_name = "Payment Transactions"

        transaction_id = kwargs.get('transaction_id')
        transaction_reference_no = kwargs.get('partner_reference_no')
        invoice_reference_no = kwargs.get('invoice_reference_no')
        store_name = kwargs.get('store_name')
        customer_name = kwargs.get('customer_name')
        product_name = kwargs.get('product_name')
        qty = kwargs.get('qty')
        total_price = kwargs.get('total_price')
        transaction_status = kwargs.get('transaction_status')

        payload = {
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
        payload_str = json.dumps(payload)
        timestamp = datetime.now()
        

        new_transaction_logs = frappe.get_doc({
            "doctype": "Transaction Logs",
            "event_name": event_name,
            "payload": payload_str,
            "transactions_id": transaction_id,
            "created_at": timestamp,
            "updated_at": timestamp
        })

        new_transaction_logs.insert()
        frappe.db.commit()

        return {"status": "success", "message": "Transaction log successfully created"}

    except Exception as e:
        # Tangani kesalahan jika terjadi
        return {"status": "failed", "message": str(e)}
 

def new_request_logs(**kwargs):
    try:
        transaction_id = kwargs.get('..')
        transaction_reference_no = kwargs.get('partner_reference_no')
        invoice_reference_no = kwargs.get('invoice_reference_no')
        store_name = kwargs.get('store_name')
        customer_name = kwargs.get('customer_name')
        product_name = kwargs.get('product_name')
        qty = kwargs.get('qty')
        total_price = kwargs.get('total_price')
        transaction_status = kwargs.get('transaction_status')

        payload = {
            "partner_reference_no": transaction_reference_no,
            "invoice_reference_no": invoice_reference_no,
            "store_name": store_name,
            "customer_name": customer_name,
            "product_name": product_name,
            "qty": qty,
            "total_price": total_price,
            "transaction_status": transaction_status,
            "transaction_id": transaction_id,
        }

        ip = frappe.local.request_ip

        host = frappe.request.host
        path = frappe.request.path
        scheme = frappe.request.scheme

        url = f"{scheme}://{host}{path}"

        new_request_logs = frappe.get_doc({
            "doctype": "Request Logs",
            "url": url,
            "ip": ip,
            "payload": json.dumps(payload),
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        })

        new_request_logs.insert()
        frappe.db.commit()
        
        return {"status": "success", "message": "Request logs berhasil disimpan"}
    except Exception as e:
        return {"status": "failed", "message": str(e)}
