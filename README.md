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
otp-cli-utils validate <secret> <otp> [--window-count <count>]
```

Options:
- `--window-count`, `-w`: Tokens in the previous 30s time windows that should be considered valid (default: 0)

Example:
- Without window count option
```bash
otp-cli-utils validate ABCDEF1234567890 123456
```

- With window count option
```bash
otp-cli-utils validate ABCDEF1234567890 123456 --window-count 2
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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
