"""
Input validation utilities for the Binance Futures Trading Bot.
"""

from typing import Optional

from bot.exceptions import ValidationError

VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol.

    Example:
        BTCUSDT
        ETHUSDT
    """
    symbol = symbol.strip().upper()

    if not symbol:
        raise ValidationError("Trading symbol cannot be empty.")

    if len(symbol) < 6:
        raise ValidationError(
            "Invalid trading symbol. Example: BTCUSDT"
        )

    return symbol


def validate_side(side: str) -> str:
    """
    Validate order side.
    """

    side = side.strip().upper()

    if side not in VALID_SIDES:
        raise ValidationError(
            "Order side must be either BUY or SELL."
        )

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate order type.
    """

    order_type = order_type.strip().upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValidationError(
            "Order type must be MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate order quantity.
    """

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero."
        )

    return quantity


def validate_price(
    price: Optional[float],
    order_type: str,
) -> Optional[float]:
    """
    Validate LIMIT order price.
    """

    if order_type == "LIMIT":

        if price is None:
            raise ValidationError(
                "Price is required for LIMIT orders."
            )

        if price <= 0:
            raise ValidationError(
                "Price must be greater than zero."
            )

    return price