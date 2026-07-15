"""
Command Line Interface for the Binance Futures Trading Bot.
"""

from datetime import datetime
from typing import Optional

import typer
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from bot.exceptions import TradingBotError
from bot.orders import OrderManager
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)

app = typer.Typer(
    help="Binance Futures Testnet Trading Bot",
    add_completion=False,
)

console = Console()


@app.callback(invoke_without_command=True)
def trade(
    ctx: typer.Context,
    symbol: str = typer.Option(..., help="Trading symbol (Example: BTCUSDT)"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: Optional[float] = typer.Option(
        None,
        help="Required only for LIMIT orders",
    ),
):
    """
    Place an order on Binance Futures Testnet.
    """

    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        summary = Table(
            title="Order Summary",
            box=box.ROUNDED,
            header_style="bold cyan",
        )

        summary.add_column("Field", style="cyan", width=18)
        summary.add_column("Value", style="green")

        summary.add_row("Symbol", symbol)
        summary.add_row("Side", side)
        summary.add_row("Order Type", order_type)
        summary.add_row("Quantity", str(quantity))
        summary.add_row("Price", str(price) if price else "-")

        console.print(summary)
        console.print()

        manager = OrderManager()

        response = manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        console.print(
            Panel.fit(
                "[bold green]✓ Order Submitted Successfully[/bold green]",
                border_style="green",
            )
        )

        result = Table(
            title="Order Response",
            box=box.ROUNDED,
            header_style="bold green",
        )

        result.add_column("Field", style="cyan", width=18)
        result.add_column("Value", style="yellow")

        fields = [
            "orderId",
            "symbol",
            "status",
            "side",
            "type",
            "origQty",
            "executedQty",
            "price",
        ]

        for field in fields:
            result.add_row(field, str(response.get(field, "-")))

        console.print(result)

        console.print()

        console.print(
            f"[bold cyan]Timestamp:[/bold cyan] "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

    except TradingBotError as error:

        console.print(
            Panel.fit(
                str(error),
                title="Error",
                border_style="red",
            )
        )

    except Exception as error:

        console.print(
            Panel.fit(
                str(error),
                title="Unexpected Error",
                border_style="red",
            )
        )


if __name__ == "__main__":
    app()