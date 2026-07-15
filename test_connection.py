from pprint import pprint

from bot.client import BinanceClient

client = BinanceClient().get_client()

exchange = client.futures_exchange_info()

print(type(exchange))
print(exchange.keys())