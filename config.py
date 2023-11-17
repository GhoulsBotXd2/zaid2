## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")

API_ID = int(getenv("API_ID", "26019444"))
API_HASH = getenv("API_HASH", "a308fac723905cdbd836414b18f3b3d6")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://admin:7518sidd@cluster0.yp1hlwy.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "OGRE")
OWNER_USERNAME = getenv("OWNER_USERNAME", "MonsterKatakuri")
ALIVE_NAME = getenv("ALIVE_NAME", "OGRE")
BOT_USERNAME = getenv("BOT_USERNAME", "UtaXDivaMusicBot")
OWNER_ID = getenv("OWNER_ID", "6046532356")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "UtaMusicAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/RealmBotSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/RealmBotUpdates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5860097723 5860097723").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/2941b97ce13e2347bac8f.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/2941b97ce13e2347bac8f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
PLAY_IMG = getenv("PLAY_IMG", "https://te.legra.ph/file/8bf6a88fa84418a644f5c.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
