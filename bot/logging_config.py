import logging
import os

def setup_logger():

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler("logs/trading_bot.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger