import os
from dotenv import load_dotenv

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")
ENTER_KEY = os.getenv("ENTER_KEY")