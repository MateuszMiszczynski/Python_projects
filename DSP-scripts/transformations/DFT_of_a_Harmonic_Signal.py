import numpy as np
import matplotlib.pyplot as plt

# Dane
N = 100    # liczba próbek
fs = 1000  # częstotliwość próbkowania
st = 1/fs  # krok próbkowania
T = 0.1    # czas trwania próbkowania

t = np.arange(0, T, st)  # przedział czasowy próbkowania

# Częstotliwości
f1 = 100
f2 = 200

# Amplitudy
A1 = 100
A2 = 200

# Kąty fazowe
p1 = np.pi/7
p2 = np.pi/11

# Tworzenie sygnału z sumy sinusów
s1 = A1 * np.cos(2 * np.pi * f1 * t + p1)
s2 = A2 * np.cos(2 * np.pi * f2 * t + p2)

# Sygnał x z sumy sinusów
x = s1 + s2


# Generowanie macierzy A - macierzy transformacji DFT
W_N = np.exp(1j * 2 * np.pi / N)  # Podstawowy element DFT
A = np.zeros((N, N), dtype=complex)  # Tworzymy macierz N x N na liczby zespolone
for k in range(N):
    for n in range(N):
        A[k, n] = (1 / np.sqrt(N)) * W_N**(-k * n)

# Dyskretna transformata Fouriera - DFT
X = A @ x

# Obliczenie składowych DFT
XRe = np.real(X)
XIm = np.imag(X)
XA = np.abs(X)
XP = np.angle(X) * (XA > 1)

# Skalowanie osi częstotliwości w Herzach
f = np.arange(0, N) * fs / N

# Wykresy
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(f, XRe, 'b-o')
plt.title('Re')
plt.xlabel('Częstotliwość [Hz]')

plt.subplot(2, 1, 2)
plt.stem(f, XIm, 'r-o')
plt.title('Im')
plt.xlabel('Częstotliwość [Hz]')
plt.show()

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(f, XA, 'b-o')
plt.title('A')
plt.xlabel('Częstotliwość [Hz]')

plt.subplot(2, 1, 2)
plt.stem(f, XP, 'r-o')
plt.title('ϕ')
plt.xlabel('Częstotliwość [Hz]')
plt.show()






# Wyznaczanie macierzy rekonstrukcji
B = np.conj(A.T)# macierz odwrotnej transformaty (rekonstrukcji) conj to sprzężenie zespolone
xrcnst = B @ X






# Sprawdzenie błędu rekonstrukcji
error1 = np.max(np.abs(x - xrcnst.real))
print(f'1 Rekonstrukcja sygnału z błędem: {error1}')

# FFT i IFFT
X_fft = np.fft.fft(x)
xrcnst_fft = np.fft.ifft(X_fft)

# Sprawdzenie błędu FFT
error2 = np.max(np.abs(x - xrcnst_fft.real))
print(f'2 Rekonstrukcja sygnału z błędem: {error2}')
print(f'Różnica w rekonstrukcjach sygnału: {error2 / error1}')







# Zmiana f1 na 125Hz
f1 = 125
s1 = A1 * np.cos(2 * np.pi * f1 * t + p1)
x = s1 + s2


# Dyskretna transformata Fouriera - DFT dla nowego sygnału
X = A @ x
XRe = np.real(X)
XIm = np.imag(X)
XA = np.abs(X)
XP = np.angle(X)

# Wykresy nowego sygnału
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(f, XRe, 'b-o')
plt.title('Re')
plt.xlabel('Częstotliwość [Hz]')

plt.subplot(2, 1, 2)
plt.stem(f, XIm, 'r-o')
plt.title('Im')
plt.xlabel('Częstotliwość [Hz]')
plt.show()

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(f, XA, 'b-o')
plt.title('A')
plt.xlabel('Częstotliwość [Hz]')

plt.subplot(2, 1, 2)
plt.stem(f, XP, 'r-o')
plt.title('ϕ')
plt.xlabel('Częstotliwość [Hz]')
plt.show()


# Wieksze N zapewnia krotsze kroki na osi czestotliwosci wiec
# wykres jest dokładniejszy



np.save("sygnal_x.npy", x)
x_loaded = np.load("sygnal_x.npy")