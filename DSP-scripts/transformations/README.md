### DFT_of_a_Harmonic_Signal
This script calculates the Discrete Fourier Transform (DFT) matrix for a signal composed of two cosine waves with different frequencies. The signal is sampled at 1000 Hz with 100 samples, and includes:
- A 100 Hz component
- A 200 Hz component
Each component has its own amplitude and phase.

The script performs the following:
- Computes the DFT of the signal
- Visualizes the real and imaginary parts, magnitude, and phase of the frequency spectrum
- Reconstructs the signal from its frequency components using the DFT matrix and compares the reconstructed signal to the original
- Replaces DFT with Fast Fourier Transform (FFT) and uses the inverse FFT for signal reconstruction
- Alters the first component's frequency to 125 Hz and recalculates the spectrum

---

### DTFT_Basics_Implementation.py
This script analyzes the frequency content of a signal using three different methods:
- Standard DFT (X1)
- Zero-padded DFT for increased resolution (X2)
- Direct computation of the Discrete-Time Fourier Transform (X3)

The process includes:
- Extending the signal by appending 100 zeros for improved frequency resolution
- Comparing the three spectra on a single plot to highlight differences in resolution and periodicity
- Visualizing the periodic nature of the DtFT across a broader frequency range (-2fs to 2fs)

---

### DTFT_Windowing_and_Resolution.py
This script compares the DtFT of a signal consisting of two sinusoids (100 Hz and 125 Hz, with one much weaker) by applying different window functions:
- Rectangular window
- Hamming window
- Blackman window
- Chebyshev window (with 100 dB and 120 dB attenuation)

The process includes:
- Plotting all spectra to observe how the window type affects visibility and leakage
- Increasing the sample count to 1000 and comparing the effects of Chebyshev windows with different attenuation

---

### FFT_ADSL_Spectrum_Analysis.py
This script analyzes an ADSL signal from the `ADSL.mat` file, which contains 8 frames of 512 samples each, preceded by a 32-sample prefix. The task involves:
- Removing the prefix from each frame
- Performing a 512-point FFT on the remaining data
- Examining the resulting frequency spectrum to identify which harmonic frequencies are used in each frame
- Visualizing the magnitude spectrum to determine the frequency components carrying data in the ADSL signal

---

### DTFT_FFT_ECG_Signal_Analysis_py
This script analyzes the EKG signal from the `ECG100.mat` file. The goal is to determine the heart rate by performing both DFT and DtFT on the signal:
- Use DFT (fft(x)) and DtFT to compute the frequency components
- Plot the EKG signal with the time axis scaled in seconds
- Show its spectra with the frequency axis scaled in Hertz
- Display the spectra in both linear and decibel scales to observe heart rate frequencies

---

### FFT_Sound_Signal_Filtering.py
This script uses two sound signals with different frequency content:
- A low-frequency signal (e.g., car engine)
- A high-frequency signal (e.g., bird chirping)

The process includes:
- Computing their DFT spectra
- Adding the signals together (padding the shorter signal with zeros)
- Zeroing out the DFT coefficients of one signal's frequencies
- Performing an inverse DFT (IDFT) to reconstruct the filtered signal
- Listening to the filtered signal and verifying its correctness

---

Feel free to explore and modify the scripts for your DSP projects!
