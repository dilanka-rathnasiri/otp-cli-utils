import sys

import typer

from otp_cli_utils.constants import help_texts
from otp_cli_utils.services import img_services, otp_services, qr_services
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


@app.command("generate-qr-code", help=help_texts.GENERATE_SECRET_QR_CODE)
def generate_secret_qr_code(
    secret: str = typer.Argument(help="OTP secret"),
    label: str = typer.Argument(help="Label for the OTP secret"),
    issuer: str = typer.Argument(help="Issuer for the OTP secret"),
    file_name: str = typer.Argument(
        default="secret_qr", help="File name for the QR code"
    ),
):
    """
    Generate a Google Authenticator Compatible QR code
    """
    secret = otp_services.generate_otp_secret()
    uri = otp_services.generate_uri(secret, label, issuer)
    img = qr_services.generate_qr_code(uri)
    img_services.save_image(img, file_name)


def main():
    app()


if __name__ == "__main__":
    main()
