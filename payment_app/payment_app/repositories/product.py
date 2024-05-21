import frappe


def get_product_after_create(product_name, store_name):
    data = frappe.get_all(
        "Product",
        filters={
            "product_name": product_name,
            "store_name": store_name
        },
        fields=["name", "store_name", "product_name", "stock", "price", "last_stock_add", "last_stock_out"]
    )
    return data