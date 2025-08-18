import pyotp
from pyotp import TOTP


def get_otp(secret: str) -> str:
    totp = TOTP(secret.upper())
    return totp.now()


def validate_otp(otp_code: str, secret: str) -> bool:
    totp = TOTP(secret.upper())
    return totp.verify(otp_code)


def generate_otp_secret() -> str:
    return pyotp.random_base32()
