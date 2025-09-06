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


def validate_otp(secret: str, otp_code: str) -> bool:
    """
    Validate an OTP code against a secret key

    Args:
        secret (str): The secret key to validate against
        otp_code (str): The OTP code to validate

    Returns:
        bool: True if the OTP code is valid, False otherwise
    """
    totp = TOTP(secret.upper())
    return totp.verify(otp_code)


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
