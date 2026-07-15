from binance.client import Client

client = Client()

info = client.futures_exchange_info()

print(type(info))
print(info.keys() if isinstance(info, dict) else info)