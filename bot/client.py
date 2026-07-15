"""
Binance client configuration.
"""

import os

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv

from bot.exceptions import ClientInitializationError
from bot.logging_config import logger

load_dotenv()


class BinanceClient:
    """
    Binance Futures client wrapper.
    """

    def __init__(self) -> None:

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ClientInitializationError(
                "BINANCE_API_KEY and BINANCE_API_SECRET must be set in the .env file."
            )

        try:

            self.client = Client(
                api_key=self.api_key,
                api_secret=self.api_secret,
                testnet=True,
            )

            self.client.futures_ping()

            logger.info("Binance client initialized.")

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise ClientInitializationError(str(e))

        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")
            raise ClientInitializationError(str(e))

        except Exception as e:
            logger.exception(e)
            raise ClientInitializationError(str(e))

    def get_client(self) -> Client:
        """
        Return configured client.
        """
        return self.client