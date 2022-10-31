from PIL import Image


CHARACTERS = ["@", "&", "$", "#", "%", "?", "+", ";", ":", ",", "."]


def resize_image(image: Image, resized_image_width: int) -> Image:
    original_width, original_height = image.size
    resize_ratio = original_height / original_width / 2
    resized_image_height = int(resized_image_width * resize_ratio)

    return image.resize((resized_image_width, resized_image_height))


def image_to_ascii_string(image: Image) -> str:
    pixels = image.getdata()

    return "".join([CHARACTERS[pixel//25] for pixel in pixels])


def main(image_width=100) -> None:
    with Image.open("./bad-apple.jpg") as image:
        resized_image = resize_image(image, image_width)
        grayscaled_image = resized_image.convert("L")
        ascii_image_stringified = image_to_ascii_string(grayscaled_image)
        ascii_image = "\n".join([ascii_image_stringified[i:(i+image_width)]
                                for i in range(0, len(ascii_image_stringified), image_width)])

        print(ascii_image)


main()
