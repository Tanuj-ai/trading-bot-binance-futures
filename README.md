# Binance Futures Testnet Trading Bot

A command-line trading bot built using Python that allows users to place MARKET and LIMIT orders on the Binance USDT-M Futures Testnet.

This project was developed as part of a backend development assignment with a focus on clean code, modular architecture, input validation, structured logging, and proper error handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- Command-line interface using Typer
- Rich formatted console output
- Input validation before placing orders
- Structured logging to `trading_bot.log`
- Environment variable support using `.env`
- Modular and reusable code structure

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── cli.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── trading_bot.log
```

---

## Technologies Used

- Python 3.9+
- python-binance
- Typer
- Rich
- python-dotenv

---

## Installation

Clone the repository

```bash
git clone https://github.com/Tanuj-ai/trading-bot-binance-futures.git

cd trading-bot-binance-futures
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Binance Testnet Setup

1. Create a Binance Futures Testnet account.
2. Generate your API Key and Secret.
3. Create a `.env` file in the project root.

Example:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

## Running the Bot

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 150000
```

---

## Sample Output

```
Order Summary

Symbol        BTCUSDT
Side          BUY
Order Type    MARKET
Quantity      0.001

✓ Order Submitted Successfully

Order Response

Order ID      21863507324
Status        NEW
Executed Qty  0.0000
```

---

## Logging

Every order request, API response, and error is written to:

```
trading_bot.log
```

This makes it easier to debug issues and track order activity.

---

## Example Log Output

### Successful MARKET BUY

```text
2026-07-15 14:15:23 | INFO | TradingBot | Initializing Binance Testnet client...
2026-07-15 14:15:23 | INFO | TradingBot | Successfully connected to Binance Futures Testnet.
2026-07-15 14:15:23 | INFO | TradingBot | Placing Order | Symbol=BTCUSDT, Side=BUY, Type=MARKET, Quantity=0.001, Price=None
2026-07-15 14:15:23 | INFO | TradingBot | Order placed successfully.
2026-07-15 14:15:23 | INFO | TradingBot | Order Summary | OrderID=21863507324 | Symbol=BTCUSDT | Side=BUY | Type=MARKET | Status=NEW | Quantity=0.0010 | Executed=0.0000 | Price=0.00
```

### Successful LIMIT SELL

```text
2026-07-15 14:21:04 | INFO | TradingBot | Initializing Binance Testnet client...
2026-07-15 14:21:04 | INFO | TradingBot | Successfully connected to Binance Futures Testnet.
2026-07-15 14:21:04 | INFO | TradingBot | Placing Order | Symbol=BTCUSDT, Side=SELL, Type=LIMIT, Quantity=0.001, Price=150000
2026-07-15 14:21:05 | INFO | TradingBot | Order placed successfully.
2026-07-15 14:21:05 | INFO | TradingBot | Order Summary | OrderID=21863591234 | Symbol=BTCUSDT | Side=SELL | Type=LIMIT | Status=NEW | Quantity=0.0010 | Executed=0.0000 | Price=150000.00
```

## Assumptions

- The application is intended for the Binance Futures Testnet.
- API credentials are provided using environment variables.
- MARKET and LIMIT orders are supported.
- Users have a valid Testnet account and API credentials.

---

## Bonus Improvements

In addition to the core requirements, the project also includes:

- Rich formatted terminal output
- Custom exception hierarchy
- Modular architecture
- Environment variable support
- Structured logging with log rotation

---

## Future Improvements

Some features that can be added in the future:

- Stop Loss and Take Profit orders
- OCO Orders
- Order cancellation
- Position management
- Account balance command
- Open orders command

---

## Author

**Tanuj Rawat**

GitHub: https://github.com/Tanuj-ai