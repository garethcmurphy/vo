#!/usr/bin/env python3
# Description: Combine multiple MP3 files into a single MP3 file using the pydub library.

from pydub import AudioSegment

# Constants
AUDIO_FILES = [
    "slide_1.mp3",
    "slide_2.mp3",
    "slide_3.mp3",
    "slide_4.mp3",
    "slide_5.mp3",
]

class AudioCombiner:
    """
    A class to combine multiple MP3 files into a single MP3 file.
    
    Attributes:
        audio_files (list): List of MP3 files to combine.
    """
    
    def __init__(self, audio_files):
        """
        Initializes the AudioCombiner with a list of audio files.
        
        Args:
            audio_files (list): List of MP3 files to combine.
        """
        self.audio_files = audio_files
        self.combined_audio = None

    def load_first_file(self):
        """
        Loads the first audio file to start the combination process.
        """
        if not self.audio_files:
            raise ValueError("No audio files provided.")
        self.combined_audio = AudioSegment.from_file(self.audio_files[0])

    def combine_files(self):
        """
        Combines all the audio files into a single audio segment.
        """
        if self.combined_audio is None:
            self.load_first_file()
        
        for file in self.audio_files[1:]:
            audio = AudioSegment.from_file(file)
            self.combined_audio += audio

    def export_combined_audio(self, output_file):
        """
        Exports the combined audio to a file.
        
        Args:
            output_file (str): The path to the output file.
        """
        if self.combined_audio is None:
            raise ValueError("No combined audio to export.")
        self.combined_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    combiner = AudioCombiner(AUDIO_FILES)
    combiner.combine_files()
    combiner.export_combined_audio("combined_output.mp3")
