import base64
import binascii
import re
import string

from otp_cli_utils.constants import error_texts
from otp_cli_utils.errors.invalid_input_error import InvalidInputError


def validate_secret(secret: str) -> None:
    """
    Validate if the secret is a valid base32 string

    Args:
        secret: The secret key to validate

    Raises:
        InvalidInputException: If the secret is not a valid base32 string
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
