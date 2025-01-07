from os import environ 

class Config:
    API_ID = environ.get("API_ID", "15090480")
    API_HASH = environ.get("API_HASH", "a3df4aae09f5add6c74658ecf4e98803")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7338587731:AAE03FVOViKdUBa1H5HVHppoSZ6tIGdarOY") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://rojagopu4596:A0eyvi1b3Xd0jVya@cluster0.b26do.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '400772525').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
