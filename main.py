from PIL import Image
import time


CHARACTERS = ["@", "&", "$", "#", "%", "?", "+", ";", ":", ",", "."]
FPS = 30


def resize_frame(frame: Image, resized_image_width: int) -> Image:
    original_width, original_height = frame.size
    resize_ratio = original_height / original_width / 2
    resized_image_height = int(resized_image_width * resize_ratio)
    
    return frame.resize((resized_image_width, resized_image_height))


def frame_to_ascii_string(frame: Image) -> str:
    pixels = frame.getdata()
    return "".join([CHARACTERS[pixel//25] for pixel in pixels])


def convert_frame(frame: Image, frame_width=100) -> str:
    resized_frame = resize_frame(frame, frame_width)
    grayscaled_frame = resized_frame.convert("L")
    ascii_frame_stringified = frame_to_ascii_string(grayscaled_frame)
    return "\n".join([ascii_frame_stringified[i:(i+frame_width)]
                      for i in range(0, len(ascii_frame_stringified), frame_width)])


def main(frame_width=100) -> None:
    second = 1
    frame_duration = second / FPS

    for i in range(1, 6573):
        frame_start = time.time()

        with Image.open(f"./frames/frame{i}.png") as frame:
            ascii_frame = convert_frame(frame, frame_width)
            print(ascii_frame)

        frame_end = time.time()
        frame_delay = frame_duration - (frame_end - frame_start)
        time.sleep(frame_delay)


main()
