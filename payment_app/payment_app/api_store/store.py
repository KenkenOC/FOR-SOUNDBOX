import frappe
from datetime import datetime
from ..middleware.request_log import request_logss
from ..utils.response import generate
from ..middleware.auth import auth

@frappe.whitelist(allow_guest=True, methods=['POST'])
def add_store():
    try:
        response_auth = auth()
        if response_auth ["statusCode"] != 200:
            return response_auth
        
        request_data = frappe.form_dict
        store_name = request_data.get("store_name")
        is_active = 1
        phone = int(request_data.get('phone'))
        email = request_data.get('email')
        timestamp = datetime.now()

        if not (store_name, phone, email):
            request_logss()
            return generate(400, "Maaf, data yang dimasukkan tidak lengkap. Mohon pastikan nama, nomor faks, dan alamat email telah sesuai.")
        
        if frappe.db.exists("Store", {"store_name": store_name}):
            request_logss()
            return generate(409, "Maaf, toko dengan nama tersebut sudah ada.")

        new_store = frappe.get_doc({
            "doctype": "Store",
            "store_name": store_name,
            "is_active": is_active,
            "phone": phone, 
            "email": email,
            "created_at" : timestamp
        })

        new_store.insert()
        frappe.db.commit()

        request_logss()

        return generate(201, "Sukses!")

    except Exception as e:
        return generate(500, f"Terjadi kesalahan saat menambahkan toko: {str(e)}")
    

@frappe.whitelist(allow_guest=True, methods=['PUT'])
def update_store():
    request_data = frappe.form_dict

    store_id = request_data.get("id")
    timestamp = datetime.now()
    
    data_to_be_updated = {
        "updated_at" : timestamp,
    }

    try:
        if not frappe.db.exists("Store", store_id):
            return generate(404, "Toko tidak ditemukan.")

        if 'email' in request_data:
            email = request_data['email']
            if email.strip():
                data_to_be_updated['email'] = email
        
        if 'store_name' in request_data:
            store_name = request_data['store_name']
            if store_name.strip():  
                data_to_be_updated['store_name'] = store_name
          
        if 'is_active' in request_data:
            is_active = request_data.get('is_active')

            if is_active not in ('0','1'):
                return generate(400, "Data harus bernilai 1 untuk aktif, 0 untuk tidak aktif")

            data_to_be_updated['is_active'] = is_active
        
     
        if 'phone' in request_data:
            phone = request_data['phone']
            if phone.strip():  
                data_to_be_updated['phone'] = phone

        if 'store_name' not in data_to_be_updated:
            existing_name = frappe.db.get_value("Store", store_id, "store_name")
            if existing_name:
                data_to_be_updated['store_name'] = existing_name

        if 'phone' not in data_to_be_updated:
            existing_fax = frappe.db.get_value("Store", store_id, "phone")
            if existing_fax:
                data_to_be_updated['phone'] = existing_fax

    
        frappe.db.set_value("Store", store_id, data_to_be_updated)
        frappe.db.commit()

        request_logss()

        return generate(200, "Toko berhasil diperbarui.")

    except Exception as e:
        return generate(500, f"Terjadi kesalahan saat memperbarui toko: {str(e)}")


@frappe.whitelist(allow_guest=True, methods=['DELETE'])
def delete_store(id):
    try:
        if not frappe.db.exists("Store", {"name": id}):
            return generate(404, "Toko dengan ID yang diberikan tidak ditemukan.")

        frappe.db.delete("Store", {"name": id})
        request_logss()
        
        return generate(200, "OK!")
    except Exception as e:
       return generate(500, f"Gagal menghapus data: {str(e)}")


@frappe.whitelist(allow_guest=True, methods=['GET'])
def getData_Store():
    try:
        data = frappe.get_all("Store")
        return {
            "statusCode": 200,
            "data": data,
            "message": "OK!"
        }
    except Exception as e:
        return generate(500, f"Gagal mengambil data: {str(e)}")