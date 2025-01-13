#!/usr/bin/env python3
# compbing slide_1.mp3 with the other ten audio files

import os

# merge audio files in sequence

def main():
    """main function"""

    audio_files = [
        "slide_1.mp3",
        "slide_2.mp3",
        "slide_3.mp3",
        "slide_4.mp3",
        "slide_5.mp3",
        "slide_6.mp3",  
        "slide_7.mp3",
        "slide_8.mp3",
        "slide_9.mp3",
        "slide_10.mp3",
    ]

    # Step 5: Merge Audio with Video Using FFmpeg
    output_video = "media/videos/tutorial_script/480p15/AirflowTutorial.mp4"

    # merge audio files
    audio_input = "|".join(audio_files)
    os.system(
        f"ffmpeg -i {output_video} -i concat:{audio_input} -c:v copy -c:a aac final_video.mp4"
    )


if __name__ == "__main__":
    main()
    print("Tutorial video generated successfully!")