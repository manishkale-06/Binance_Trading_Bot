import argparse
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import validate_order
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    parser.add_argument("--sl", type=float)
    parser.add_argument("--tp", type=float)

    args = parser.parse_args()

    error = validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if error:
        print(f"Error: {error}")
        return

    client = BinanceClient().get_client()
    order_service = OrderService(client)

    order = order_service.place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if "error" in order:
        print(f"Order Failed: {order['error']}")
        return

    print("\nORDER SUCCESS")
    print("-" * 30)
    print(f"Symbol       : {args.symbol}")
    print(f"Side         : {args.side}")
    print(f"Type         : {args.type}")
    print(f"Order ID     : {order.get('orderId')}")
    print(f"Status       : {order.get('status')}")
    print(f"Executed Qty : {order.get('executedQty')}")

    if args.sl or args.tp:
        print("\nPlacing Stop-Loss / Take-Profit...")
        results = order_service.place_sl_tp(
            args.symbol,
            args.side,
            args.sl,
            args.tp
        )

        for label, res in results:
            if label == "error":
                print(f"SL/TP Error: {res}")
            else:
                print(f"{label} Order ID: {res.get('orderId')}")

if __name__ == "__main__":
    main()