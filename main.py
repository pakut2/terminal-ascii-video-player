from PIL import Image


ASCII_CHARS = ["@", "&", "#", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image: Image, new_width=100):
    width, height = image.size
    ratio = height / width / 2
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))

    return (resized_image)


def grayify(image: Image):
    return image.convert("L")


def pixels_to_ascii(image: Image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def main(new_width=100):
    with Image.open("./bad-apple.jpg") as image:
        new_image = pixels_to_ascii(grayify(resize_image(image, new_width)))
        pixel_count = len(new_image)
        ascii_image = "\n".join([new_image[index:(index+new_width)]
                                for index in range(0, pixel_count, new_width)])

        print(ascii_image)


main()
