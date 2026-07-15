"""
Custom exceptions for the Trading Bot.
"""


class TradingBotError(Exception):
    """Base exception for the trading bot."""

    pass


class ValidationError(TradingBotError):
    """Raised when user input is invalid."""

    pass


class ClientInitializationError(TradingBotError):
    """Raised when the Binance client cannot be initialized."""

    pass


class OrderPlacementError(TradingBotError):
    """Raised when an order cannot be placed."""

    pass