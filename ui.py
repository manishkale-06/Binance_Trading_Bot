import tkinter as tk
from tkinter import messagebox
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import validate_order
from bot.logging_config import setup_logging

setup_logging()

client = BinanceClient().get_client()
order_service = OrderService(client)

def place_order():
    symbol = symbol_entry.get().upper()
    side = side_entry.get().upper()
    order_type = type_entry.get().upper()
    quantity = quantity_entry.get()
    price = price_entry.get()

    error = validate_order(symbol, side, order_type, quantity, price)
    if error:
        messagebox.showerror("Error", error)
        return

    order = order_service.place_order(symbol, side, order_type, float(quantity), price)

    if "error" in order:
        output.insert(tk.END, f"Error: {order['error']}\n")
    else:
        output.insert(tk.END, f"Order ID: {order.get('orderId')}\n")

root = tk.Tk()
root.title("Trading Bot UI")
root.geometry("400x400")

tk.Label(root, text="Symbol").pack()
symbol_entry = tk.Entry(root)
symbol_entry.insert(0, "BTCUSDT")
symbol_entry.pack()

tk.Label(root, text="Side (BUY/SELL)").pack()
side_entry = tk.Entry(root)
side_entry.insert(0, "BUY")
side_entry.pack()

tk.Label(root, text="Type (MARKET/LIMIT)").pack()
type_entry = tk.Entry(root)
type_entry.insert(0, "MARKET")
type_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.insert(0, "0.001")
quantity_entry.pack()

tk.Label(root, text="Price (for LIMIT)").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Button(root, text="Place Order", command=place_order).pack(pady=10)

output = tk.Text(root, height=10)
output.pack()

root.mainloop()