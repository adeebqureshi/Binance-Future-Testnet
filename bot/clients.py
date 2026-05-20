import os

from dotenv import load_dotenv
from binance.client import Client

from bot.exceptions import ConfigurationError

load_dotenv()

class BinanceFuturesClient:

    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ConfigurationError(
                "BINANCE_API_KEY and BINANCE_API_SECRET must be set in environment or .env"
            )

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client
