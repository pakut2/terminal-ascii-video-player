from PIL import Image
from os import listdir
from time import time, sleep

CHARACTERS = ["@", "&", "$", "#", "%", "?", "+", ";", ":", ",", "."]
BRIGHTNESS_TO_ASCII_SCALE = 255 // (len(CHARACTERS) - 1)
FPS = 24


def resize_frame(frame: Image, resized_image_width: int) -> Image:
    original_width, original_height = frame.size
    resize_ratio = original_height / original_width / 2
    resized_image_height = int(resized_image_width * resize_ratio)

    return frame.resize((resized_image_width, resized_image_height))


def frame_to_ascii_string(frame: Image) -> str:
    pixels = frame.getdata()

    return "".join([CHARACTERS[pixel//BRIGHTNESS_TO_ASCII_SCALE] for pixel in pixels])


def convert_frame(frame: Image, frame_width=100) -> str:
    resized_frame = resize_frame(frame, frame_width)
    grayscaled_frame = resized_frame.convert("L")
    ascii_frame_stringified = frame_to_ascii_string(grayscaled_frame)
    return "\n".join([ascii_frame_stringified[i:(i+frame_width)]
                      for i in range(0, len(ascii_frame_stringified), frame_width)])


def print_image(image_width=300) -> None:
    with Image.open("./shrek.jpeg") as image:
        ascii_image = convert_frame(image, image_width)
        print(ascii_image)


def main(frame_width=100) -> None:
    frame_duration = 1 / FPS

    for i in range(1, len(listdir("./frames")) - 1):
        frame_start = time()

        with Image.open(f"./frames/frame{i}.png") as frame:
            ascii_frame = convert_frame(frame, frame_width)
            print(ascii_frame)

        frame_end = time()
        frame_delay = frame_duration - (frame_end - frame_start)
        if (frame_delay > 0):
            sleep(frame_delay)


main()
