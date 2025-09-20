import sys

import typer

from otp_cli_utils.constants import command_texts, help_texts
from otp_cli_utils.services import img_services, otp_services, qr_services
from otp_cli_utils.utils import msg_utils

app = typer.Typer(
    name="otp-cli-utils",
    help=help_texts.MAIN,
)


@app.command(command_texts.GET_OTP, help=help_texts.GET_OTP)
def get_otp(secret: str = typer.Argument(help=help_texts.SECRET_ARG)):
    """
    Get the current OTP code for the given secret
    """
    otp = otp_services.get_otp(secret)
    msg_utils.print_success_msg(f"Current OTP: {otp}")


@app.command(command_texts.VALIDATE, help=help_texts.VALIDATE)
def validate(
    secret: str = typer.Argument(help=help_texts.SECRET_ARG),
    otp: str = typer.Argument(help=help_texts.OTP_ARG),
    window_count: int = typer.Option(
        0,
        "--window-count",
        "-w",
        help=help_texts.WINDOW_COUNT_ARG,
    ),
):
    """
    Validate if the provided OTP matches the expected value for the given secret
    """
    if otp_services.validate_otp(secret, otp, window_count):
        msg_utils.print_success_msg("Valid OTP")
    else:
        msg_utils.print_error_msg("Invalid OTP")
        sys.exit(1)


@app.command(command_texts.GENERATE_SECRET, help=help_texts.GENERATE_SECRET)
def generate_secret():
    """
    Generate a new secure random secret key for OTP generation
    """
    secret = otp_services.generate_otp_secret()
    msg_utils.print_success_msg(f"Generated OTP secret: {secret}")


@app.command(
    command_texts.GENERATE_SECRET_QR_CODE, help=help_texts.GENERATE_SECRET_QR_CODE
)
def generate_secret_qr_code(
    label: str = typer.Argument(help=help_texts.LABEL_ARG),
    issuer: str = typer.Argument(help=help_texts.ISSUER_ARG),
    file_name: str = typer.Argument(
        default="otp_secret_qr", help=help_texts.FILENAME_ARG
    ),
):
    """
    Generate a Google Authenticator Compatible QR code with a new OTP secret
    """
    secret = otp_services.generate_otp_secret()
    uri = otp_services.generate_uri(secret, label, issuer)
    img = qr_services.generate_qr_code(uri)
    saved_file_path = img_services.save_image(img, file_name)
    message = (
        f"Generated OTP secret: {secret}\n\n"
        f"OTP secret QR code saved to: {saved_file_path}"
    )
    msg_utils.print_success_msg(message)


def main():
    app()


if __name__ == "__main__":
    main()
