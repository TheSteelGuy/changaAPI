import os
import requests
from ..helpers.mpesa_apis_auth_gen import generate_auth

def send_request(contribution_obj):
    """send request"""
    try:
        url = os.environ['STK_PUSH_URL']
        auth_token = generate_auth()
        res = requests.post(
        url, headers={'Authorization': 'Bearer '+auth_token, 'content-type': 'application/json'},
        json=contribution_obj
        )
        return res.json()
    
    except Exception as e:
        #log this error
        raise e
