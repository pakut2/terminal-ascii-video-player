import cv2 as cv
import os
import time
import sys


CHARACTERS = ["@", "&", "$", "#", "%", "?", "+", ";", ":", ",", "."]
BRIGHTNESS_TO_ASCII_SCALE = 255 // (len(CHARACTERS) - 1)
FPS = 24


def resize_image(image: cv.Mat, resized_image_width: int) -> cv.Mat:
    (original_height, original_width) = image.shape
    resize_ratio = original_height / original_width / 2
    resized_image_height = int(resized_image_width * resize_ratio)

    return cv.resize(image, (resized_image_width, resized_image_height))


def image_to_ascii_string(image: cv.Mat) -> str:
    ascii_image: list[str] = []

    for row in image:
        ascii_string = "".join(
            [CHARACTERS[pixel//BRIGHTNESS_TO_ASCII_SCALE] for pixel in row])
        ascii_string += "\n"
        ascii_image.append(ascii_string)

    return ascii_image

def print_image(image_width = 300)->None:
    image = cv.imread("./crazy.jpg", cv.IMREAD_GRAYSCALE)
    resized_image = resize_image(image, image_width)
    ascii_image_array = image_to_ascii_string(resized_image)
    ascii_image = "".join(ascii_image_array)

    print(ascii_image)


def main(image_width=100) -> None:
    frame_duration = 1 / FPS

    for i in range(1, len(os.listdir("./frames")) - 1):
        frame_start = time.time()
        image = cv.imread(f"./frames/frame{i}.png", cv.IMREAD_GRAYSCALE)

        resized_image = resize_image(image, image_width)
        ascii_image_array = image_to_ascii_string(resized_image)
        ascii_image = "".join(ascii_image_array)

        sys.stdout.write(ascii_image)
        sys.stdout.flush()

        frame_end = time.time()
        frame_delay = frame_duration - (frame_end - frame_start)
        if (frame_delay > 0):
            time.sleep(frame_delay)


print_image()
