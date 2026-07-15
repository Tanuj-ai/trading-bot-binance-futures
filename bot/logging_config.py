"""
Logging configuration for the Trading Bot.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = "trading_bot.log"


def setup_logger() -> logging.Logger:
    """
    Configure application logger.
    """

    logger = logging.getLogger("TradingBot")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    Path(LOG_FILE).touch(exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File logger
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Console logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()