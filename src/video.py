from PIL import Image
import os
import time
from process_frame import convert_frame

FPS = 24


def play_video(horizontal_resolution=100) -> None:
    frame_duration = 1 / FPS

    for i in range(1, len(os.listdir("./frames"))):
        frame_start = time.perf_counter()

        with Image.open(f"./frames/frame{i}.png") as frame:
            ascii_frame = convert_frame(frame, horizontal_resolution)
            print(ascii_frame)

        frame_end = time.perf_counter()
        frame_elapsed = frame_end - frame_start
        frame_delay = frame_duration - frame_elapsed

        if (frame_delay > 0):
            time.sleep(frame_delay)


play_video()
