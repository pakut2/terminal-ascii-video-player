from PIL import Image
import argparse
from process_frame import convert_frame

parser = argparse.ArgumentParser(description="Display ASCII image")
parser.add_argument("--image", dest="image_dir", type=str, required=True,
                    help="Path to source image")
parser.add_argument("--hres", type=int, default=100,
                    help="Image horizontal resolution in pixels")

args = parser.parse_args()


def print_image(horizontal_resolution: int) -> None:
    with Image.open(args.image_dir) as image:
        ascii_image = convert_frame(image, horizontal_resolution)
        print(ascii_image)


print_image(abs(args.hres))
