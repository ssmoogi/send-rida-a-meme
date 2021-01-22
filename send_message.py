from config import *

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_message(sender, message, meme):
    message = client.messages.create(
        body="from " + sender + ": " + message,
        media_url=[meme],
        from_=SENDER_PHONE,
        to=RIDA_PHONE
        )

    print(message.sid)