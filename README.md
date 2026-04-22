# Binance Futures Testnet Trading Bot 
A simple Python trading bot which is able to place orders on Binance Futures Testnet, with CLI support, logging, validation mechanisms.

## Objective

This project was developed as an interview assignment to: 

- Place MARKET and LIMIT orders on Binance
- Supports BUY and SELL operations 
- Implement logging, validation, and error handling
- Implement CLI- based interaction

## Setup Instructions

### Clone the Project
git clone https://github.com/manishkale-06/Binance_Trading_Bot.git
cd Binance_Trading_Bot

### Install Dependencies
pip install -r requirements.txt

### Create Binance Future Testnet Account
- Register on Binance Futures Testnet
- Generate API Key and Secret

### Configure API Keys
Open:
botfiles/client.py

Replace:

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

## How to Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000

### With Stop-Loss and Take-Profit
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --sl 58000 --tp 62000

### Run with GUI
python ui.py

A window will open where you can:

- Enter order details
- Place orders interactively

## Logging

All activity is stored in:
trading_bot.log

Includes:
- Order requests 
- API responses 
- Errors

## Assumptions

- Testnet account has sufficient balance
- Symbols are availble(like BTCUSDT)
- Internet connection is stable

## Dependencies 

python-binance

## Example Output

ORDER SUCCESS 
Order ID: 12345678 
Status: FILLED 
Executed Qty: 0.001

