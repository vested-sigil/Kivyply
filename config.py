import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    B4A_API_URL = "https://parseapi.back4app.com/classes/"

    # Headers for Game app
    HEADERS_GAME = {
        "X-Parse-Application-Id": os.getenv("GAME_BACK4APP_AppID"),
        "X-Parse-REST-API-Key": os.getenv("GAME_X-Parse-REST-API-Key"),
        "Content-Type": "application/json"
    }
    HEADERS_LORE = {
        "X-Parse-Application-Id": os.getenv("LORE_BACK4APP_AppID"),
        "X-Parse-REST-API-Key": os.getenv("LORE_X-Parse-REST-API-Key"),
        "Content-Type": "application/json"
    }
    HEADERS_FLARE = {
        "X-Parse-Application-Id": os.getenv("FLARE_BACK4APP_AppID"),
        "X-Parse-REST-API-Key": os.getenv("FLARE_X-Parse-REST-API-Key"),
        "Content-Type": "application/json"
    }
    HEADERS_AUTOPROMPTER = {
        "X-Parse-Application-Id": os.getenv("AUTOPROMPTER_BACK4APP_AppID"),
        "X-Parse-REST-API-Key": os.getenv("AUTOPROMPTER_X-Parse-REST-API-Key"),
        "Content-Type": "application/json"
    }
    HEADERS_IQUEUE = {
        "X-Parse-Application-Id": os.getenv("IQUEUE_BACK4APP_AppID"),
        "X-Parse-REST-API-Key": os.getenv("IQUEUE_X-Parse-REST-API-Key"),
        "Content-Type": "application/json"
    }
