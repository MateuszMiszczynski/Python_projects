import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ellip, freqs
import sympy as sp


f = np.arange(90e6, 102e6 + 100, 100)  # od 90 MHz do 102 MHz co 100 Hz
f0 = 96e6                              # częstotliwość środkowa
w = 2 * np.pi * f                      # częstotliwość kątowa


# Filtr testowy: 96 MHz ±1 MHz
N1 = 5
wp1 = [2*np.pi*(f0 - 1e6), 2*np.pi*(f0 + 1e6)]
b1, a1 = ellip(5, 3, 40, wp1, btype='bandpass', analog=True)
w_, H1 = freqs(b1, a1, worN=w)
H1 = H1 / np.max(np.abs(H1))
H1log = 20 * np.log10(np.abs(H1))

plt.figure("Filtr testowy")
plt.plot(f, H1log, 'b')
plt.title('Filtr testowy: 96 MHz ±1 MHz')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('20*log10|H(jω)| [dB]')
plt.ylim([-140, 20])
plt.grid(True)

# Filtr docelowy: 96 MHz ±100 kHz
N2 = 3
wp2 = [2*np.pi*(f0 - 1e5), 2*np.pi*(f0 + 1e5)]
b2, a2 = ellip(N2, 3, 40, wp2, btype='bandpass', analog=True)
w_, H2 = freqs(b2, a2, worN=w)
H2 = H2 / np.max(np.abs(H2))
H2log = 20 * np.log10(np.abs(H2))

plt.figure("Filtr docelowy")
plt.plot(f, H2log, 'r')
plt.title('Filtr docelowy: 96 MHz ±100 kHz')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('20*log10|H(jω)| [dB]')
plt.ylim([-140, 20])
plt.grid(True)

# Porównanie filtrów
plt.figure("Porównanie filtrów")
plt.plot(f, H1log, 'b', label='1 MHz')
plt.plot(f, H2log, 'r', label='100 kHz')
plt.title('Porównanie filtrów')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('20*log10|H(jω)| [dB]')
plt.ylim([-140, 20])
plt.legend()
plt.grid(True)

# Granice pasma
plt.figure("Granice pasma")
plt.plot(f, H1log, 'b', label='1 MHz')
plt.plot(f, H2log, 'r', label='100 kHz')

# linie graniczne pasma
plt.axvline(95.9e6, color='k', linestyle='--')
plt.axvline(96.1e6, color='k', linestyle='--')
plt.axvline(95e6, color='k', linestyle='--')
plt.axvline(97e6, color='k', linestyle='--')
plt.axhline(-3, color='k', linestyle='--')
plt.axhline(-40, color='k', linestyle='--')

plt.title('Granice pasma zaporowego i przepustowego')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('20*log10|H(jω)| [dB]')
plt.ylim([-140, 20])
plt.legend()
plt.grid(True)
plt.show()






# Projekt prototypu LP

n = 7

# Definicja symbolu s (dziedzina Laplace'a)
s = sp.symbols('s', complex=True)

# Obliczamy bieguny Butterwortha dla LP o jednostkowej częstotliwości odcięcia (1 rad/s)
# Dla filtru Butterwortha bieguny są dane wzorem:
#   p_k = exp(j*pi*(2*k + n - 1) / (2*n)), k = 1, 2, ..., n
# Przyjmujemy tylko te, które są w lewej połowie płaszczyzny (stabilne)
poles = []
for k in range(1, n + 1):
    pk = sp.exp(sp.I * sp.pi * (2 * k + n - 1) / (2 * n)) #
    if sp.re(pk) < 0:  # wybieramy bieguny o ujemnej części rzeczywistej
        poles.append(pk)

# Wielomian mianownika prototypu LP tworzymy jako (s - p1)(s - p2)...(s - p_m)
A_lp = sp.expand(sp.prod(s - p for p in poles))
# Zakładamy licznik równy 1 (unitary gain), więc transmitancja:
H_lp = 1 / A_lp


# Transformacja LP -> BP

# Parametry filtru BP – przykładowo dla odbioru stacji FM:
#   - Częstotliwość środkowa f0 = 96 MHz
#   - Pożądane pasmo przepustowe: ±100 kHz (czyli szerokość pasma B_f = 200 kHz)
f0 = 96e6  # środek w Hz
B_f = 200e3  # pełna szerokość pasma w Hz (od -100 kHz do +100 kHz względem f0)

# Konwertujemy do częstotliwości kątowych (rad/s)
omega0 = 2 * sp.pi * f0  # środkowa częstotliwość w rad/s
B = 2 * sp.pi * B_f  # szerokość pasma BP w rad/s

# Transformacja LP do BP wzór:
#      s  -> (s^2 + ω0^2) / (B * s)
# Dlatego w transmitancji podstawiamy:
s_lp = (s ** 2 + omega0 ** 2) / (B * s)

# Otrzymujemy transmitancję BP przez podstawienie s_lp do H_lp(s)
H_bp = sp.simplify(H_lp.subs(s, s_lp))
H_bp = sp.together(H_bp)  # łączenie ułamków w jedną postać


# Aby sprawdzić charakterystykę częstotliwościową filtru BP, podstawiamy s = jω
# Wybieramy zakres częstotliwości ok. ω0
omega0_float = float(omega0)
omega_vals = np.linspace(omega0_float * 0.8, omega0_float * 1.2, 1000)  # ok. 80% do 120% ω0

# Przygotowujemy funkcję H_bp(s) numeryczną – podstawiamy s = j*ω
H_bp_func = sp.lambdify(s, H_bp, 'numpy')
H_bp_vals = H_bp_func(1j * omega_vals)

plt.figure(figsize=(8, 5))
plt.plot(omega_vals / (2 * np.pi), 20 * np.log10(np.abs(H_bp_vals)))
plt.title("Charakterystyka BP uzyskana przez transformację prototypu LP")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Wzmocnienie [dB]")
plt.grid(True)
plt.show()
