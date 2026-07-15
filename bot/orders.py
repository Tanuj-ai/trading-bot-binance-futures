"""
Order placement logic for Binance Futures Testnet.
"""

from binance.enums import (
    SIDE_BUY,
    SIDE_SELL,
    FUTURE_ORDER_TYPE_MARKET,
    FUTURE_ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC,
)
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import BinanceClient
from bot.logging_config import logger


class OrderManager:
    """
    Handles Binance Futures order placement.
    """

    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float = None,
    ):
        """
        Place a MARKET or LIMIT order.
        """

        logger.info(
            f"Request -> Symbol={symbol}, Side={side}, "
            f"Type={order_type}, Qty={quantity}, Price={price}"
        )

        try:

            if side == "BUY":
                side = SIDE_BUY
            else:
                side = SIDE_SELL

            if order_type == "MARKET":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=FUTURE_ORDER_TYPE_MARKET,
                    quantity=quantity,
                )

            else:

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=FUTURE_ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC,
                )

            logger.info(f"Response -> {response}")

            return response

        except BinanceAPIException as e:

            logger.error(f"Binance API Error: {e}")

            raise

        except BinanceRequestException as e:

            logger.error(f"Network Error: {e}")

            raise

        except Exception as e:

            logger.exception(f"Unexpected Error: {e}")

            raise