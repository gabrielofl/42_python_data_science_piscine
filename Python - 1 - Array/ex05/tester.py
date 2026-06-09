# from load_image import ft_load
# from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red

# array = ft_load("landscape.jpg")
# ft_invert(array)
# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)
# print(ft_invert.__doc__)

import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

def main():
    try:
        # 1. Load the image
        img = ft_load("landscape.jpg")

        # 2. Apply filters
        inverted = ft_invert(img)
        red_only = ft_red(img)
        green_only = ft_green(img)
        blue_only = ft_blue(img)
        grey_scale = ft_grey(img)

        # 3. Display results using subplots
        filters = [img, inverted, red_only, green_only, blue_only, grey_scale]
        titles = ["Original", "Invert", "Red", "Green", "Blue", "Grey"]

        fig, axes = plt.subplots(2, 3, figsize=(12, 8))
        for ax, f, title in zip(axes.flatten(), filters, titles):
            ax.imshow(f.astype(int))
            ax.set_title(title)
            ax.axis('off')
        
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()