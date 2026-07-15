"""
Input validation utilities for the trading bot.
"""

from typing import Optional


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol.
    """
    symbol = symbol.strip().upper()

    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    if len(symbol) < 6:
        raise ValueError("Invalid symbol. Example: BTCUSDT")

    return symbol


def validate_side(side: str) -> str:
    """
    Validate order side.
    """
    side = side.strip().upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate order type.
    """
    order_type = order_type.strip().upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate order quantity.
    """
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return quantity


def validate_price(price: Optional[float], order_type: str) -> Optional[float]:
    """
    Validate price for LIMIT orders.
    """
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")

        if price <= 0:
            raise ValueError("Price must be greater than 0.")

    return price