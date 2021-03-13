from MadBoi.events import register as MadBoii
from MadBoi import telethn as bot
from MadBoi import API_ID, API_HASH
from MadBoi.events import *
from telethon import TelegramClient
from telethon.sessions import StringSession

import os
STRING_SESSION = os.environ.get("STRING_SESSION")
if STRING_SESSION:
    user = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
else:
     print ("please add StringSession var")

try:
     user.start()
except Exception as e:
     print(e)
