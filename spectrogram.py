import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
import os
import re


# Segmentation of spectrogram
def sg_segments(file, cat):
    samples, sample_rate, frequencies, times, spectrogram = create_spectrogram(file)
    audio_dur = len(samples)/ sample_rate
    # split the spectrogram in intervals of 5 seconds
    for i in range(5, int(round(audio_dur)) + 5, 5):
        start_idx = np.searchsorted(times, i-5)
        end_idx = np.searchsorted(times, i)
        interval = times[start_idx:end_idx]
        adjusted_sg = np.log10(spectrogram[:, start_idx:end_idx])
        plot_spectrogram_segment(sample_rate, interval, frequencies, adjusted_sg, cat)


# file: WAV file
# cat: category of audio
# returns variables: frequencies, times, and spectrogram
def create_spectrogram(file):
    nperseg = 1024 # Window size
    noverlap = nperseg // 2  # 50% overlap
    sample_rate, samples = wavfile.read(f'audio_files/{file}')
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nperseg=nperseg, noverlap=noverlap)
    return samples, sample_rate, frequencies, times, spectrogram


# creates and saves spectrogram 
def plot_spectrogram_segment(sample_rate, interval, frequencies, adjusted_sg, cat):
    # obtain index for spectrogram file creation
    index = index_folder(cat)
    # limit range of spectrogram
    freq_limit = 2200  # 2.2 kHz
    max_freq_index = np.where(frequencies > freq_limit)[0][0]
    # Plot a segment of the spectrogram data
    plt.figure(figsize=(10, 8))  # Adjust figsize to your preference
    plt.pcolormesh(interval, frequencies[:max_freq_index], adjusted_sg[:max_freq_index, :], shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar(label='Intensity [dB]')
    plt.ylim([0, 2200])  # Update this if you want to zoom into a frequency range
    plt.title(f"Spectrogram from {int(interval[0])} to {int(interval[-1])+1} seconds")
    plt.savefig(f'spectrograms/sg_{cat}{index}.png', dpi=300)
    plt.close()
    

# args: type-what type of spectrogram is it i.e. chord or music sample
def index_folder(cat):
    files = os.listdir(f'spectrograms/')
    filename = f"sg_{cat}"
    pattern = re.compile(rf"^{filename}(\d+)\.png$")
    indices = [int(match.group(1)) for file in files if (match := pattern.match(file))]
    # determine next available index
    return max(indices) + 1 if indices else 1


def main():
    file = input("Enter file name recording: ")
    cat = input("Enter category of file (description): ")
    sg_segments(file, cat)
    return

if __name__ == '__main__':
    main()