import os
import base64
import requests

def auth_credentials_to_b64():
    try:
        consumer_key = os.environ['CONSUMER_KEY']
        consumer_secret = os.environ['CONSUMER_SECRET']
        sec_key = consumer_key+':'+consumer_secret
        b64_string = base64.b64encode(sec_key.encode()).decode()
        return 'Basic '+b64_string
    except Exception as e:
        #log error
        raise e
    

def generate_auth():
    """generate token"""
    try:
        url = os.environ['MPESA_AUTH_URL']
        credentials = auth_credentials_to_b64()
        PARAMS = {'grant_type':'client_credentials'}
        res = requests.get(
        url, headers={'Authorization': credentials},
        params=PARAMS
        )
        print(res.json()['access_token'])
        return res.json()['access_token']
    
    except Exception as e:
        #log this error
        raise e
print(generate_auth())