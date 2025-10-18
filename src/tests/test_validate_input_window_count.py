import pytest

from otp_cli_utils.constants import error_texts
from otp_cli_utils.errors.invalid_input_error import InvalidInputError
from otp_cli_utils.services.input_validation_services import validate_input_window_count


def test_validate_input_window_count_valid():
    """
    Test validate_input_window_count with valid counts (0 and a positive integer)
    """
    assert validate_input_window_count(0) is None
    assert validate_input_window_count(10) is None


def test_validate_input_window_count_invalid_type():
    """
    Test validate_input_window_count with a non-integer value
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_WINDOW_COUNT_TYPE_TEXT
    ):
        validate_input_window_count("5")  # type: ignore


def test_validate_input_window_count_negative():
    """
    Test validate_input_window_count with a negative integer
    """
    with pytest.raises(
        InvalidInputError, match=error_texts.INVALID_WINDOW_COUNT_RANGE_TEXT
    ):
        validate_input_window_count(-1)
