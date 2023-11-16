from PIL import Image
import argparse
import os
import time
import curses
from image_processor import image_to_ascii_string

parser = argparse.ArgumentParser(description="Display ASCII video")
parser.add_argument("--hres", type=int, default=100,
                    help="Video horizontal resolution in pixels")

args = parser.parse_args()
FPS = 24


def play_video(horizontal_resolution: int) -> None:
    screen = curses.initscr()
    frame_duration = 1 / FPS

    for i in range(1, len(os.listdir("./frames"))):
        frame_start = time.perf_counter()

        with Image.open(f"./frames/frame{i}.png") as frame:
            ascii_frame = image_to_ascii_string(frame, horizontal_resolution)

            screen.addstr(0, 0, ascii_frame)
            screen.refresh()

        frame_end = time.perf_counter()
        frame_elapsed = frame_end - frame_start
        frame_delay = frame_duration - frame_elapsed

        if (frame_delay > 0):
            time.sleep(frame_delay)


try:
    play_video(abs(args.hres))
finally:
    curses.endwin()