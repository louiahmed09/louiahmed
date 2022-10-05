import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SUDO = int(os.environ.get("SUDO", ""))
HEROKU = os.environ.get("HEROKU", "")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
