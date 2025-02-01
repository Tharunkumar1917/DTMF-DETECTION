import numpy as np
import sounddevice as sd
from scipy.signal import find_peaks
from scipy.fft import rfft, rfftfreq

# Define DTMF frequencies
DTMF_FREQS = {
    (697, 1209): '1', (697, 1336): '2', (697, 1477): '3', (697, 1633): 'A',
    (770, 1209): '4', (770, 1336): '5', (770, 1477): '6', (770, 1633): 'B',
    (852, 1209): '7', (852, 1336): '8', (852, 1477): '9', (852, 1633): 'C',
    (941, 1209): '*', (941, 1336): '0', (941, 1477): '#', (941, 1633): 'D'
}

# Sampling parameters
SAMPLE_RATE = 44100  # Audio sample rate in Hz
DURATION = 0.1       # Duration of each chunk of audio (in seconds)

# Find the closest frequency match
def find_closest(freq, freq_list, tolerance=10):
    for f in freq_list:
        if abs(freq - f) <= tolerance:
            return f
    return None

# Function to detect DTMF tones
def detect_dtmf(audio):
    # Perform FFT on the audio data
    fft_spectrum = rfft(audio)
    frequencies = rfftfreq(len(audio), d=1/SAMPLE_RATE)
    magnitude = np.abs(fft_spectrum)

    # Find prominent frequencies
    peaks, _ = find_peaks(magnitude, height=max(magnitude) * 0.5)
    detected_freqs = [frequencies[p] for p in peaks]

    # Match frequencies to DTMF table
    low_group = [697, 770, 852, 941]
    high_group = [1209, 1336, 1477, 1633]

    low_freq = find_closest(min(detected_freqs, default=0), low_group)
    high_freq = find_closest(max(detected_freqs, default=0), high_group)

    if low_freq and high_freq and (low_freq, high_freq) in DTMF_FREQS:
        return DTMF_FREQS[(low_freq, high_freq)]
    return None

# Callback function for real-time audio processing
def audio_callback(indata, frames, time, status):
    if status:
        print(f"Status: {status}")
      # Flatten the audio data to mono
    audio_data = indata[:, 0]
    # Detect DTMF tone
    tone = detect_dtmf(audio_data)
    if tone:
        print(f"Detected DTMF Tone: {tone}")

# Start real-time audio stream
if __name__ == "__main__":
    print("Listening for DTMF tones...")
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE, blocksize=int(SAMPLE_RATE * DURATION)):
        sd.sleep(1000000)  # Run for 10 seconds (adjust as needed)


