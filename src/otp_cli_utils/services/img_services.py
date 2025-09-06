from pathlib import Path

from qrcode.image.pil import PilImage


def save_image(img: PilImage, name: str) -> str:
    """
    Save an image to a png file

    Args:
        img (PIL.Image): The PIL Image object to be saved
        name (str): The base name for the output file (without extension)

    Returns:
        str: The absolute path of the saved PNG file
    """
    file_name = f"{name}.png"
    img.save(file_name)
    return f"{Path.cwd()}/{file_name}"
