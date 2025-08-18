import sys

import typer

from otp_cli_utils.services import otp_services
from otp_cli_utils.utils import msg_utils

app = typer.Typer(
    name="otp-cli-utils",
    help="cli tool for OTP",
)


@app.command("get-otp", help="get otp code")
def get_otp(secret: str = typer.Argument(help="OTP secret")):
    """
    Get the current OTP code for the given secret
    """
    otp = otp_services.get_otp(secret)
    msg_utils.print_success_msg(f"Current OTP: {otp}")


@app.command(help="validate otp")
def validate(
    otp: str = typer.Argument(help="The OTP code to validate"),
    secret: str = typer.Argument(help="OTP secret"),
):
    """
    Validate if the provided OTP matches the expected value for the given secret
    """
    if otp_services.validate_otp(otp, secret):
        msg_utils.print_success_msg("Valid OTP")
    else:
        msg_utils.print_error_msg("Invalid OTP")
        sys.exit(1)


@app.command("generate-secret", help="generate a new OTP secret")
def generate_secret():
    """
    Generate a new secure random secret key for OTP generation
    """
    secret = otp_services.generate_otp_secret()
    msg_utils.print_success_msg(f"Generated OTP secret: {secret}")


def main():
    app()


if __name__ == "__main__":
    main()
