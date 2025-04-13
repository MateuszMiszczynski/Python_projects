import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
import sounddevice as sd
import scipy.io.wavfile as wav
import librosa


# Wczytywanie plików dźwiękowych
def load_audio(file):
    data, rate = librosa.load(file, sr=None)  # Automatyczne wczytanie próbkowania
    return rate, data

def plot_spectrum(data, rate, title):
    N = len(data)
    freqs = np.fft.fftfreq(N, 1/rate)
    spectrum = np.fft.fft(data)
    plt.figure()
    plt.plot(freqs[:N//2], np.abs(spectrum[:N//2])) # N//2 oznacza, że bierzemy częstotliwości od 0 Hz do Nyquista (rate/2).
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplituda")
    plt.show()

def play_audio(data, rate):
    sd.play(data / np.max(np.abs(data)), rate) #  Normalizuje sygnał do zakresu [-1, 1], aby uniknąć przesterowania.
    sd.wait() # Czeka, aż dźwięk skończy grać.


rate1, sound1 = load_audio("low_freq.wav")
rate2, sound2 = load_audio("high_freq.wav")

# Analiza widma
plot_spectrum(sound1, rate1, "Spectrum of Low-Frequency Sound")
plot_spectrum(sound2, rate2, "Spectrum of High-Frequency Sound")

# Ustalamy wspólną częstotliwość próbkowania (najwyższą z dwóch)
target_rate = max(rate1, rate2)

# Resampling obu dźwięków do target_rate BO INACZEJ SIE NIE DODADZĄ POPRAWNIE
sound1_resampled = librosa.resample(sound1, orig_sr=rate1, target_sr=target_rate)
sound2_resampled = librosa.resample(sound2, orig_sr=rate2, target_sr=target_rate)

# Wyrównanie długości
length = max(len(sound1_resampled), len(sound2_resampled))
sound1_resampled = np.pad(sound1_resampled, (0, length - len(sound1_resampled)), 'constant')
sound2_resampled = np.pad(sound2_resampled, (0, length - len(sound2_resampled)), 'constant')

# Sumowanie dźwięków
total_sound = sound1_resampled + sound2_resampled


# Zerowanie składowych niskiej częstotliwości
spectrum_total = scipy.fft.fft(total_sound)

threshold = 500 # Przykładowa wartość odcięcia dla niskich częstotliwości

N = len(total_sound)
freqs = np.fft.fftfreq(N, 1/target_rate)

for i in range(N):
    if freqs[i] < threshold :
        spectrum_total[i] = 0

# Odtwarzanie odfiltrowanego dźwięku
filtered_sound = np.real(scipy.fft.ifft(spectrum_total))
plot_spectrum(filtered_sound, target_rate, "Spectrum after Filtering")
play_audio(filtered_sound, target_rate)

# Zapis wyniku do pliku
wav.write("filtered_sound.wav", target_rate, filtered_sound)
