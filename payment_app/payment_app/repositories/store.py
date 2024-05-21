import frappe

def get_store_by_customer_id(customer_id):
    data = frappe.get_all(
        "Store",
        filters = {"customer_id": customer_id},
        fields=["name", "store_name", "email","phone","customer_id","is_active", "created_at", "updated_at"]
        )
    return data