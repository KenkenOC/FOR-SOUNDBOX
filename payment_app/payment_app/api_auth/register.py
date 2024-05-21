# register akun customer
import frappe
from datetime import datetime
from ..utils.response import generate
from ..utils.generate_code import generate_virtual_account
from ..middleware.request_log import request_logss
from ..middleware.auth import auth
from ..repositories.store import get_store_by_customer_id
from ..repositories.customer import get_customer_by_phone

@frappe.whitelist(allow_guest=True)
def register_akun_customer():
    request_data = frappe.form_dict
    request_get = frappe.db.get_value

    customer_name = request_data.get("customer_name")
    phone = request_data.get("phone")
    email = request_data.get("email")
    password = request_data.get("password")

    # Validasi
    if not (customer_name and phone and email and password):
        request_logss()
        return "Maaf, data yang dimasukkan tidak lengkap. Mohon pastikan nama, nomor faks, dan alamat email telah sesuai."
    
    # Cek apakah customer sudah terdaftar
    cek_customer_name = request_get("Customers", {"name1": customer_name})
    if cek_customer_name:
        request_logss()
        return generate (400, "Nama sudah terdaftar di sistem.")
    
    cek_customer_phone = request_get("Customers", {"phone": phone})
    if cek_customer_phone:
        return generate (400,"Nomor telepon sudah terdaftar di sistem.")
    
    cek_customer_email = request_get("Customers", {"email": email})
    if cek_customer_email:
        return generate(400, "Alamat email sudah terdaftar di sistem.")
    
    if not (any(char.isdigit() for char in password) and any(char.isupper() for char in password)):
        return "Password harus mengandung setidaknya satu angka dan satu huruf besar."

    virtual_account = generate_virtual_account()

    new_customers = frappe.get_doc ({
        "doctype": "Customers",
        "name1": customer_name,
        "phone": phone,
        "email": email,
        "password":  password,
        "virtual_account": virtual_account,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    })

    new_customers.insert()
    frappe.db.commit()
    
    request_logss()
    return generate(200,"Registrasi berhasil! Selamat datang, {}.".format(customer_name), get_customer_by_phone(phone))



# register store, validasi token 
# Register akun store
@frappe.whitelist(allow_guest=True)
def register_akun_store():
    response_auth = auth()
    if response_auth ["statusCode"] != 200:
        return response_auth

    request_data = frappe.form_dict
    request_get = frappe.db.get_value

    store_name = request_data.get("store_name")
    email = request_data.get("email")
    is_active = 1

    if not (store_name and email):
        request_logss()
        return  generate (400,"Maaf, data yang dimasukkan tidak lengkap. Mohon pastikan semua kolom telah diisi.")

    try: 
        customer_data = response_auth["data"]
        customer_id = customer_data["customer_id"]
        customer_phone = customer_data["phone"]

        cek_store_name = request_get("Store", {"store_name": store_name})
        if cek_store_name:
            return generate(400, "Nama toko sudah terdaftar di sistem.")

        cek_owner_email = request_get("Store", {"email": email})
        if cek_owner_email:
            return generate(400, "Alamat email sudah terdaftar di sistem.")
        
        cek_customer = request_get("Store", {"customer_id": customer_id})
        if cek_customer:
            return generate(400, "Anda sudah memiliki akun toko.")

        new_store = frappe.get_doc({
            "doctype": "Store",
            "store_name": store_name,
            "phone": customer_phone,
            "email": email,
            "customer_id": customer_id,
            "is_active": is_active,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        })

        new_store.insert()
        frappe.db.commit()

        request_logss()
        return generate(200,"Registrasi toko berhasil! Selamat datang, {}.".format(store_name), get_store_by_customer_id(customer_id))
    
    except Exception as e:
        return generate(500, "Failed register store!", str(e))

