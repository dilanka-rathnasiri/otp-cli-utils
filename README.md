# OTP CLI Utils

A simple command-line utility for validating TOTP (Time-based One-Time Password) codes

## Installation

Install the package using pip:

```bash
pip install otp-cli-utils
```

## Usage

### Validate an OTP

```bash
otp-utils {{otp}} {{secret}}
```

Example:
```bash
otp-utils 123456 ABCDEF123456
```

### Exit Codes
- `0`: OTP is valid
- `1`: OTP is invalid
