from binance.exceptions import BinanceAPIException
from bot.clients import BinanceFuturesClient
from bot.exceptions import BinanceAPIError
from bot.logging_config import setup_logger

logger = setup_logger()

class OrderService:

    def __init__(self):
        self.client = BinanceFuturesClient().get_client()

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(
                "MARKET ORDER | symbol=%s side=%s quantity=%s",
                symbol,
                side,
                quantity,
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

            logger.info("Order response: %s", response)
            return response

        except BinanceAPIException as e:
            logger.error("Binance API error placing market order", exc_info=True)
            raise BinanceAPIError(str(e)) from e
        except Exception as e:
            logger.error("Unexpected error placing market order", exc_info=True)
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(
                "LIMIT ORDER | symbol=%s side=%s quantity=%s price=%s",
                symbol,
                side,
                quantity,
                price,
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

            logger.info("Order response: %s", response)
            return response

        except BinanceAPIException as e:
            logger.error("Binance API error placing limit order", exc_info=True)
            raise BinanceAPIError(str(e)) from e
        except Exception as e:
            logger.error("Unexpected error placing limit order", exc_info=True)
            raise
