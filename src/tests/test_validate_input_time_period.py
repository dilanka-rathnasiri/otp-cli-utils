import pytest

from otp_cli_utils.constants import error_texts
from otp_cli_utils.errors.invalid_input_error import InvalidInputError
from otp_cli_utils.services.input_validation_services import validate_input_time_period


def test_validate_input_time_period_valid():
    """
    Test validate_input_time_period with valid time periods
    """
    assert validate_input_time_period(30) is None
    assert validate_input_time_period(60) is None
    assert validate_input_time_period(90) is None


def test_validate_input_time_period_invalid_type():
    """
    Test validate_input_time_period with a non-integer value
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_TIME_PERIOD_TYPE_TEXT
    ):
        validate_input_time_period("60")  # type: ignore


def test_validate_input_time_period_less_than_30():
    """
    Test validate_input_time_period with a value less than 30
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_TIME_PERIOD_RANGE_TEXT
    ):
        validate_input_time_period(29)


def test_validate_input_time_period_not_a_multiple_of_30():
    """
    Test validate_input_time_period with a value that is not a multiple of 30
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_TIME_PERIOD_MULTIPLE_TEXT
    ):
        validate_input_time_period(31)
