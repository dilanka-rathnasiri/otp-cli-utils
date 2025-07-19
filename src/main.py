import sys

import typer

from services.otp_services import validate_otp
from utils import msg_utils

app = typer.Typer()


@app.command()
def validate(otp: str, secret: str):
    if validate_otp(otp, secret):
        msg_utils.print_success_msg("Valid OTP")
    else:
        msg_utils.print_error_msg("Invalid OTP")
        sys.exit(1)


def main():
    app()


if __name__ == "__main__":
    main()
