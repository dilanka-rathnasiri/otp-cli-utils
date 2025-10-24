import sys

import typer

from otp_cli_utils.constants import command_texts, error_texts, help_texts
from otp_cli_utils.errors.invalid_input_error import InvalidInputError
from otp_cli_utils.services import (
    img_services,
    input_validation_services,
    otp_services,
    qr_services,
)
from otp_cli_utils.services.error_handling import handle_invalid_input
from otp_cli_utils.utils import msg_utils

app = typer.Typer(
    name="otp-cli-utils",
    help=help_texts.MAIN,
)


@app.command(command_texts.GET_OTP, help=help_texts.GET_OTP)
@handle_invalid_input
def get_otp(secret: str = typer.Argument(help=help_texts.SECRET_ARG)):
    """
    Get the current OTP code for the given secret

    Args:
        secret: The base32 encoded secret key for OTP generation
    """
    input_validation_services.validate_input_secret(secret)
    otp = otp_services.get_otp(secret)
    msg_utils.print_success_msg(f"Current OTP: {otp}")


@app.command(command_texts.VALIDATE, help=help_texts.VALIDATE)
@handle_invalid_input
def validate(
    secret: str = typer.Argument(help=help_texts.SECRET_ARG),
    otp: str = typer.Argument(help=help_texts.OTP_ARG),
    window_count: int | None = typer.Option(
        None,
        "--window-count",
        "-w",
        help=help_texts.WINDOW_COUNT_ARG,
    ),
    valid_time_period: int | None = typer.Option(
        None, "--time-period", "-t", help=help_texts.VALID_TIME_PERIOD_ARG
    ),
):
    """
    Validate if the provided OTP matches the expected value for the given secret

    Args:
        secret: The base32 encoded secret key for OTP validation
        otp: The OTP code to validate
        window_count: Number of time steps to validate against (mutually exclusive with valid_time_period)
        valid_time_period: Time period in seconds to validate against (mutually exclusive with window_count)
    """
    input_validation_services.validate_input_secret(secret)
    input_validation_services.validate_input_otp_code(otp)

    if window_count is not None and valid_time_period is not None:
        raise InvalidInputError(error_texts.BOTH_WINDOW_COUNT_AND_TIME_PERIOD_TEXT)

    if valid_time_period is not None:
        input_validation_services.validate_input_time_period(valid_time_period)
        window_count = otp_services.get_windows_for_time_period(valid_time_period)

    window_count = window_count or 0
    input_validation_services.validate_input_window_count(window_count)

    if otp_services.validate_otp(secret, otp, window_count):
        msg_utils.print_success_msg(error_texts.VALID_OTP_TEXT)
    else:
        msg_utils.print_error_msg(error_texts.INVALID_OTP_TEXT)
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
    """Generate a Google Authenticator Compatible QR code with a new OTP secret

    Args:
        label: Label for the OTP account (usually email or username)
        issuer: Issuer name (usually the service name)
        file_name: Base filename for the generated QR code image
    """
    secret = otp_services.generate_otp_secret()
    uri = otp_services.generate_uri(secret, label.strip(), issuer.strip())
    img = qr_services.generate_qr_code(uri)
    saved_file_path = img_services.save_image(img, file_name)

    msg_utils.print_success_msg(
        f"Generated OTP secret: {secret}\n\n"
        f"OTP secret QR code saved to: {saved_file_path}"
    )


def main():
    app()


if __name__ == "__main__":
    main()
