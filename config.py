import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ENTER_KEY = os.getenv("ENTER_KEY")

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
SENDER_PHONE = os.getenv("SENDER_PHONE")
RIDA_PHONE = os.getenv("RIDA_PHONE")
