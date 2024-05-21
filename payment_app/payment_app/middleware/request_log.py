import frappe
from datetime import datetime

@frappe.whitelist(allow_guest=True)
def request_logss():
    path = frappe.request.path
    ip = frappe.local.request_ip
    
    if path.startswith("/api/method/payment_app"):
        request_body = frappe.local.request.data
        
    timestamp = datetime.now()
    if request_body:
        new_request = frappe.get_doc({
            "doctype": "Request Logs",
            "url": path,
            "ip": ip,
            "payload": request_body,
            "created_at": timestamp,
            "updated_at": timestamp
        })
        new_request.insert()
        frappe.db.commit()
