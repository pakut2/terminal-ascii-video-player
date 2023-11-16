from PIL import Image
import argparse
from image_processor import image_to_ascii_string

parser = argparse.ArgumentParser(description="Display ASCII image")
parser.add_argument("--image", dest="image_path", type=str, required=True,
                    help="Path to source image")
parser.add_argument("--hres", type=int, default=100,
                    help="Image horizontal resolution in pixels")

args = parser.parse_args()


def print_image(horizontal_resolution: int) -> None:
    with Image.open(args.image_path) as image:
        ascii_image = image_to_ascii_string(image, horizontal_resolution)
        print(ascii_image)


print_image(abs(args.hres))
