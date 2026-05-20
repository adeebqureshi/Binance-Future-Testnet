import argparse
import sys

from bot.exceptions import ValidationError
from bot.orders import OrderService
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Place Binance Futures Testnet USDT-M orders."
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol, e.g. BTCUSDT",
    )
    parser.add_argument(
        "--side",
        required=True,
        help="Order side: BUY or SELL",
    )
    parser.add_argument(
        "--type",
        required=True,
        help="Order type: MARKET or LIMIT",
    )
    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity",
    )
    parser.add_argument(
        "--price",
        help="Limit order price (required for LIMIT orders)",
    )

    return parser


def print_order_summary(symbol, side, order_type, quantity, price=None):
    print("\nORDER REQUEST")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    if price is not None:
        print(f"Price: {price}")


def print_order_response(response):
    print("\nORDER RESPONSE")
    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Avg Price: {response.get('avgPrice', 'N/A')}")


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        symbol = args.symbol.upper().strip()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = args.price

        if order_type == "LIMIT":
            price = validate_price(price)

        service = OrderService()

        print_order_summary(symbol, side, order_type, quantity, price)

        if order_type == "MARKET":
            response = service.place_market_order(symbol, side, quantity)
        else:
            response = service.place_limit_order(symbol, side, quantity, price)

        print_order_response(response)
        print("\nSUCCESS")
        return 0

    except ValidationError as exc:
        print(f"\nINPUT ERROR: {exc}")
        return 1
    except Exception as exc:
        print(f"\nFAILED: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
