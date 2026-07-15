"""
CLI entry point for the Binance Futures Trading Bot.
"""

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

app = typer.Typer(help="Binance Futures Testnet Trading Bot")

console = Console()


@app.command()
def trade(
    symbol: str = typer.Option(..., help="Trading symbol (e.g. BTCUSDT)"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: Optional[float] = typer.Option(
        None,
        help="Price (required for LIMIT orders)"
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
            show_header=True,
            header_style="bold cyan",
        )

        summary.add_column("Field")
        summary.add_column("Value")

        summary.add_row("Symbol", symbol)
        summary.add_row("Side", side)
        summary.add_row("Order Type", order_type)
        summary.add_row("Quantity", str(quantity))
        summary.add_row("Price", str(price) if price else "-")

        console.print(summary)

        manager = OrderManager()

        response = manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        console.print()

        console.print(
            Panel.fit(
                "[bold green]✓ Order Submitted Successfully[/bold green]"
            )
        )

        result = Table(
            title="Order Response",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold green",
        )

        result.add_column("Field")
        result.add_column("Value")

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

    except TradingBotError as e:

        console.print(
            Panel.fit(
                f"[bold red]{e}[/bold red]"
            )
        )

    except Exception as e:

        console.print(
            Panel.fit(
                f"[bold red]Unexpected Error:[/bold red]\n{e}"
            )
        )


if __name__ == "__main__":
    app()