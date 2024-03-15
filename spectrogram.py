import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np

nperseg = 1024 # Window size
noverlap = nperseg // 2  # 50% overlap
sample_rate, samples = wavfile.read('output.wav')
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nperseg=nperseg, noverlap=noverlap)

# print("Sample Rate:", sample_rate)
# print("Total Samples:", len(samples))
# print("Audio Duration:", len(samples) / sample_rate, "seconds")

# plt.figure(figsize=(10, 4))
# plt.pcolormesh(times, frequencies, 10*np.log(spectrogram))
# plt.imshow(spectrogram)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')

# aspect_ratio = 0.005  # This is an example; adjust it based on your data and preferences
# plt.gca().set_aspect(aspect_ratio)

# # Set the x-axis limits to match the audio duration
# plt.xlim([0, len(samples) / sample_rate])
# plt.show()

def plot_spectrogram_segment(start_time, end_time):
    # Find the time indices corresponding to the start and end times
    start_idx = np.searchsorted(times, start_time)
    end_idx = np.searchsorted(times, end_time)

    # Plot a segment of the spectrogram data
    plt.figure(figsize=(10, 8))  # Adjust figsize to your preference
    plt.pcolormesh(times[start_idx:end_idx], frequencies, np.log10(spectrogram[:, start_idx:end_idx]), shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar(label='Intensity [dB]')
    plt.ylim([0, sample_rate / 2])  # Update this if you want to zoom into a frequency range
    plt.title(f"Spectrogram from {start_time} to {end_time} seconds")
    plt.show()

# Call this function with the desired time segment
plot_spectrogram_segment(0, 5)  # for the first 5 seconds
plot_spectrogram_segment(5, 10)  # for the next 5 seconds, and so on

# create for loop for segments
# save images as files
