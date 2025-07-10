from rich import print
from rich.box import HEAVY
from rich.panel import Panel


def print_panel(msg: str, color: str) -> None:
    print(Panel.fit(msg, style=f"{color} bold", box=HEAVY))


def print_error_msg(msg: str) -> None:
    print_panel(msg, "red")


def print_success_msg(msg: str) -> None:
    print_panel(msg, "green")
