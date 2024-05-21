import frappe
import jwt
from datetime import datetime
from ..utils.response import generate
from ..utils.generate_code import secret_key

@frappe.whitelist(allow_guest=True)
def auth():
    try:
        access_token = frappe.request.headers.get("Authorization")

        path = frappe.request.path
        if path != "/api/method/payment_app.payment.login.login" and path.startswith("/api/method/payment_app."):

            if not access_token:
                return {"error": "Access token is missing in the Authorization header", "statusCode": 401}

            decoded_token = jwt.decode(access_token, secret_key(), algorithms=["HS256"])

            phone = decoded_token.get("phone")
            email = decoded_token.get("email")

            customer_phone = frappe.db.get_value("Customers", {"phone": phone})
            customer_email = frappe.db.get_value("Customers", {"email": email})

            if not (customer_phone and customer_email):
                return generate(401, "Phone or email not found in the token")

            return generate(200, "The authentication was successful!", decoded_token)

    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired", "statusCode": 401}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token or secret key mismatch", "statusCode": 401}
    except Exception as e:
        return {"error": str(e), "statusCode": 500}
