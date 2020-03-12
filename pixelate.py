from argparse import ArgumentParser
import os

import cv2
import numpy as np


def pixelate(img, num_colors=64, pixel_size=8):
    """Pixelate an image and reduce use a limited palette of colours.

    Parameters:
    - img The image to pixelate as a numpy array.
    - num_colors The number of colors used in the pixelated image.
    - pixel_size The number of pixels to combine into a new pixel.
    """
    # Convert each pixel value to the average color value of the block it's in.
    for x in range(0, img.shape[1], pixel_size):
        for y in range(0, img.shape[0], pixel_size):
            img[y:y+pixel_size, x:x+pixel_size] = np.mean(img[y:y+pixel_size, x:x+pixel_size], axis=(0, 1))
    # Perform k-means clustering to find pixel-colour mapping, using a size k palette.
    z = np.float32(img.reshape((-1, 3)))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, center = cv2.kmeans(z, num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    # Reshape to the original size and type.
    center = np.uint8(center)
    flat_pixelated_img = center[labels.flatten()]
    pixelated_img = flat_pixelated_img.reshape(img.shape)
    return pixelated_img


def cli():
    """Provide a CLI to the pixelate function."""
    parser = ArgumentParser(description='Pixelate an image with a limited colour palette.')
    parser.add_argument('input', help='The path to the input image')
    parser.add_argument('output', help='The path to the output image')
    parser.add_argument('-b', '--block-size', default=8, help='Pixel block size', type=int)
    parser.add_argument('-c', '--colours', default=64, help='Number of colours to use in the palette', type=int)
    args = parser.parse_args()
    if not os.path.exists(args.input):
        raise FileNotFoundError(f'Input file "{args.input}" could not be found.')
    return args


if __name__ == '__main__':
    args = cli()
    img = cv2.imread(args.input)
    pixelated_img = pixelate(img, args.colours, args.block_size)
    cv2.imwrite(args.output, pixelated_img)
