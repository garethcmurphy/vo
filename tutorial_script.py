#!/usr/bin/env python3
"""script to generate a tutorial video using Manim and gTTS"""
import os
from gtts import gTTS
#from manim import *
from manim import Scene, Text, Write

# Step 1: Voiceover Text for Each Slide
voiceover_text = [
    """
Welcome to this step-by-step tutorial on creating an Apache Airflow DAG for mapping ontology data from an API.
In this session, we’ll use a sample dataset from early pharma research to demonstrate how you can automate your workflows.""",
    """
Here’s what we’ll cover: First, we’ll outline the problem and solution.
Then, we’ll set up the Airflow environment, define the tasks for data fetching and mapping, and finally, test and deploy the DAG.
Let’s dive in!""",
    """
Ontology mapping can be a time-consuming and error-prone task when done manually. 
By automating this process, we can save time and ensure
    consistent, accurate mapping for early pharma research data.""",
    """An Airflow DAG, or Directed Acyclic Graph, is used to define workflows as
    a sequence of tasks. In our case, we’ll set up a DAG with two main tasks:
    fetching ontology data and mapping it to research terms.""",
    """We begin by defining the DAG. This includes specifying default arguments,
    such as retry behavior, and the DAG’s schedule interval. Here, we’ve set it
    to run daily starting from January 1, 2025.""",
    """Our first task is to fetch ontology data from an API. This function sends
    a request to the API and returns the data in JSON format if successful.
    Don’t forget to replace the placeholder URL with your actual API
    endpoint.""",
    """The next task is to map the ontology data to your research terms. This
    example matches ontology terms to those in a sample pharma dataset.
    Customize this logic to fit your specific requirements.""",
    """Finally, we link the tasks in our DAG. This ensures that the mapping task
    runs only after the data has been successfully fetched from the API.""",
    """To test your DAG, save the Python file in Airflow’s `dags` folder,
    restart the scheduler, and use the Airflow UI to trigger the DAG manually.
    Check the logs to ensure all tasks run successfully.""",
    """Congratulations! You’ve successfully created an Airflow DAG to fetch
    ontology data and map it to research terms. If you enjoyed this tutorial,
    don’t forget to like, share, and subscribe for more data automation
    tips.""",
]

# Step 2: Generate Voiceover Audio
audio_files = []
for i, text in enumerate(voiceover_text):
    tts = gTTS(text)
    audio_file = f"slide_{i + 1}.mp3"
    tts.save(audio_file)
    audio_files.append(audio_file)


# Step 3: Define Slides Using Manim
class AirflowTutorial(Scene):
    """script to generate a tutorial video using Manim and gTTS"""
    def construct(self):
        # Slide 1
        slide_1 = Text("Setting Up an Airflow DAG for Ontology Data Mapping")
        self.play(Write(slide_1))
        self.wait(10)  # Match this to the length of audio
        self.remove(slide_1)

        # Slide 2
        slide_2 = Text(
            "What We’ll Cover\n- Problem and Solution\n- Setting up Airflow\n- Tasks for Data Fetching and Mapping\n- Testing and Deployment"
        )
        self.play(Write(slide_2))
        self.wait(10)
        self.remove(slide_2)

        # Add more slides here, following the same format
        # ...


# Step 4: Combine Slides and Voiceover into Video
os.system("manim -pql tutorial_script.py AirflowTutorial")

# Step 5: Merge Audio with Video Using FFmpeg
output_video = "airflow_tutorial.mp4"
audio_input = "voiceover_audio.mp3"
os.system(
    f"ffmpeg -i {output_video} -i {audio_input} -c:v copy -c:a aac final_video.mp4"
)

print("Tutorial video generated successfully!")
