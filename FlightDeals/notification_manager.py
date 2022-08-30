from twilio.rest import Client

TWILIO_SID = "ACb087a90e312b0465fc65f4828bf73419"
TWILIO_AUTH_TOKEN = "d653725c68869069cc31ced16f7586cb"
TWILIO_VIRTUAL_NUMBER = "+13252464340"
TWILIO_VERIFIED_NUMBER = "+38765845127"


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