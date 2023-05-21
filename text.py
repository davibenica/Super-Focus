from twilio.rest import Client

class textBot:
    def    __init__(self,phoneNum) -> None:
        self.account_sid = 'ENTER ACCOUNT SID HERE'

        self.auth_token = 'ENTER AUTH TOKEN HERE'

        self.twilioNumber = '+18884016793'

        self.targetNumber = str(phoneNum)

    def sendMeassage(self, message):
        client = Client(self.account_sid,self.auth_token)

        message_sent = client.messages.create(
            body = str(message),
            from_ = self.twilioNumber,
            to = self.targetNumber
        )
    