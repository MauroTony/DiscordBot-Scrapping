import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class GeneralConfig:

    DISCORD_TOKEN: str = os.getenv('DISCORD_TOKEN')
    CREDENTIAL_USERNAME: str = os.getenv('CREDENTIAL_USERNAME')
    CREDENTIAL_PASSWORD: str = os.getenv('CREDENTIAL_PASSWORD')
    CREDENTIAL_TYPE: str = os.getenv('CREDENTIAL_TYPE')
    URL_LOGIN_TWITTER: str = "https://medium.com/m/account/authenticate-twitter?state=twitter-%7Chttps%3A%2F%2Fmedium.com%2F%3Fsource%3Dlogin--------------------------lo_home_nav-----------%7Clogin&source=login--------------------------lo_home_nav-----------"

def get_config() -> GeneralConfig:
    return GeneralConfig()