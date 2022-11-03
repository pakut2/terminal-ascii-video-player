from PIL import Image

CHARACTERS = ["@", "&", "$", "#", "%", "?", "+", ";", ":", ",", "."]
BRIGHTNESS_TO_ASCII_SCALE = 255 // (len(CHARACTERS) - 1)


def resize_frame(frame: Image, resized_width: int) -> Image:
    original_width, original_height = frame.size
    resize_ratio = original_height / original_width / 2
    resized_height = int(resized_width * resize_ratio)

    return frame.resize((resized_width, resized_height))


def frame_to_ascii_string(frame: Image) -> str:
    pixels = frame.getdata()

    return "".join([CHARACTERS[pixel//BRIGHTNESS_TO_ASCII_SCALE] for pixel in pixels])


def convert_frame(frame: Image, frame_width: int) -> str:
    resized_frame = resize_frame(frame, frame_width)
    grayscaled_frame = resized_frame.convert("L")
    ascii_frame_stringified = frame_to_ascii_string(grayscaled_frame)

    return "\n".join([ascii_frame_stringified[i:(i+frame_width)]
                      for i in range(0, len(ascii_frame_stringified), frame_width)])
