import sys

import typer

from otp_cli_utils.services.otp_services import validate_otp
from otp_cli_utils.utils import msg_utils

app = typer.Typer(
    name="otp-cli-utils",
    help="cli tool for OTP",
)


@app.command(help="validate otp")
def validate(
    otp: str = typer.Argument(help="The OTP code to validate"),
    secret: str = typer.Argument(help="OTP secret"),
):
    """
    Validate if the provided OTP matches the expected value for the given secret
    """
    if validate_otp(otp, secret):
        msg_utils.print_success_msg("Valid OTP")
    else:
        msg_utils.print_error_msg("Invalid OTP")
        sys.exit(1)


def main():
    app()


if __name__ == "__main__":
    main()
