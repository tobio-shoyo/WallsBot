# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    TOKEN = "5275308569:AAGxW6SikyZUlTWRgeI2CQqVyeseSwi2Lfc"
    WEBHOOK = False
    URL = "https://pixabay.com/api/"
    PIX_API = "24446951-f5131704e39ee7908be3a51e4"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
