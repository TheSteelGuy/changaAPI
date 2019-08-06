import os
import requests
from datetime import date
from decimal import Decimal
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


def add_context_to_contribution(instance, chamaa_obj, user, Contribution):
    try:
        if instance.required_amount > 0:
            contribution = Contribution.objects.filter(
                msisdn=instance.msisdn,
                business_shortcode=instance.business_shortcode,
                created_at__month=date.today().month
            ).first()

            if contribution:
                instace_amount = float(instance.amount)
                contribution.amount += Decimal(instace_amount)
                contribution_amount = float(contribution.amount)
                
                print('>>>>>>><<<<<<<<<<>>>>>>>><<>><>><',contribution_amount)
                if float(contribution.required_amount) > contribution_amount:
                    
                    contribution.outstanding_balance = Decimal(float(contribution.required_amount) - float(contribution_amount))
                    
                    contribution.indicator_level = Decimal(round(
                    (contribution_amount/float(contribution.required_amount)), 2))
                  
                elif float(contribution.required_amount) < contribution_amount:
                    contribution.outstanding_balance = Decimal(float(contribution.required_amount) - contribution_amount)
                    contribution.indicator_level = 1.00
               
                contribution.account_balance = str(float(contribution.account_balance) + float(instance.amount))
                contribution.save()
        
            # the first contribution of the month
            else:
                instance.outstanding_balance = Decimal(float(instance.required_amount) - float(instance.amount))
                instance.indicator_level = Decimal(round(
                    (float(instance.amount)/float(instance.required_amount)), 2))
                instance.save()
                user.contributions.add(instance)

                chamaa_obj.contributions.add(instance)
                user.chamaas.add(chamaa_obj)
        else:
            instance.indicator_level = 1.00
            instance.save()
    except:
        raise

