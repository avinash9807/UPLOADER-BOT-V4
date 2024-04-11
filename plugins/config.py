import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7180353652:AAGAMKtdPYldvxzythfbJv1V6ZKvJomcZfQ")
    
    API_ID = int(os.environ.get("API_ID", "18724699"))
    
    API_HASH = os.environ.get("API_HASH", "c05642ac6905c60778182c622e03f49d")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000

    #PORT = int(os.environ.get('PORT', 5000))
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "By Avinash Chauhan"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://lovepoint9807:9807301306@cluster0.suofhqg.mongodb.net/?retryWrites=true&w=majority")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002028635056"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002069976332")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "800000580"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "AvinashL_bot")
    
