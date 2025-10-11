import functools
import sys

from otp_cli_utils.errors.invalid_input_error import InvalidInputError
from otp_cli_utils.utils import msg_utils


def handle_invalid_input(func):
    """
    A decorator that catches InvalidInputError and handles it
    by printing the error message and exiting with status code 1
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidInputError as e:
            msg_utils.print_error_msg(f"Invalid input: {str(e)}")
            sys.exit(1)

    return wrapper
