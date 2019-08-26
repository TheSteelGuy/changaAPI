import os
import requests

from celery.utils.log import get_task_logger
from celery import task

from ..contributions.models import Contribution

from ..helpers.mpesa_apis_auth_gen import generate_auth

logger = get_task_logger(__name__)

@task()
def callback_not_received():
    """incase the the call back url did not receive any response"""
    try:
        transactions = Contribution.objects.filter(result_code=1)
        contribution_objs = []
        if transactions:
            for transaction in transactions:
                auth_token = generate_auth()
                print('')
                url = os.environ['QUERY_REQUEST_URL']
                data = {
                    "BusinessShortCode": transaction.business_shortcode,
                    "Password": transaction.password,
                    "Timestamp": transaction.timestamp,
                    "CheckoutRequestID": transaction.checkout_request_id
                }
                response = requests.post(
                    url, json=data, headers={'Authorization': 'Bearer ' + auth_token, 'content-type': 'application/json'}
                )
                res_json = response.json()
                if res_json.get('ResultCode') == '0':
                    contribution_objs.append(transaction)
                    transaction.result_code = 0
                    transaction.amount = transaction.last_amount
                # elif res_json.get('ResultCode') and res_json.get('ResultCode') != '0':
                
            Contribution.objects.bulk_update(contribution_objs, ['result_code'])
            logger.info("sucess")

    except Exception as e:
        logger.error(e)
        print(e)
