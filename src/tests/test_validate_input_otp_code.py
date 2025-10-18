import pytest

from otp_cli_utils.constants import error_texts
from otp_cli_utils.errors.invalid_input_error import InvalidInputError
from otp_cli_utils.services.input_validation_services import validate_input_otp_code


def test_validate_input_otp_code_valid():
    """
    Test validate_input_otp_code with a valid 6-digit OTP
    """
    valid_otp = "123456"
    assert validate_input_otp_code(valid_otp) is None


def test_validate_input_otp_code_invalid_length():
    """
    Test validate_input_otp_code with an OTP of invalid length
    """
    invalid_otp = "12345"
    with pytest.raises(InvalidInputError, match=error_texts.INVALID_OTP_FORMAT_TEXT):
        validate_input_otp_code(invalid_otp)


def test_validate_input_otp_code_not_a_digit():
    """
    Test validate_input_otp_code with an OTP containing non-digit characters
    """
    invalid_otp = "123a56"
    with pytest.raises(InvalidInputError, match=error_texts.INVALID_OTP_FORMAT_TEXT):
        validate_input_otp_code(invalid_otp)
