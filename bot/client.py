"""
Binance Futures Testnet client configuration.
"""

import os

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv

from bot.exceptions import ClientInitializationError
from bot.logging_config import logger

# Load environment variables
load_dotenv()


class BinanceClient:
    """
    Creates and manages a Binance Futures Testnet client.

    API credentials are loaded from the .env file.
    """

    def __init__(self) -> None:
        """
        Initialize the Binance client.
        """

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ClientInitializationError(
                "Missing Binance API credentials. "
                "Please configure BINANCE_API_KEY and "
                "BINANCE_API_SECRET in the .env file."
            )

        try:
            logger.info("Initializing Binance Testnet client...")

            self.client = Client(
                api_key=self.api_key,
                api_secret=self.api_secret,
                testnet=True,
            )

            # Verify connection
            self.client.futures_ping()

            logger.info(
                "Successfully connected to Binance Futures Testnet."
            )

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise ClientInitializationError(
                "Failed to authenticate with Binance."
            ) from e

        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")
            raise ClientInitializationError(
                "Unable to connect to Binance."
            ) from e

        except Exception as e:
            logger.exception("Unexpected error during client initialization.")
            raise ClientInitializationError(
                "Unexpected error while initializing Binance client."
            ) from e

    def get_client(self) -> Client:
        """
        Return the configured Binance client.
        """
        return self.client

    def check_connection(self) -> bool:
        """
        Verify connectivity to Binance Futures Testnet.

        Returns:
            True if the connection is successful.
        """

        try:
            self.client.futures_ping()
            return True

        except Exception:
            return False