from qrcode.image.pil import PilImage


def save_image(img: PilImage, name: str) -> None:
    """
    Save an image to a png file
    """
    img.save(f"{name}.png")
