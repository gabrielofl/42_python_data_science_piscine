import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """Loads an image, prints its shape, and returns it as an RGB array."""

    if not os.path.exists(path):
        raise FileNotFoundError(f"The file '{path}' does not exist.")

    ext = os.path.splitext(path)[1].lower()
    if ext not in ['.jpg', '.jpeg']:
        raise ValueError("JPG/JPEG only allowed.")

    try:
        img = Image.open(path)
        img_rgb = img.convert("RGB")

        img_array = np.array(img_rgb)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the image: {e}")
