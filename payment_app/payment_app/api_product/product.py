import frappe
from datetime import datetime
from ..utils.response import generate
from ..middleware.request_log import request_logss
from ..middleware.auth import auth
from ..repositories.product import get_product_after_create

@frappe.whitelist(allow_guest=True)
def add_product():
    response_auth = auth()
    if response_auth ["statusCode"]!= 200:
        return response_auth
    
    request_data = frappe.form_dict
    request_get = frappe.db.get_value

    product_name = request_data.get("product_name")
    stock = request_data.get("stock")
    price = request_data.get("price")
    timestamp = datetime.now()

    if not all([product_name, stock, price]):
        return generate(422, "Product, stock, price must be filled in!")

    try:
        data_customer = response_auth["data"]
        customer_id = data_customer["customer_id"]

        store_id = request_get("Store", {"customer_id": customer_id})
        if not store_id:
            return generate(404, "You do not have store!")
        
        store_name = request_get("Store", store_id, "store_name")
        
        valid_product = request_get("Product", {"store_name": store_name, "product_name": product_name})
        if valid_product:
            return generate(400, "The product already exists in your store")


        new_product = frappe.get_doc({
            "doctype": "Product",
            "product_name": product_name,
            "store_name": store_name,
            "stock": stock,
            "price": price,
            "last_stock_add": timestamp
        })

        new_product.insert()
        frappe.db.commit()

        request_logss()

        return generate(200, "The products from your store have been added", get_product_after_create(product_name, store_name))
    except Exception as e:
        return generate(500, f"An error occurred while adding the product: {str(e)}")

@frappe.whitelist(allow_guest=True, methods=['DELETE'])
def delete_product():
    response_auth = auth()
    if response_auth["statusCode"] != 200:
        return response_auth
    
    request_get = frappe.db.get_value
    request_data = frappe.form_dict

    product_name = request_data.get("product_name")

    try:
        data_customer = response_auth["data"]
        customer_id = data_customer["customer_id"]

        store_id = request_get("Store", {"customer_id": customer_id}, "name")
        if not store_id:
            return generate(404, "You do not have a store!")
        
        product_id = request_get("Product", {"product_name": product_name}, "name")
        if not product_id:
            return generate(404, "Product not found")

        frappe.db.delete("Product", {"product_name": product_name})
        frappe.db.commit()

        request_logss()

        return generate(200, "Product successfully deleted.")
    except Exception as e:
        return generate(500, f"An error occurred while deleting the product: {str(e)}")
    

@frappe.whitelist(allow_guest=True, methods=['PUT'])
def update_product():
    response_auth = auth()
    if response_auth["statusCode"] != 200:
        return response_auth
    
    request_data = frappe.form_dict
    request_get = frappe.db.get_value

    product_name = request_data.get("product_name")
    stock = request_data.get("stock")
    price = request_data.get("price")
    
    timestamp = datetime.now()
    
    data_to_be_updated = {
        "last_stock_add": timestamp
    }

    if not product_name:
        return generate(422, "Product name must be provided!")

    try:
        data_customer = response_auth["data"]
        customer_id = data_customer["customer_id"]

        store_id = request_get("Store", {"customer_id": customer_id}, "name")
        if not store_id:
            return generate(404, "You do not have a store!")
        
        store_name = request_get("Store", store_id, "store_name")
        
        product_id = request_get("Product", {"store_name": store_name, "product_name": product_name}, "name")
        if not product_id:
            return generate(404, "Product not found")

        if 'stock' in request_data:
            stock = request_data['stock']
            if stock is not None:
                if not isinstance(stock, (int, float)):
                    return generate(422, "Stock must be a number!")
                data_to_be_updated['stock'] = stock

        if 'price' in request_data:
            price = request_data['price']
            if price is not None:
                if not isinstance(price, (int, float)):
                    return generate(422, "Price must be a number!")
                data_to_be_updated['price'] = price

        if len(data_to_be_updated) == 1:
            return generate(422, "At least one of stock or price must be provided for update!")

        frappe.db.set_value("Product", product_id, data_to_be_updated)
        frappe.db.commit()

        request_logss()

        return generate(200, "Product successfully updated.")
    except Exception as e:
        return generate(500, f"An error occurred while updating the product: {str(e)}")
