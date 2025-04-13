import numpy as np
import scipy.io
import matplotlib.pyplot as plt

# Wczytanie pliku .mat
file_path = "ECG100.mat"
mat_data = scipy.io.loadmat(file_path)

# Pobranie sygnału EKG i skrócenie o połowę
ecq_signal = mat_data["val"]
N = ecq_signal.shape[1] // 2  # Skrócenie liczby próbek o połowę
ecq_signal = ecq_signal[:, :N]

# W FFT składowa stałą sygnalu jest w f = 0Hz, ten sygnał ma bardzo
# silną składową stałą więc aby wykres byłczytelny i aby ją usunąć
# odejmiemy wartość średnią sygnału przed dokonaniem FFT

ecq_signal[0] = ecq_signal[0] - np.mean(ecq_signal[0])

# W drugim przypadku widzimy na osi czasu że sygnal jest przesunięty
# w góre lub w dół co oznacza ze wartośc średnia jest różna od zera
# Ale wciąż dominuje więc sie jej pozbywamy

ecq_signal[1] = ecq_signal[1] - np.mean(ecq_signal[1])

# Parametry
fs = 400
t = np.arange(N) / fs

# Rysowanie sygnałów EKG
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, ecq_signal[0], label="Kanał 1")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Sygnał EKG - Kanał 1")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, ecq_signal[1], label="Kanał 2", color='b')
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Sygnał EKG - Kanał 2")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Obliczanie DFT (FFT)
freqs = np.fft.fftfreq(N, 1 / fs)  # Oś częstotliwości w Hz
fft_ch1 = np.fft.fft(ecq_signal[0]) / N
fft_ch2 = np.fft.fft(ecq_signal[1]) / N

# Obliczanie DtFT
fmax = 2.5 * fs  # Maksymalna częstotliwość dla DtFT
df = 0.5  # Krok częstotliwości
f_dtft = np.arange(0, fmax, df)  # Zakres częstotliwości
dtft_ch1 = np.array([np.sum(ecq_signal[0] * np.exp(-1j * 2 * np.pi * f / fs * np.arange(N))) / N for f in f_dtft])
dtft_ch2 = np.array([np.sum(ecq_signal[1] * np.exp(-1j * 2 * np.pi * f / fs * np.arange(N))) / N for f in f_dtft])

# Wykresy widma DFT (FFT) w skali liniowej
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(freqs[:N // 2], np.abs(fft_ch1[:N // 2]), 'r-')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo DFT (FFT) - Kanał 1")
plt.xlim(0, 30)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(freqs[:N // 2], np.abs(fft_ch2[:N // 2]), 'b-')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo DFT (FFT) - Kanał 2")
plt.xlim(0, 30)
plt.grid()

plt.tight_layout()
plt.show()

# Wykresy widma DFT (FFT) w skali decybelowej
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(freqs[:N // 2], 20 * np.log10(np.abs(fft_ch1[:N // 2])), 'r-')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.title("Widmo DFT (FFT) - Kanał 1")
plt.xlim(0, 30)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(freqs[:N // 2], 20 * np.log10(np.abs(fft_ch2[:N // 2])), 'b-')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.title("Widmo DFT (FFT) - Kanał 2")
plt.xlim(0, 30)
plt.grid()

plt.tight_layout()
plt.show()

# Wykresy widma DtFT w skali liniowej
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(f_dtft, np.abs(dtft_ch1), 'r-')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo DtFT - Kanał 1")
plt.xlim(0, 60)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(f_dtft, np.abs(dtft_ch2), 'b-')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo DtFT - Kanał 2")
plt.xlim(0, 60)
plt.grid()

plt.tight_layout()
plt.show()

# Wykresy widma DtFT w skali decybelowej
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(f_dtft, 20 * np.log10(np.abs(dtft_ch1)), 'r-')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.title("Widmo DtFT - Kanał 1")
plt.xlim(0, 60)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(f_dtft, 20 * np.log10(np.abs(dtft_ch2)), 'b-')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.title("Widmo DtFT - Kanał 2")
plt.xlim(0, 60)
plt.grid()

plt.tight_layout()
plt.show()
