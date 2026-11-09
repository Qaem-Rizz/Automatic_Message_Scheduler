import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

TWILIO_SENDER_NUMBER = os.getenv("TWILIO_SENDER_NUMBER")
DEFAULT_COUNTRY_CODE = "+91" # Default country code for India

