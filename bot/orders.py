import logging
from binance.exceptions import BinanceAPIException

class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logging.info(f"Placing Order: {symbol} {side} {order_type} {quantity} {price}")

            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            else:
                raise ValueError("Invalid order type")

            logging.info(f"Order Response: {order}")
            return order

        except BinanceAPIException as e:
            logging.error(f"API Error: {e}")
            return {"error": str(e)}

        except Exception as e:
            logging.error(f"General Error: {e}")
            return {"error": str(e)}

    def place_sl_tp(self, symbol, side, stop_loss=None, take_profit=None):
        results = []
        try:
            exit_side = "SELL" if side == "BUY" else "BUY"

            if stop_loss:
                sl = self.client.futures_create_order(
                    symbol=symbol,
                    side=exit_side,
                    type="STOP_MARKET",
                    stopPrice=stop_loss,
                    closePosition=True
                )
                results.append(("Stop Loss", sl))

            if take_profit:
                tp = self.client.futures_create_order(
                    symbol=symbol,
                    side=exit_side,
                    type="TAKE_PROFIT_MARKET",
                    stopPrice=take_profit,
                    closePosition=True
                )
                results.append(("Take Profit", tp))

            logging.info(f"SL/TP Orders: {results}")
            return results

        except BinanceAPIException as e:
            logging.error(f"SL/TP Error: {e}")
            return [("error", str(e))]