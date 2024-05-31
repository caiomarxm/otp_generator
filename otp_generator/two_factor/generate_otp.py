import pyotp

def generate_totp_from_secret(secret: str):
    totp = pyotp.TOTP(secret)
    totp_code = totp.now()
    return totp_code
