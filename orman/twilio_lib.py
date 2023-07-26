# /usr/bin/env python
import os
from twilio.rest import Client

#"MG13543774237da8a99548db0c1dcb29bf"

class sender():
    account_sid = 'AC0ec54b3c7390f83eb3ba9ac02653a891'    
    auth_token = 'e3fc5884ea24369381a3b8c937194f48'
    
    def send(self, number, message):
        client = Client(self.account_sid, self.auth_token)
        try:
            client.api.account.messages.create(     
                messaging_service_sid='MG13543774237da8a99548db0c1dcb29bf', 
                to="+52{}".format(number),
                body="{}".format(message))
            return True
        except:
            return False
        
