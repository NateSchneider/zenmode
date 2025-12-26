#!/usr/bin/env python3
import evdev
import subprocess
import random

# IR input device
device = evdev.InputDevice('/dev/input/event3')
print(f"Listening for IR on {device.name}")
print("Press red button to trigger zen mode...")

# Video directory
video_dir = "/home/schneiderpi/zenmode/videos"
#videos = [f"{video_dir}/video{i}.mp4" for i in range(1, 7)]

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_MSC and event.value == 0x472:
        #video = random.choice(videos)
        video = "/home/schneiderpi/zenmode/videos/video3.mp4"
        print(f"Red button pressed! Playing {video}...")
        subprocess.Popen(['vlc', '--fullscreen', '--loop', video])

