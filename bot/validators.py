def validate_order(symbol, side, order_type, quantity, price):
    if not symbol:
        return "Symbol is required"

    if side not in ["BUY", "SELL"]:
        return "Side must be BUY or SELL"

    if order_type not in ["MARKET", "LIMIT"]:
        return "Order type must be MARKET or LIMIT"

    try:
        float(quantity)
    except:
        return "Quantity must be a number"

    if order_type == "LIMIT":
        if price is None:
            return "Price required for LIMIT order"
        try:
            float(price)
        except:
            return "Invalid price"

    return None