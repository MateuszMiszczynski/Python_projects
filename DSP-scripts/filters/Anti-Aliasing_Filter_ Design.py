import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, cheby2, ellip, freqs, tf2zpk

# Parametry
fs = 256e3
f0 = fs / 2
f3dB = f0 / 2
w0 = 2 * np.pi * f0
w3dB = 2 * np.pi * f3dB
# w3dB - to częstotliwość graniczna filtru czyli częstotliwość
# dla której filtr zaczyna tłumić sygnały czyli u nas poniżej 65kHz
# ale funkcje butter,cheby1 itp działają na częstotliwosciach kątowych rad/s

f = np.arange(0, 300e3 + 1, 1)  # 0 do 300 kHz
w = 2 * np.pi * f

def plot_response(f, Hlog, label):
    plt.plot(f, Hlog, label=label)
    plt.plot([0, 300e3], [-3, -3], 'k')
    plt.plot([0, 300e3], [-40, -40], 'k')
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('20*log10|H(jω)| [dB]')
    plt.title('Charakterystyka amplitudowa (dB)')
    plt.grid(True)

def plot_poles_zeros(b, a, title):
    z, p, k = tf2zpk(b, a)
    plt.figure()
    plt.plot(np.real(p), np.imag(p), 'ro')
    plt.title(title)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.grid(True)

# Butterworth
N = 7
b1, a1 = butter(N, w3dB, btype='low', analog=True)
# b1 - współczynnik licznika transmitancji
# a1 - współczynnik mianownika transmitancji
# transmitancja H(s) =  (b1[0] * s⁷ + b1[1] * s⁶ + ... ) / (a1[0] * s⁷ + a1[1] * s⁶ + ...)
# To tzw. transmitancja filtru analogowego w domenie Laplace’a

w_, H1 = freqs(b1, a1, worN=w)
# freqs - liczy odpowiedź częstotliwościową filtru analogowego
# worN=w - to mówi, żeby obliczyć H(jω) dla wartości w (czyli naszej częstotliwości w rad/s)
# w_ - zwraca te same częstotliwości (można pominąć)
# H1 - wartość funkcji H(s) w tych punktach to liczby zespolone
# H1 - wektor zespolone warotści transmitancji H(j*omega) dla wielu punktów omega
# Pokazuje jak silnie filtr przepuszcza sygnał dla danej omegi

H1log = 20 * np.log10(np.abs(H1 / np.max(H1)))

plt.figure()
plot_response(f, H1log, 'Butterworth N=7')
plt.legend()
plot_poles_zeros(b1, a1, 'Bieguny filtru Butterworth')

# Chebyshev I
N = 5
b2, a2 = cheby1(N, 3, w3dB, btype='low', analog=True)
w_, H2 = freqs(b2, a2, worN=w)
H2log = 20 * np.log10(np.abs(H2 / np.max(H2)))

plt.figure()
plot_response(f, H2log, 'Chebyshev I N=5')
plt.legend()
plot_poles_zeros(b2, a2, 'Bieguny filtru Czebyszewa I')

# Chebyshev II
N = 5
b3, a3 = cheby2(N, 40, w0, btype='low', analog=True)
w_, H3 = freqs(b3, a3, worN=w)
H3log = 20 * np.log10(np.abs(H3 / np.max(H3)))

plt.figure()
plot_response(f, H3log, 'Chebyshev II N=5')
plt.legend()
plot_poles_zeros(b3, a3, 'Bieguny filtru Czebyszewa II')

# Eliptyczny
N = 5
b4, a4 = ellip(N, 3, 40, w3dB, btype='low', analog=True)
# 3 - zafalowanie w pasmie przepustowym,a le szybko tłumi poza tym pasmem
# 40 - tłumienie w paśmie zaporowym
w_, H4 = freqs(b4, a4, worN=w)
H4log = 20 * np.log10(np.abs(H4 / np.max(H4)))

plt.figure()
plot_response(f, H4log, 'Eliptyczny N=10')
plt.legend()
plot_poles_zeros(b4, a4, 'Bieguny filtru eliptycznego')

# Pomiar zafalowania i tłumienia
def get_value_at(freq_Hz, f, Hlog):
    idx = np.argmin(np.abs(f - freq_Hz))
    return Hlog[idx]

print("Zmiany tłumienia (dla f3dB = 64 kHz):")
print("Butterworth:", get_value_at(64e3, f, H1log))
print("Chebyshev I:", get_value_at(64e3, f, H2log))
print("Chebyshev II:", get_value_at(64e3, f, H3log))
print("Eliptyczny:", get_value_at(64e3, f, H4log))

print("\nTłumienia (dla fs/2 = 128 kHz):")
print("Butterworth:", get_value_at(128e3, f, H1log))
print("Chebyshev I:", get_value_at(128e3, f, H2log))
print("Chebyshev II:", get_value_at(128e3, f, H3log))
print("Eliptyczny:", get_value_at(128e3, f, H4log))

plt.show()
