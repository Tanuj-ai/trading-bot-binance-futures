import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Log file name
LOG_FILE = "trading_bot.log"


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.
    Logs are written both to the console and to a log file.
    """

    logger = logging.getLogger("TradingBot")

    # Prevent duplicate handlers if called multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Create log file if it doesn't exist
    Path(LOG_FILE).touch(exist_ok=True)

    # File handler with rotation
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )

    # Console handler
    console_handler = logging.StreamHandler()

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Shared logger instance
logger = setup_logger()