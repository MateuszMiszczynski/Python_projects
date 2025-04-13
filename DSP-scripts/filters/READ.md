## Scripts Overview

### Filter_Design_Zero_Pole.py
This script designs a band-pass filter using the zero-pole method. It places poles and zeros on the complex plane to create the transfer function. The script plots the following:
- Pole-zero diagram
- Amplitude-frequency response (both linear and dB)
- Phase-frequency response

The script helps verify the band-pass behavior of the filter and its impact on the signal.

### Butterworth_Low-Pass_Filter_Design.py
This script designs Butterworth low-pass filters (LP) for orders \(N = 2, 4, 6, 8\) with a cutoff frequency. It places poles on the left half of the complex plane, forming a circle with a radius equal to the cutoff frequency. The script plots:
- Amplitude and phase characteristics (linear and logarithmic scales)
- Impulse response
- Step response for the N = 4 filter

### Anti-Aliasing_Filter_Design.py
This script designs an anti-aliasing low-pass filter to prevent frequency aliasing before an A/D converter. The filter design aims to:
- Attenuate frequencies above the Nyquist frequency f_s/2
- Pass frequencies below f_s/2

The filter is designed using different types:
- Butterworth
- Chebyshev 1
- Chebyshev 2
- Elliptic (the best one so far)

The design seeks the smallest possible filter order with:
- A maximum ripple of 3 dB in the passband (up to 64 kHz)
- At least 40 dB attenuation at f_s/2 (128 kHz)

The script plots:
- Pole distribution
- Frequency response of the analog transfer function H(s)

### FM Radio Station Separation Filter.py
This script designs a bandpass analog filter for separating FM radio stations. The design process includes:
1. A test filter designed for a frequency range of 96 MHz ± 1 MHz.
2. A target filter for a narrower range of 96 MHz ± 100 kHz.

The filter is designed with:
- No more than 3 dB ripple in the passband
- At least 40 dB attenuation in the stopband

The frequency response of the designed filter is plotted with the frequency axis in Hz, showing key points like the passband and stopband limits. If the filter characteristics are unsatisfactory, the requirements for stopband attenuation can be relaxed, and the filter order increased.

Design the low-pass prototype filter and then perform a frequency transformation to a bandpass filter.
