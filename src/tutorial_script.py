#!/usr/bin/env python3
"""script to generate a tutorial video using Manim and gTTS"""

import os

from manim import Scene, Text, Write


# Step 3: Define Slides Using Manim
class AirflowTutorial(Scene):
    """script to generate a tutorial video using Manim and gTTS"""

    def construct(self):
        # Slide 1
        slide_1 = Text("Setting Up an Airflow DAG\n for Ontology Data Mapping")
        self.play(Write(slide_1))
        self.wait(10)  # Match this to the length of audio
        self.remove(slide_1)

        # Slide 2
        slide_2 = Text(
            """
What We’ll Cover\n-
 Problem and Solution\n
 - Setting up Airflow\n- Tasks for Data Fetching and Mapping\n- Testing and Deployment
 """
        )
        self.play(Write(slide_2))
        self.wait(10)
        self.remove(slide_2)

        # Add more slides here, following the same format
        # ...


# Step 4: Combine Slides and Voiceover into Video
os.system("manim -pql tutorial_script.py AirflowTutorial")
