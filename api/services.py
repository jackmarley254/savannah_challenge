import os
import africastalking
#from africastalking.AfricasTalkingGateway import AfricasTalkingGateway
from django.conf import settings

def send_order_alert_sms(customer_phone_number, message): 
    """
    Sends an SMS to a customer using Africa's Talking gateway.
    """
    username = settings.AT_USERNAME
    api_key = settings.AT_API_KEY
    
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    
    #gateway = AfricasTalkingGateway(username, api_key)
    
    recipients = [customer_phone_number]

    
    #sms = africastalking.SMS
    
    try:
        response = sms.send(recipients, message)
        print(f"SMS response: {response}")
        return response
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return None