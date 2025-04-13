# Digital Signal Processing Scripts

This directory contains Python scripts related to Digital Signal Processing (DSP) that were developed during laboratory exercises at AGH University of Krakow. The labs cover various techniques such as Fourier Transforms, Digital and Analog Filters, and their applications.

## Folder Structure

### `transformations/`
This folder contains scripts related to transformations, such as Fourier Transforms and their applications:
- **DFT (Discrete Fourier Transform)**: Script for computing the discrete Fourier transform.
- **FFT (Fast Fourier Transform)**: Efficient implementation of the fast Fourier transform.
- **DtFT (Discrete-Time Fourier Transform)**: Script for computing the discrete-time Fourier transform.
- **Zero-padding**: Script for padding signals with zeros to improve spectral resolution.

### `filters/`
This folder contains scripts for digital and analog filters:
- **Analog Filters**: Scripts for designing analog filters, including low-pass, high-pass, band-pass, and band-stop filters.
- **Digital Filters**: Scripts for designing digital FIR and IIR filters, using methods like windowing and transformations.

## Scripts Overview

### Transformations
- **Fourier_Transformations.py**: Basic implementation of Fourier Transforms (DFT and DtFT).
- **DFT.py**: Script for applying the Discrete Fourier Transform (DFT).
- **FFT.py**: Efficient Fast Fourier Transform (FFT) implementation.
- **Applications_FFT.py**: Use cases of FFT in signal analysis.

### Filters
- **Analog_Filters.py**: Implementation of analog filters.
- **Digital_Filters_IIR.py**: Recursive IIR digital filter implementation.
- **Digital_Filters_FIR.py**: Non-recursive FIR digital filter implementation.
- **FIR_Sampling_Frequency.py**: FIR filter for changing the sampling frequency.
- **Adaptive_Filters_FIR.py**: Adaptive FIR filters for real-time signal processing.

## Libraries Used
- **numpy**: Numerical operations for signal processing.
- **scipy**: Signal processing tools for creating filters and handling transformations.
- **matplotlib**: Visualization of signals and filter responses.
