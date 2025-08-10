# OTP CLI Utils

A command-line utility for working with TOTP (Time-based One-Time Password) codes

## Installation

Install the package using pip:

```bash
pip install otp-cli-utils
```

## Usage

### Get Current OTP Code

Get the current OTP code for a given secret:

```bash
otp-utils get-otp <secret>
```

Example:
```bash
otp-utils get-otp ABCDEF123456
```

### Validate an OTP

Validate if an OTP code matches the expected value for a given secret:

```bash
otp-utils validate <otp> <secret>
```

Example:
```bash
otp-utils validate 123456 ABCDEF123456
```

### Exit Codes
- `0`: Command executed successfully
- `1`: Invalid OTP (for validate command) or error occurred
