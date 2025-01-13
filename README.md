# Setup Video for Tutorial in Airflow

This project demonstrates how to create a tutorial video using Manim and gTTS. The tutorial covers setting up an Apache Airflow DAG for mapping ontology data from an API.

## Project Structure

## Dependencies

The project uses the following dependencies:
- Python 3.12
- Manim 0.18.1
- gTTS 2.5.4
- pydub 0.25.1

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd voiceover
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

## Usage

1. **Generate Voiceover Audio**:
    ```sh
    poetry run python src/generate_voiceover_audio.py
    ```

2. **Render Slides Using Manim**:
    ```sh
    poetry run manim -pql src/tutorial_script.py AirflowTutorial
    ```

3. **Combine Audio Files**:
    ```sh
    poetry run python src/combine.py
    ```

4. **Merge Audio with Video Using FFmpeg**:
    ```sh
    ffmpeg -i media/videos/tutorial_script/480p15/partial_movie_files/AirflowTutorial/partial_movie_file_list.txt -i voiceover_audio.mp3 -c:v copy -c:a aac final_video.mp4
    ```

## Project Files

- **[src/generate_voiceover_audio.py](http://_vscodecontentref_/4)**: Script to generate voiceover audio using gTTS.
- **[src/tutorial_script.py](http://_vscodecontentref_/5)**: Manim script to create tutorial slides.
- **[src/audio_combiner.py](http://_vscodecontentref_/6)**: Class to combine multiple audio files into one.
- **[src/combine.py](http://_vscodecontentref_/7)**: Script to combine audio files and merge with video using FFmpeg.

## License

This project is licensed under the MIT License.

