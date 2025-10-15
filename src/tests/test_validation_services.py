import pytest

from otp_cli_utils.constants import error_texts
from otp_cli_utils.errors.invalid_input_error import InvalidInputError
from otp_cli_utils.services import validation_services


# Tests for validate_secret
def test_validate_secret_valid():
    """
    Test validate_secret with a valid base32 secret
    """
    valid_secret = "MFRGGZDFMZTWQ2LK"
    assert validation_services.validate_secret(valid_secret) is None


def test_validate_secret_invalid_length():
    """
    Test validate_secret with a secret of invalid length
    """
    invalid_secret = "MFRGGZDFMZTWQ2L"
    with pytest.raises(InvalidInputError, match=error_texts.INVALID_SECRET_LENGTH_TEXT):
        validation_services.validate_secret(invalid_secret)


def test_validate_secret_invalid_characters():
    """
    Test validate_secret with a secret containing invalid characters
    """
    invalid_secret = "MFRGGZDFMZTWQ2L1"  # Contains '1'
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_SECRET_CHARACTERS_TEXT
    ):
        validation_services.validate_secret(invalid_secret)


def test_validate_secret_invalid_base32_padding():
    """
    Test validate_secret with a string that has invalid base32 padding
    """
    invalid_secret = "MFRGGZDFMZT====="
    with pytest.raises(InvalidInputError, match=error_texts.INVALID_SECRET_BASE32_TEXT):
        validation_services.validate_secret(invalid_secret)


# Tests for validate_otp_code
def test_validate_otp_code_valid():
    """
    Test validate_otp_code with a valid 6-digit OTP
    """
    valid_otp = "123456"
    assert validation_services.validate_otp_code(valid_otp) is None


def test_validate_otp_code_invalid_length():
    """
    Test validate_otp_code with an OTP of invalid length
    """
    invalid_otp = "12345"
    with pytest.raises(InvalidInputError, match=error_texts.INVALID_OTP_FORMAT_TEXT):
        validation_services.validate_otp_code(invalid_otp)


def test_validate_otp_code_not_a_digit():
    """
    Test validate_otp_code with an OTP containing non-digit characters
    """
    invalid_otp = "123a56"
    with pytest.raises(InvalidInputError, match=error_texts.INVALID_OTP_FORMAT_TEXT):
        validation_services.validate_otp_code(invalid_otp)


# Tests for validate_window_count
def test_validate_window_count_valid():
    """
    Test validate_window_count with valid counts (0 and a positive integer)
    """
    assert validation_services.validate_window_count(0) is None
    assert validation_services.validate_window_count(10) is None


def test_validate_window_count_invalid_type():
    """
    Test validate_window_count with a non-integer value
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_WINDOW_COUNT_TYPE_TEXT
    ):
        validation_services.validate_window_count("5")


def test_validate_window_count_negative():
    """
    Test validate_window_count with a negative integer
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_WINDOW_COUNT_RANGE_TEXT
    ):
        validation_services.validate_window_count(-1)


# Tests for validate_time_period
def test_validate_time_period_valid():
    """
    Test validate_time_period with valid time periods
    """
    assert validation_services.validate_time_period(30) is None
    assert validation_services.validate_time_period(60) is None
    assert validation_services.validate_time_period(90) is None


def test_validate_time_period_invalid_type():
    """
    Test validate_time_period with a non-integer value
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_TIME_PERIOD_TYPE_TEXT
    ):
        validation_services.validate_time_period("60")


def test_validate_time_period_less_than_30():
    """
    Test validate_time_period with a value less than 30
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_TIME_PERIOD_RANGE_TEXT
    ):
        validation_services.validate_time_period(29)


def test_validate_time_period_not_a_multiple_of_30():
    """
    Test validate_time_period with a value that is not a multiple of 30
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_TIME_PERIOD_MULTIPLE_TEXT
    ):
        validation_services.validate_time_period(31)
