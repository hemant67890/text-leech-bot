import os

API_ID    = os.environ.get("API_ID", "26512964")
API_HASH  = os.environ.get("API_HASH", "e5d187c6c7a0919ccb8866f76f655701")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7721687137:AAG0eLiP6k0IuFD7ROcSHyITh2pY3py_-TI") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
