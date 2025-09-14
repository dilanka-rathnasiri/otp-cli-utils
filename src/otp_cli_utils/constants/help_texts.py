# main command help texts
MAIN = "CLI tool for OTP (One-Time Password) generation and validation"

# command help texts
GET_OTP = "Get the current OTP code for the given secret"
VALIDATE = (
    "Validate if the provided OTP matches the expected value for the given secret"
)
GENERATE_SECRET = "Generate a new secure random secret key for OTP generation"
GENERATE_SECRET_QR_CODE = "Generate a Google Authenticator Compatible QR code"

# argument help texts
SECRET_ARG = "OTP secret"
OTP_ARG = "The OTP code to validate"
LABEL_ARG = "Label for the OTP secret"
ISSUER_ARG = "Issuer for the OTP secret"
FILENAME_ARG = "File name for the QR code (without extension)"
WINDOW_COUNT_ARG = (
    "Tokens in the previous 30s time windows that should be considered valid"
)
