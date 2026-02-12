class ValidationError(Exception):
    """Custom validation error."""
    pass


def validate_symbol(symbol: str) -> str:
    symbol = symbol.upper().strip()

    if not symbol.isalnum():
        raise ValidationError("Symbol must be alphanumeric (e.g., BTCUSDT).")

    return symbol


def validate_side(side: str) -> str:
    side = side.upper().strip()

    if side not in {"BUY", "SELL"}:
        raise ValidationError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper().strip()

    if order_type not in {"MARKET", "LIMIT", "STOP_LIMIT"}:
        raise ValidationError("Order type must be MARKET, LIMIT, or STOP_LIMIT.")

    return order_type


def validate_positive_number(value, field_name):
    try:
        val = float(value)

        if val <= 0:
            raise ValidationError(f"{field_name} must be greater than 0.")

        return val

    except (ValueError, TypeError):
        raise ValidationError(f"{field_name} must be a valid number.")


def validate_prices(order_type, price=None, stop_price=None):
    if order_type == "LIMIT":
        price = validate_positive_number(price, "Price")

    elif order_type == "STOP_LIMIT":
        price = validate_positive_number(price, "Price")
        stop_price = validate_positive_number(stop_price, "Stop price")

    return price, stop_price


def validate_order_inputs(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
    stop_price=None,
):
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_positive_number(quantity, "Quantity")

    price, stop_price = validate_prices(order_type, price, stop_price)

    return {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "price": price,
        "stopPrice": stop_price,
    }
