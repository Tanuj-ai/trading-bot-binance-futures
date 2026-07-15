"""
Order management for Binance Futures Testnet.
"""

from typing import Any, Dict, Optional

from binance.enums import (
    FUTURE_ORDER_TYPE_LIMIT,
    FUTURE_ORDER_TYPE_MARKET,
    SIDE_BUY,
    SIDE_SELL,
    TIME_IN_FORCE_GTC,
)
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import BinanceClient
from bot.exceptions import OrderPlacementError
from bot.logging_config import logger


class OrderManager:
    """
    Handles Binance Futures order placement.
    """

    def __init__(self) -> None:
        self.client = BinanceClient().get_client()

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Place MARKET or LIMIT order.
        """

        logger.info(
            f"Placing order | "
            f"Symbol={symbol}, "
            f"Side={side}, "
            f"Type={order_type}, "
            f"Quantity={quantity}, "
            f"Price={price}"
        )

        side_enum = SIDE_BUY if side == "BUY" else SIDE_SELL

        try:

            if order_type == "MARKET":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=FUTURE_ORDER_TYPE_MARKET,
                    quantity=quantity,
                )

            else:

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=FUTURE_ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC,
                )

            logger.info("Order placed successfully.")
            logger.info(response)

            return response

        except BinanceAPIException as e:

            logger.error(f"Binance API Error: {e}")
            raise OrderPlacementError(str(e))

        except BinanceRequestException as e:

            logger.error(f"Network Error: {e}")
            raise OrderPlacementError(
                "Network error while placing the order."
            )

        except Exception as e:

            logger.exception(e)
            raise OrderPlacementError(
                "Unexpected error occurred while placing the order."
            )