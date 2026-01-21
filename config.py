from os import environ

# Telegram Account Api Id And Api Hash
API_HASH = environ.get("API_HASH", "82f0b6610caaacf2c6e0974ddbab2bf5")

# Your Main Bot Token 

BOT_TOKEN = environ.get("BOT_TOKEN", "8257547423:AAE_rDTcjikUpG0ZlGBFmHLoDASruTLNLuo")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7468895020")) # Owner Id or Admin Id

MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://test:test@test01.7rr7ogr.mongodb.net/?appName=TEST01")
