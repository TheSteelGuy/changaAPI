import requests
from helpers.mpesa_apis_auth_gen import generate_auth
access_token = generate_auth()
api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode": " ",
    "ResponseType": " ",
    "ConfirmationURL": "http://ip_address:port/confirmation",
    "ValidationURL": "http://ip_address:port/validation_url"}

response = requests.post(api_url, json = request, headers=headers)