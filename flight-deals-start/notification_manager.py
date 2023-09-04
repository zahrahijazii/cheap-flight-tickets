from twilio.rest import Client


TWILIO_SID = "AC53ec109fd4521b121d3b8a25052aca93"
TWILIO_AUTH_TOKEN = "06696ced934f4b1c3a91ee40f9c4c21c"
TWILIO_VIRTUAL_NUMBER = '+14706348198'
TWILIO_VERIFIED_NUMBER = '+15558675310'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
    
