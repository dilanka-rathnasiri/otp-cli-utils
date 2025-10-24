# otp validation error texts
VALID_OTP_TEXT = "Valid OTP"
INVALID_OTP_TEXT = "Invalid OTP"
INVALID_OTP_FORMAT_TEXT = "OTP must be a 6-digit number"

# input secret validation error texts
INVALID_SECRET_LENGTH_TEXT = "Secret length should be multiple of 8"
INVALID_SECRET_CHARACTERS_TEXT = "Secret should only contain A-Z, 2-7, and ="
INVALID_SECRET_BASE32_TEXT = "Secret should be a valid base32 string"

# window count validation error texts
INVALID_WINDOW_COUNT_TYPE_TEXT = "Window count must be an integer"
INVALID_WINDOW_COUNT_RANGE_TEXT = "Window count must be greater than or equal to 0"

# time period validation error texts
INVALID_TIME_PERIOD_TYPE_TEXT = "Time period must be an integer"
INVALID_TIME_PERIOD_RANGE_TEXT = (
    "Time period must be greater than or equal to 30 seconds"
)
INVALID_TIME_PERIOD_MULTIPLE_TEXT = "Time period must be a multiple of 30 seconds"

# validate command error texts
BOTH_WINDOW_COUNT_AND_TIME_PERIOD_TEXT = (
    "Only one option from window count or valid time period can be provided"
)

# generate ecret qr code
INVALID_LABEL_TEXT = "Label can't be empty"
INVALID_ISSUER_TEXT = "Issuer can't be empty"
