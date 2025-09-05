import qrcode
from qrcode.image.pil import PilImage


def generate_qr_code(data: str) -> PilImage:
    """
    Generate a QR code image from the given string data

    Args:
        data (str): The data to encode in the QR code

    Returns:
        PilImage: A PIL Image object containing the QR code
    """
    return qrcode.make(data, image_factory=PilImage)
