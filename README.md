# OTP CLI Utils

A command-line utility for working with TOTP (Time-based One-Time Password) codes. This tool helps you generate, validate, and manage OTP secrets with ease.

## Features

- 🔑 Generate current TOTP codes from a secret
- ✅ Validate OTP codes against a secret
- 🔄 Generate secure random OTP secrets
- 📱 Create Google Authenticator compatible QR codes
- 🛠️ Simple and intuitive command-line interface

## Installation

Install the package using pip:

```bash
pip install otp-cli-utils
```

## Usage

### Get Current OTP Code

Get the current OTP code for a given secret:

```bash
otp-cli-utils get-otp <secret>
```

Example:

```bash
otp-cli-utils get-otp ABCDEF1234567890
```

### Validate an OTP

Validate if an OTP code matches the expected value for a given secret:

```bash
otp-cli-utils validate <secret> <otp> [--window-count <count> | --time-period <seconds>]
```

Options (mutually exclusive - use only one):
- `--window-count`, `-w`: Number of time steps to validate against (default: 0)
- `--time-period`, `-t`: Time period in seconds to validate against (must be ≥30 and a multiple of 30)

Examples:

- Basic validation (checks current time step only):

```bash
otp-cli-utils validate ABCDEF1234567890 123456
```

- With window count (checks current and previous N time steps):

```bash
otp-cli-utils validate ABCDEF1234567890 123456 --window-count 2
```

- With custom time period (in seconds, must be multiple of 30):

```bash
otp-cli-utils validate ABCDEF1234567890 123456 --time-period 120
```

### Generate a New OTP Secret

Generate a new secure random secret key for OTP generation:

```bash
otp-cli-utils generate-secret
```

### Generate QR Code for Authenticator Apps

- Generate a QR code that can be scanned by Google Authenticator or similar apps
- QR code will be generated with a new secure random secret key
- Generated QR code will be saved as a png image file

```bash
otp-cli-utils generate-secret-qr-code <label> <issuer> [filename]
```

Arguments:
- `label`: Account name (e.g., user@example.com)
- `issuer`: Service or provider name (e.g., GitHub)
- `filename`: (Optional) Output filename without extension (default: otp_secret_qr)

Example:

```bash
otp-cli-utils generate-secret-qr-code "user@example.com" "GitHub" github_2fa
```

## Exit Codes

- `0`: Command executed successfully
- `1`: Invalid OTP (for validate command) or error occurred

## Input Validation

The tool performs the following validations on the inputs:

- **OTP Secret**:
  - Must be a valid Base32 encoded string.
  - The length of the secret must be a multiple of 8.
  - It can only contain uppercase letters (`A-Z`), digits from `2` to `7`, and the padding character (`=`).

- **OTP Code**:
  - Must be a 6-digit number.

- **Window Count (`--window-count`, `-w`)**:
  - Must be an integer.
  - Must be a non-negative number (0 or greater).

- **Time Period (`--time-period`, `-t`)**:
  - Must be an integer.
  - Must be 30 seconds or greater.
  - Must be a multiple of 30.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
