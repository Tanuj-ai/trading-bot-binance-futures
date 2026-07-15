import os

from binance.client import Client
from dotenv import load_dotenv

from bot.logging_config import logger

load_dotenv()


class BinanceClient:
    """
    Binance Futures Testnet client wrapper.
    """

    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError(
                "BINANCE_API_KEY and BINANCE_API_SECRET must be set in the .env file."
            )

        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True,
        )

        logger.info("Binance client initialized.")

    def get_client(self):
        return self.client