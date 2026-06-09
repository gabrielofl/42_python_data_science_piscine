import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def rotate_image(path: str):
    """Rotates the image by transposing by T"""
    try:
        img = ft_load(path)
        square = img[0:400, 0:400]
        if len(square.shape) == 3 and square.shape[2] == 3:
            square = np.dot(square[..., :3], [0.2989, 0.5870, 0.1140])
        print(square)
        rotated = square.T

        print(rotated)

        plt.imshow(rotated, cmap='gray')
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    rotate_image("animal.jpeg")