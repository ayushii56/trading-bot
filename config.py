import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
    BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

    BINANCE_FUTURES_URL = "https://testnet.binancefuture.com/fapi"


settings = Settings()
