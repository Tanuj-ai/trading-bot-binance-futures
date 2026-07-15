"""
Order management for the Binance Futures Trading Bot.
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
        """Initialize the order manager."""
        self.client = BinanceClient().get_client()

    @staticmethod
    def _get_side(side: str) -> str:
        """
        Convert BUY/SELL string into Binance enum.
        """
        return SIDE_BUY if side.upper() == "BUY" else SIDE_SELL

    def _log_order_summary(self, response: Dict[str, Any]) -> None:
        """
        Log a concise order summary.
        """
        logger.info(
            "Order Summary | "
            f"OrderID={response.get('orderId')} | "
            f"Symbol={response.get('symbol')} | "
            f"Side={response.get('side')} | "
            f"Type={response.get('type')} | "
            f"Status={response.get('status')} | "
            f"Quantity={response.get('origQty')} | "
            f"Executed={response.get('executedQty')} | "
            f"Price={response.get('price')}"
        )

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Place a MARKET or LIMIT order.

        Args:
            symbol: Trading symbol (e.g. BTCUSDT)
            side: BUY or SELL
            order_type: MARKET or LIMIT
            quantity: Order quantity
            price: Required for LIMIT orders

        Returns:
            Binance API response dictionary.
        """

        logger.info(
            "Placing Order | "
            f"Symbol={symbol}, "
            f"Side={side}, "
            f"Type={order_type}, "
            f"Quantity={quantity}, "
            f"Price={price}"
        )

        try:
            side_enum = self._get_side(side)

            if order_type.upper() == "MARKET":

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

            self._log_order_summary(response)

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")

            raise OrderPlacementError(
                f"Binance rejected the order: {e}"
            ) from e

        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")

            raise OrderPlacementError(
                "Network error while communicating with Binance."
            ) from e

        except Exception as e:
            logger.exception("Unexpected error while placing order.")

            raise OrderPlacementError(
                "Unexpected error occurred while placing the order."
            ) from e