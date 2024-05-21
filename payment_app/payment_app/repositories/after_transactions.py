import frappe

def get_transaction_by_phone(invoice_reference_no):
    data = frappe.get_all(
        "Invoice",
        filters={"reference_no": invoice_reference_no},
        fields=["name", "reference_no", "product_name", "qty", "price", "total_price", "wallet_name","customer_id","store_id", "created_at", "updated_at"],
    )
    return data
