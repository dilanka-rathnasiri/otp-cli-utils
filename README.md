# OTP CLI Utils

A command-line utility for working with TOTP (Time-based One-Time Password) codes

## Features

- Generate current OTP codes from a secret
- Validate OTP codes against a secret
- Generate secure random OTP secrets


## Installation

Install the package using pip:

```bash
pip install otp-cli-utils
```

## Usage

### Get Current OTP Code

Get the current OTP code for a given secret:

```bash
otp-cli-utils get-otp {{secret}}
```

Example:
```bash
otp-cli-utils get-otp ABCDEF1234567890
```

### Validate an OTP

Validate if an OTP code matches the expected value for a given secret


```bash
otp-cli-utils validate {{otp}} {{secret}}
```

Example:
```bash
otp-cli-utils validate 123456 ABCDEF1234567890
```

### Generate a New OTP Secret

Generate a new secure random secret key for OTP generation

```bash
otp-cli-utils generate-secret
```

## Exit Codes

- `0`: Command executed successfully
- `1`: Invalid OTP (for validate command) or error occurred

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
