# Music Pilot

Music Pilot is a program designed to identify music chords from audio recordings, allowing users to play along with their instrument. This tool is particularly useful for those who are not well-versed in music theory, as it helps to identify the chords of songs, making it easier to play along with others.

## Features

- **Audio Recording**: Capture music recordings directly from your device using Python.
- **Spectrogram Generation**: Create visual representations of the music files in the form of spectrograms.
- **Chord Identification**: (In Progress) Develop a machine learning model to identify chords based on the frequencies displayed in the spectrograms.
- **Music Theory Integration**: (Planned) Implement a RAG (Retrieval-Augmented Generation) model for music theory to:
  - Retrieve information from music documents.
  - Focus on the music scale of the song.
  - Make inferences to validate the identified chords.

## Usage

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Necessary Python libraries:
  - `numpy`
  - `matplotlib`
  - `scipy`
  - `librosa`
  - `tensorflow` or `pytorch` (for the machine learning model)


## Future Work

- **Machine Learning Model**: Develop and train a model to accurately identify chords from spectrograms.
- **Music Theory Integration**: Implement the RAG model to enhance the chord identification process by incorporating music theory.
- **User Interface**: Create a user-friendly interface to make the tool accessible to users with minimal technical knowledge.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.


## Contact

For any questions or suggestions, feel free to reach out to me at avillalobos@utexas.edu

---

Thank you for using Music Pilot! Let's make music theory accessible and enjoyable for everyone.
