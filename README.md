# Pixelate

This script pixelates an image using a colour palette of a given size.

# Installation
To run the script, first install its dependencies:

`pip3 install opencv-python numpy`

# Usage
The pixelate script syntax is as follows:
`python3 pixelate.py input_path output_path`

For optional usage and additional parameters, use:
`python3 pixelate.py --help`

# Examples
The `examples` folder shows a couple of example pictures pre and post pixelization.
Here are some examples:

![Mountain lake](examples/lake.jpg)

Pixelated with `b = 8` and `c = 64`.

![Pixelated mountain lake with b = 8 and c = 64](examples/lake_pixelated_b8_c64.png)

Pixelated with `b = 4` and `c = 8`.

![Pixelated mountain lake with b = 4 and c = 8](examples/lake_pixelated_b4_c8.png)

With `b = 1`, the script essentially reduces the image to a smaller color palette, creating some cool effects.

With `c = 4`.

![Pixelated mountain lake with b = 1 and c = 4](examples/lake_pixelated_b1_c4.png)

With `c = 2`.

![Pixelated mountain lake with b = 1 and c = 2](examples/lake_pixelated_b1_c2.png)
