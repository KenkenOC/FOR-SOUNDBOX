import frappe
import jwt
from datetime import datetime
from ..utils.response import generate
from ..middleware.request_log import request_logss
from ..utils.generate_code import secret_key


@frappe.whitelist(allow_guest=True)
def login():
    try:
        request_data = frappe.form_dict
        request_get = frappe.db.get_value

        email_or_phone = request_data.get("email_or_phone")
        password = request_data.get("password")

        customer_id = request_get("Customers", {"email": email_or_phone}, "name")
        if not customer_id:
            customer_id = request_get("Customers", {"phone": email_or_phone}, "name")
            if not customer_id:
                request_logss()
                return {"error": "Customer not found"}

        get_virtual_account = request_get("Customers", customer_id, "virtual_account")

        customer_name = request_get("Customers", customer_id, "name1")
        request_logss()
        if not customer_name:
            return {"error": "Customer name not found"}

        phone = request_get("Customers", customer_id, "phone")
        request_logss()
        if not phone:
            return {"error": "Phone not found"}

        email = request_get("Customers", customer_id, "email")
        request_logss()
        if not email:
            return {"error": "Email not found"}

        password = request_get("Customers", customer_id, "password")
        request_logss()
        if not password:
            return {"error": "Password not found"}

        if password != request_data.get("password"):
            request_logss()
            return {"error": "Incorrect password"}

        payload = {
            "customer_id": customer_id,
            "phone": phone,
            "email": email,
            "virtual_account": get_virtual_account
        }

        access_token = jwt.encode(payload, secret_key(), algorithm="HS256")

        token_doc = frappe.get_doc({
            "doctype": "Tokens",
            "token": access_token,
            "email": email,
            "phone": phone,
            "created_at": datetime.now()
        })
        token_doc.insert()
        frappe.db.commit()

        request_logss()

        return generate(200,"Login Berhasil!",{
            "token": access_token
        })

    except Exception as e:
        return {"error": str(e)}
