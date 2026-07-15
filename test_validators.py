from bot.validators import *

print(validate_symbol("btcusdt"))
print(validate_side("buy"))
print(validate_order_type("market"))
print(validate_quantity(0.01))
print(validate_price(50000, "LIMIT"))