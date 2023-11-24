from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "161b61f5a06dd299a3d88a3384b9f104")
      API_ID = int(getenv("API_ID", "16681004"))
      AS_COPY = getenv("AS_COPY", "{file_Caption}") == "{file_caption}"
      BOT_TOKEN = getenv("BOT_TOKEN", "6416226948:AAFnRXV_d-OeJNsbcHVBYdFMzmsEnmbzOq8")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001822165826:-1002031705842").replace("\n", " ").split(' '))

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
