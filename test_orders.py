from pprint import pprint

from bot.orders import OrderManager

manager = OrderManager()

response = manager.place_order(
    symbol="BTCUSDT",
    side="BUY",
    order_type="MARKET",
    quantity=0.001,
)

print(type(response))

pprint(response)