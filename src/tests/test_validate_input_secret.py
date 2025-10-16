import pytest

from otp_cli_utils.constants import error_texts
from otp_cli_utils.errors.invalid_input_error import InvalidInputError
from otp_cli_utils.services.input_validation_services import validate_input_secret


def test_validate_input_secret_valid():
    """
    Test validate_input_secret with a valid base32 secret
    """
    valid_secret = "MFRGGZDFMZTWQ2LK"
    assert validate_input_secret(valid_secret) is None


def test_validate_input_secret_invalid_length():
    """
    Test validate_input_secret with a secret of invalid length
    """
    invalid_secret = "MFRGGZDFMZTWQ2L"
    with pytest.raises(InvalidInputError, match=error_texts.INVALID_SECRET_LENGTH_TEXT):
        validate_input_secret(invalid_secret)


def test_validate_input_secret_invalid_characters():
    """
    Test validate_input_secret with a secret containing invalid characters
    """
    invalid_secret = "MFRGGZDFMZTWQ2L1"  # Contains '1'
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_SECRET_CHARACTERS_TEXT
    ):
        validate_input_secret(invalid_secret)


def test_validate_input_secret_invalid_base32_padding():
    """
    Test validate_input_secret with a string that has invalid base32 padding
    """
    invalid_secret = "MFRGGZDFMZT====="
    with pytest.raises(InvalidInputError, match=error_texts.INVALID_SECRET_BASE32_TEXT):
        validate_input_secret(invalid_secret)
