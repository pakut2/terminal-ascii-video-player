from PIL import Image
from process_frame import convert_frame


def print_image(horizontal_resolution=300) -> None:
    with Image.open("./shrek.jpeg") as image:
        ascii_image = convert_frame(image, horizontal_resolution)
        print(ascii_image)


print_image()
