import numpy as np

def ft_invert(array) -> np.ndarray:
    """Inverts the colors: 255 - pixel_value"""
    return 255 - array

def ft_red(array) -> np.ndarray:
    """Keeps red removes blue and green"""
    array_copy = array.copy()
    array_copy[:, :, 1] = array_copy[:, :, 1] * 0
    array_copy[:, :, 2] = array_copy[:, :, 2] * 0
    return array_copy

def ft_green(array) -> np.ndarray:
    """Keeps green removes red and blue"""
    array_copy = array.copy()
    array_copy[:, :, 0] = array_copy[:, :, 0] - array_copy[:, :, 0]
    array_copy[:, :, 2] = array_copy[:, :, 2] - array_copy[:, :, 2]
    return array_copy

def ft_blue(array) -> np.ndarray:
    """Keeps blue removes red and green"""
    array_copy = array.copy()
    array_copy[:, :, 0] = 0
    array_copy[:, :, 1] = 0
    return array_copy

def ft_grey(array) -> np.ndarray:
    """Sum the channels and divide by 3 and reconstruct the image."""
    avg = (array[:, :, 0] / 3) + (array[:, :, 1] / 3) + (array[:, :, 2] / 3)
    return np.stack((avg, avg, avg), axis=2).astype(np.uint8)