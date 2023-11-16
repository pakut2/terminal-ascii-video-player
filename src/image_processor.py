from PIL import Image

CHARACTERS = ["@", "&", "$", "#", "%", "?", "+", ";", ":", ",", "."]
BRIGHTNESS_TO_ASCII_SCALE = 255 // (len(CHARACTERS) - 1)


def resize_image(image: Image, resized_width: int) -> Image:
    original_width, original_height = image.size
    resize_ratio = original_height / original_width / 2
    resized_height = int(resized_width * resize_ratio)

    return image.resize((resized_width, resized_height)) 


def image_to_ascii_string(image: Image, image_width: int) -> str:
    resized_image = resize_image(image, image_width)
    grayscaled_image = resized_image.convert("L")
    pixels = grayscaled_image.getdata()
    
    ascii_image_stringified = "".join([CHARACTERS[pixel//BRIGHTNESS_TO_ASCII_SCALE] for pixel in pixels])

    return "\n".join([ascii_image_stringified[i:(i+image_width)]
                      for i in range(0, len(ascii_image_stringified), image_width)])
