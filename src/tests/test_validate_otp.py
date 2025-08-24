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

    assert otp_services.validate_otp(current_otp_code, otp_secret) is True


def test_validate_invalid_otp(otp_secret):
    """
    Test the validate_otp function with an invalid OTP
    """
    current_otp_code = "1234567"

    assert otp_services.validate_otp(current_otp_code, otp_secret) is False
