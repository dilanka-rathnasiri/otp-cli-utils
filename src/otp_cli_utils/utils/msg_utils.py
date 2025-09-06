from rich import print
from rich.box import HEAVY
from rich.panel import Panel


def print_panel(msg: str, color: str) -> None:
    """
    Print a message in a styled panel

    Args:
        msg (str): The message to display
        color (str): The color to use for the panel text
    """
    print(Panel.fit(msg, style=f"{color} bold", box=HEAVY))


def print_error_msg(msg: str) -> None:
    """
    Print an error message in a red panel

    Args:
        msg (str): The error message to display
    """
    print_panel(msg, "red")


def print_success_msg(msg: str) -> None:
    """
    Print a success message in a green panel

    Args:
        msg (str): The success message to display
    """
    print_panel(msg, "green")
