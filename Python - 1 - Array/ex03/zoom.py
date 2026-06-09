import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def zoom_image(path: str):
    """Increases image view by crop, performs grayscaling"""
    try:
        img = ft_load(path)
        zoomed = img[0:400, 0:400]
        zoomed_gray = np.dot(zoomed[..., :3], [0.2989, 0.5870, 0.1140])
        zoomed_final = zoomed_gray.reshape(400, 400, 1)
        
        print(zoomed_final)

        plt.imshow(zoomed_final.squeeze(), cmap='gray')
        plt.show()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    zoom_image("animal.jpeg")