#!/usr/bin/env python3
"""script to combine audio and
 video files using FFmpeg"""
import os

# Step 5: Merge Audio with Video Using FFmpeg
output_video = "media/videos/tutorial_script/480p15/AirflowTutorial.mp4"
audio_input = "slide_1.mp3"
os.system(
    f"ffmpeg -i {output_video} -i {audio_input} -c:v copy -c:a aac final_video.mp4"
)

print("Tutorial video generated successfully!")
