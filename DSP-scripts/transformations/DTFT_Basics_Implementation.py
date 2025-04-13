import numpy as np
import matplotlib.pyplot as plt

# Dane
N = 100    # liczba próbek
fs = 1000  # częstotliwość próbkowania
ds = 1/fs  # krok próbkowania

x = np.load("sygnal_x.npy")
f1 = 125

# Generowanie macierzy transformacji DFT

W_N = np.exp(1j * 2 * np.pi / N)  # Podstawowy element DFT
A = np.zeros((N, N), dtype=complex)  # Tworzymy macierz N x N na liczby zespolone
for k in range(N):
    for n in range(N):
        A[k, n] = (1 / np.sqrt(N)) * W_N**(-k * n)

# Dyskretna transformata Fouriera (DFT)
X1 = np.dot(A, x)



# Zwiększenie rozdzielczości częstotliwości (dodanie 100 zer)
M = 100
xz = np.concatenate((x, np.zeros(M)))

# DTF dla X2
W_NM = np.exp(-1j * 2 * np.pi / (N + M))  # Podstawowy element zespolony dla (N+M)
A2 = np.zeros((N+M, N+M), dtype=complex)  # Macierz (N+M)x(N+M)

for k in range(N+M):
    for n in range(N+M):
        A2[k, n] = W_NM ** (k * n)

X2 = np.dot(A2,xz)/(N+M)

# szybsza alternatywa dajaca te same wyniki: X2 = np.fft.fft(xz) / (N + M)




# DtFT dla x ( DtFT to funkcja czestotliwosci wiec widmo jest ciagle a nie dyskretne jak przy DTF)
df = 0.1 #Bardziej dokładne widmo bo czestotliwosci są co 0.1Hz zamiast co 10 lub 5
f = np.arange(0, 1000, df)
X3 = np.zeros(len(f), dtype=complex)

for i in range(len(f)):
    current_f = f[i]  # Aktualna częstotliwość
    exponent = np.exp(-1j * 2 * np.pi * current_f * np.arange(N) / fs)  # e^(-j2πfn/fs)
    X3[i] = np.sum(x * exponent)  # Sumujemy wartości transformaty dla danej częstotliwości

# Normalizujemy wynik
X3 = X3 / N


# Skalowanie osi częstotliwości
fx1 = np.arange(N) * fs / N
fx2 = np.arange(N + M) * fs / (N + M)
fx3 = f

# Wykresy transformacji
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.plot(fx1, np.real(X1))
plt.title('X1 - DFT')
plt.xlabel('Częstotliwość [Hz]')

plt.subplot(1, 3, 2)
plt.plot(fx2, np.real(X2))
plt.title('X2 - 100 zer na końcu x')
plt.xlabel('Częstotliwość [Hz]')

plt.subplot(1, 3, 3)
plt.plot(fx3, np.real(X3))
plt.title('X3 - DtFT')
plt.xlabel('Częstotliwość [Hz]')
plt.show()

# Nakładanie widm
plt.figure(figsize=(10, 6))
plt.plot(fx1, np.abs(X1), 'b', label='X1 - DFT')
plt.plot(fx2, np.abs(X2), 'r', label='X2 - DFT z zerami')
plt.plot(fx3, np.abs(X3), 'g', label='X3 - DtFT')
plt.legend()
plt.title('Widma sygnałów nałożone na siebie')
plt.xlabel('Częstotliwość [Hz]')
plt.show()

# Rozszerzona analiza DtFT (-2000 Hz do 2000 Hz)
f = np.arange(-2000, 2000, df)
X3 = np.array([np.sum(x * np.exp(-1j * 2 * np.pi * fq * np.arange(N) / fs)) for fq in f]) / N
fx3 = f

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.plot(fx1, np.real(X1))
plt.title('X1 - DFT')
plt.xlabel('Częstotliwość [Hz]')

plt.subplot(1, 3, 2)
plt.plot(fx2, np.real(X2))
plt.title('X2 - 100 zer na końcu x')
plt.xlabel('Częstotliwość [Hz]')

plt.subplot(1, 3, 3)
plt.plot(fx3, np.real(X3))
plt.title('X3 - DtFT rozszerzone')
plt.xlabel('Częstotliwość [Hz]')
plt.show()

# Nakładanie widm dla rozszerzonego zakresu
plt.figure(figsize=(10, 6))
plt.plot(fx1, np.abs(X1), 'b', label='X1 - DFT')
plt.plot(fx2, np.abs(X2), 'r', label='X2 - DFT z zerami')
plt.plot(fx3, np.abs(X3), 'g', label='X3 - DtFT rozszerzone')
plt.legend()
plt.title('Widma sygnałów nałożone na siebie')
plt.xlabel('Częstotliwość [Hz]')
plt.show()

# fs = 1000 wiec fs/2 = 500. Zachodzi aliasing gdzie środkie odbicia
# lustrzanego jest 500Hz z warunku Nyquista2