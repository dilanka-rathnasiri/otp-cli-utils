import sys

import typer

from utils import msg_utils

app = typer.Typer()


@app.command()
def validate(otp: int, secret: int):
    if otp == secret:
        msg_utils.print_success_msg("Valid OTP")
    else:
        msg_utils.print_error_msg("Invalid OTP")
        sys.exit(1)


def main():
    app()


if __name__ == "__main__":
    main()
