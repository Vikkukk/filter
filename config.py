
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5735937868:AAG6rfVcLc-OEJV_kzaNIJY1XTtbGlTnWcs")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "16869866"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "b6defd08178346ef6d0539e4db127acf")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCr97P4mi8BgW4OI04VyJXThVclfrcBk4F3qnSsW8pQsXuWG6D3OGrMVJ36onWi8fSQ-fn7hF7UGhIBLJnJuiTQEUCKlmlFwpeMgGO4cxNs_BO2C-SnCYr96ygzchSxyurFrv7vWGzDifFqmfzW-SahFMFJS7_ke_U7TUCBnA28jcuzjtfPZn6HK3MTN0AT9fDwVe1J_Yup8cQPoLQQR5L-4uTcoAzNCmzK6pR8KhZyVRGAJLVuxFSQUNxmECMeScmb4YvqrNvmIAwOxS8T7J9OHFGg7sLIAYjljLcWavDo0LiuhG2qIVwOAvYXxM2KYcEUMFKz5mt7fFqA_knt6FKxcKPvpwA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Vikkukk:Lami@123#@cluster0.jpd0xtm.mongodb.net/?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1889791911").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "no").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
