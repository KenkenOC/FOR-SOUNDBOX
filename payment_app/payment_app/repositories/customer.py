import frappe

def get_customer_by_phone(phone):
    data = frappe.get_all(
        "Customers",
        filters = {"phone": phone},
        fields=["name", "name1", "phone", "email", "virtual_account", "created_at", "updated_at"]
        )
    return data