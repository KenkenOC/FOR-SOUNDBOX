import frappe

@frappe.whitelist(allow_guest=True)
def generate(status, message, data=""):
    return {
        "statusCode": status,
        "responseMessage": message,
        "data": data
    }

# response_auth = auth()
# if "statusCode" in response_auth and response_auth["statusCode"] != 200:
#     return response_auth
