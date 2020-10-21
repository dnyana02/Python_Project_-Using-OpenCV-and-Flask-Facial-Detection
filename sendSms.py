from twilio.rest import Client

class sendsms:

    def sendSms(number):
    
        account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
        auth_token = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyy'
  
        client = Client(account_sid, auth_token)
        print("------------------------------------------------\n")
        print("                Sending SMS......\n")
        message = client.messages.create( 
                                            from_='xxxxxxxxxx',     # sender's twillio phone no.
                                            body ='Alert!!!  \nThere are '+str(number)+' number of people in Elavator!!!', 
                                            to   ='+91xxxxxxxxxx'     # receiver's twillio phone no.
                                        ) 
  
        print(message.sid) 
        print("------------------------------------------------\n")
    