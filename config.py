import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    BOT_NAME = os.environ.get("BOT_NAME", "")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")
    
    SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "")
    
    UPDATES_CH = os.environ.get("UPDATES_CH", "")
    
    SUPPORT_NAME = os.environ.get("SUPPORT_NAME", "")
    
    UPDATES_NAME = os.environ.get("UPDATES_NAME", "")
    
    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "")
