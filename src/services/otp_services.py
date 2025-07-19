from pyotp import TOTP


def validate_otp(otp_code: str, secret: str) -> bool:
    totp = TOTP(secret.upper())
    return totp.verify(otp_code)
