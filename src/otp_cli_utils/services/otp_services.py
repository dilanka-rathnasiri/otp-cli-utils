from datetime import datetime, timedelta
from typing import List

import pyotp
from pyotp import TOTP


def get_otp(secret: str) -> str:
    totp = TOTP(secret.upper())
    return totp.now()


def get_otp_times_for_window_count(window_count: int) -> List[datetime]:
    now = datetime.now()
    return [now - timedelta(seconds=30 * i) for i in range(window_count + 1)]


def validate_otp_at(totp: TOTP, secret: str, otp_at: datetime) -> bool:
    return totp.verify(secret, otp_at)


def validate_otp(otp_code: str, secret: str, window_count: int) -> bool:
    totp = TOTP(secret.upper())

    if window_count == 0:
        return validate_otp_at(totp, secret, datetime.now())

    otp_times = get_otp_times_for_window_count(window_count)

    for otp_time in otp_times:
        if totp.verify(otp_code, otp_time):
            return True

    return False


def generate_otp_secret() -> str:
    return pyotp.random_base32()
