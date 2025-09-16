from datetime import datetime, timedelta

import pytest
from pyotp import TOTP

from otp_cli_utils.services import otp_services


@pytest.fixture
def otp_secret():
    return "6IHWNRO2TB4OBGLPXDCU666C42GYUDON"


@pytest.fixture
def totp_instance(otp_secret):
    return TOTP(otp_secret)


def test_validate_valid_otp(otp_secret, totp_instance):
    """
    Test the validate_otp function with a valid OTP
    """
    current_otp_code = totp_instance.now()

    assert otp_services.validate_otp(otp_secret, current_otp_code, 0) is True


def test_validate_invalid_otp(otp_secret):
    """
    Test the validate_otp function with an invalid OTP
    """
    current_otp_code = "1234567"

    assert otp_services.validate_otp(otp_secret, current_otp_code, 0) is False


def test_validate_otp_with_window_count_one_invalid_previous_otp(otp_secret):
    """
    Test the validate_otp function with a window count of 2 and an invalid OTP from the previous window
    """
    invalid_otp_code = "1234567"

    assert otp_services.validate_otp(otp_secret, invalid_otp_code, 2) is False


def test_validate_otp_with_window_count_two_valid_previous_otp(
    otp_secret, totp_instance
):
    """
    Test the validate_otp function with a window count of 2 and a valid OTP from two windows ago
    """
    previous_otp_code = totp_instance.at(datetime.now() - timedelta(seconds=60))

    assert otp_services.validate_otp(otp_secret, previous_otp_code, 2) is True


def test_validate_otp_with_window_count_one_valid_two_windows_ago_otp(
    otp_secret, totp_instance
):
    """
    Test the validate_otp function with a window count of 1 and a valid OTP from two windows ago
    """
    previous_otp_code = totp_instance.at(datetime.now() - timedelta(seconds=60))

    assert otp_services.validate_otp(otp_secret, previous_otp_code, 1) is False
