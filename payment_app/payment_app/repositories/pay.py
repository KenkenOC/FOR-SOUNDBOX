import frappe


def after_payment(transaction_reference_no):
    data = frappe.get_all(
    "Transactions",
    filters={"reference_no": transaction_reference_no},
    fields=["store_name", "customer_name", "product_name", "qty", "total_price", "transaction_status", "created_at", "updated_at", "updated_at"]
    )
    return data