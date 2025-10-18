import base64
import binascii
import string

from otp_cli_utils.constants import error_texts
from otp_cli_utils.errors.invalid_input_error import InvalidInputError


def validate_input_secret(secret: str) -> None:
    """
    Validate if the secret is a valid base32 string

    Args:
        secret: The secret key to validate

    Raises:
        InvalidInputError: If the secret is not a valid base32 string
    """
    # convert to uppercase
    secret_upper = secret.upper()

    # ensure the length is a multiple of 8
    if len(secret) % 8 != 0:
        raise InvalidInputError(error_texts.INVALID_SECRET_LENGTH_TEXT)

    # check if the secret only has A-Z, 2-7, and =
    valid_charaters_str = string.ascii_uppercase + string.octdigits + "="
    valid_charaters_set = set(valid_charaters_str)
    valid_charaters_set.remove("0")
    valid_charaters_set.remove("1")
    secret_upper_set = set(secret_upper)
    if not secret_upper_set.issubset(valid_charaters_set):
        raise InvalidInputError(error_texts.INVALID_SECRET_CHARACTERS_TEXT)

    # try to decode to verify it's valid base32
    try:
        base64.b32decode(secret_upper)
    except binascii.Error:
        raise InvalidInputError(error_texts.INVALID_SECRET_BASE32_TEXT)


def validate_input_otp_code(otp: str) -> None:
    """
    Validate if the OTP code is a 6-digit number

    Args:
        otp: The OTP code to validate

    Raises:
        InvalidInputError: If the OTP is not a 6-digit number
    """
    if not otp.isdigit() or len(otp) != 6:
        raise InvalidInputError(error_texts.INVALID_OTP_FORMAT_TEXT)


def validate_input_window_count(window_count: int) -> None:
    """
    Validate the window count parameter

    Args:
        window_count: The window count to validate

    Raises:
        InvalidInputError: If window_count is less than 0 or not an integer
    """
    if not isinstance(window_count, int):
        raise InvalidInputError(error_texts.INVALID_WINDOW_COUNT_TYPE_TEXT)
    elif window_count < 0:
        raise InvalidInputError(error_texts.INVALID_WINDOW_COUNT_RANGE_TEXT)


def validate_input_time_period(time_period: int) -> None:
    """
    Validate the time period parameter

    Args:
        time_period: The time period in seconds to validate

    Raises:
        InvalidInputError: If time_period is not a multiple of 30, less than 30, or not an integer
    """
    if not isinstance(time_period, int):
        raise InvalidInputError(error_texts.INVALID_TIME_PERIOD_TYPE_TEXT)
    elif time_period < 30:
        raise InvalidInputError(error_texts.INVALID_TIME_PERIOD_RANGE_TEXT)
    elif time_period % 30 != 0:
        raise InvalidInputError(error_texts.INVALID_TIME_PERIOD_MULTIPLE_TEXT)
