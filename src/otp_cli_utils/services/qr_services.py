import qrcode
from qrcode.image.pil import PilImage


def generate_qr_code(data: str) -> PilImage:
    """
    Generate a QR code for the given string data
    """
    return qrcode.make(data, image_factory=PilImage)
