from bot.exceptions import ValidationError

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_side(side):

    side = side.upper()

    if side not in VALID_SIDES:
        raise ValidationError(
            f"Invalid side. Use {VALID_SIDES}"
        )

    return side

def validate_order_type(order_type):

    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValidationError(
            f"Invalid order type. Use {VALID_ORDER_TYPES}"
        )

    return order_type

def validate_quantity(quantity):

    quantity = float(quantity)

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than 0"
        )

    return quantity

def validate_price(price):

    if price is None:
        raise ValidationError(
            "Price is required for LIMIT orders"
        )

    price = float(price)

    if price <= 0:
        raise ValidationError(
            "Price must be greater than 0"
        )

    return price