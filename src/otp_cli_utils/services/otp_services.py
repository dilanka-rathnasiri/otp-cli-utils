from datetime import datetime, timedelta
from typing import List

import pyotp
from pyotp import TOTP


def get_otp(secret: str) -> str:
    """
    Generate the current OTP code for the given secret

    Args:
        secret (str): The secret key used to generate the OTP

    Returns:
        str: The current OTP code as a string
    """
    totp = TOTP(secret.upper())
    return totp.now()


def get_otp_times_for_window_count(window_count: int) -> List[datetime]:
    """
    Get a list of past datetime objects corresponding with the given window count

    The list will contain the current time and the previous window_count number of 30s time windows

    Args:
        window_count (int): The number of past 30s time windows to consider

    Returns:
        List[datetime]: A list of datetime objects representing the past window_count number of 30s time windows
    """
    now = datetime.now()
    return [now - timedelta(seconds=30 * i) for i in range(window_count + 1)]


def get_windows_for_time_period(time_period: int) -> int:
    """
    Calculate the number of past 30s time windows for the given valid time period

    Args:
        time_period (int): The time period in seconds

    Returns:
        int: The number of 30s time windows
    """
    return time_period // 30 - 1


def validate_otp_at(totp: TOTP, otp_code: str, otp_at: datetime) -> bool:
    return totp.verify(otp_code, otp_at)


def validate_otp(secret: str, otp_code: str, window_count: int) -> bool:
    """
    Validate an OTP code against a secret key

    Args:
        secret (str): The secret key to validate against
        otp_code (str): The OTP code to validate
        window_count (int): The number of past 30s time window count to consider

    Returns:
        bool: True if the OTP code is valid, False otherwise
    """
    totp = TOTP(secret.upper())

    otp_times = get_otp_times_for_window_count(window_count)

    for otp_time in otp_times:
        if totp.verify(otp_code, otp_time):
            return True

    return False


def generate_otp_secret() -> str:
    """
    Generate a new random OTP secret key

    Returns:
        str: A base32-encoded random secret key
    """
    return pyotp.random_base32()


def generate_uri(secret: str, label: str, issuer: str) -> str:
    """
    Generate a Google Authenticator URI
    More info: https://github.com/google/google-authenticator/wiki/Key-Uri-Format

    Args:
        secret (str): The OTP secret key
        label (str): Account name
        issuer (str): Service or provider name

    Returns:
        str: A URI string compatible with Google Authenticator
    """
    return f"otpauth://totp/{label}?secret={secret}&issuer={issuer}"
