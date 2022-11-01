import cv2 as cv

CHARACTERS = ["@", "&", "$", "#", "%", "?", "+", ";", ":", ",", "."]


def resize_image(image: cv.Mat, resized_image_width: int) -> cv.Mat:
    (original_height, original_width) = image.shape
    resize_ratio = original_width / original_height / 2
    resized_image_height = int(resized_image_width * resize_ratio)

    return cv.resize(image, (resized_image_width, resized_image_height))


def image_to_ascii_string(image: cv.Mat) -> str:
    pixels = image.flatten()

    return "".join([CHARACTERS[pixel//25] for pixel in pixels])


def main(image_width=100) -> None:
    for i in range(1, 6573):
        image = cv.imread(f"./frames/frame{i}.png", cv.IMREAD_GRAYSCALE)

        resized_image = resize_image(image, image_width)
        ascii_image_stringified = image_to_ascii_string(resized_image)
        ascii_image = "\n".join([ascii_image_stringified[i:(i+image_width)]
                                for i in range(0, len(ascii_image_stringified), image_width)])

        print(ascii_image)


main()
