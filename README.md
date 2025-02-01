# DTMF-DETECTION

## Aim : DTMF (DUAL TONE MULTIPLE FREQUENCY)  Detection.

"To design, implement, and test a real-time DTMF (Dual-Tone Multi-Frequency) detection system using Python, with the objective of identifying telephone keypad tones and decoding them into corresponding digits or symbols based on their frequency components."

- DTMF Background:

### What is DTMF?
Dual-Tone Multi-Frequency (DTMF) is a signaling system used in telecommunication to send information through audible tones. It is widely used in telephone systems, interactive voice response (IVR) systems, and remote control applications.

### How DTMF Works?
1.	When a user presses a key on a telephone keypad, the system generates two simultaneous tones:
a.	One from a low-frequency group
b.	One from a high-frequency group
2.  The combination of these tones uniquely identifies the pressed key.

![image](https://github.com/user-attachments/assets/ed30d797-aad9-4033-9148-58a879b897d7)

 ### DTMF Detection Methods
1.	Goertzel Algorithm – A computationally efficient way to detect specific frequencies.
2.	Fast Fourier Transform (FFT) – Extracts dominant frequencies from an audio signal.
3.	Bandpass Filters – Filters out unwanted frequencies to isolate DTMF tones


 ### Algorithm:

- Step 1: Setup the Environment
1.	Install necessary Python libraries (numpy, scipy, sounddevice).
2.	Open Visual Studio Code and create a new Python script.
- Step 2: Capture or Load Audio Input
1.	Record audio using sounddevice or load a pre-recorded .wav file using scipy.io.wavfile.
2.	Set the sampling rate (e.g., fs = 8000 Hz).
- Step 3: Preprocess the Audio
1.	Convert the recorded audio into a numerical array using numpy.
2.	Normalize the signal for better frequency detection.
- Step 4: Apply Fourier Transform (FFT)
1.	Compute the Fast Fourier Transform (numpy.fft.fft) of the signal.
2.	Extract the dominant frequency components.
- Step 5: Identify DTMF Frequencies
1.	Find the two most prominent frequencies in the signal.
2.	Match these frequencies with standard DTMF frequency pairs.
- Step 6: Map Frequencies to Keypad Digits
1.	Use a predefined lookup table to determine the corresponding DTMF digit.
2.	Print or store the detected digit.
- Step 7: Display the Results
1.	Show the detected key in the console or a GUI.
2.	Optionally, plot the frequency spectrum using matplotlib for debugging.
- Step 8: Optimize for Real-Time Detection
1.	Process small chunks of audio instead of the entire signal at once.
2.	Use a sliding window approach for continuous detection. 

### OUTPUT

![image](https://github.com/user-attachments/assets/97c7d861-d4a8-4462-9a50-315dda0a4b34)

