import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Załaduj dane z pliku

mat = scipy.io.loadmat('ADSL.mat')
modulo = (444 % 16) + 1
x = mat[f'x_{modulo}'].flatten()

# Prędkość transmisji przyjąłem sobie że jest rowna 20Mb/s
# x ma długość 4353 wartosci kalsy double czyli w pythonie ma 64 bity
# wychodzi że sygnał ma 278 592 bitow


# Parametry sygnału

T = 278592 / 20e6  # 0.01392 s
fs = 1 / T  # Około 71.78 Hz - zaokrąglijmy do 72Hz żeby można było łątwo podzielić na 2
# (nasze fs to czestotliwość Nyquista a musi ono byc dwa razy wieksze niz najwieksza czestotliwosc w sygnale)


N = 512  # Długość ramki
M = 32  # Długość prefiksu
K = 8  # Liczba ramek

fs = 2048

# Wyszukiwanie ramek

ramki = []
for m in range(K):
    ramki.append(x[m * (N + M) + 1 + M:  m * (N + M) + 1 + M + N])

# Tworzenie wykresów

fig, axs = plt.subplots(4, 2, figsize=(15, 6))  # Tworzymy siatkę wykresów 3x2
fig.suptitle('Widmo częstotliwościowe poszczególnych ramek')

for i, r in enumerate(ramki):
    X = np.fft.fft(r, N) / N  # FFT

    threshold = max(
        np.abs(X[:N // 2])) / 10  # Próg - wybieramy te częstotliwości, które mają min. 10% mocy max wartości

    freq = np.fft.fftfreq(N, 1 / (fs / 2))[:N // 2]  # Pierwsza połowa częstotliwości

    Amplituda = np.abs(X[:N // 2])  # Amplituda

    # Znalezienie indeksów, gdzie amplituda przekracza próg
    harmoniczne = freq[Amplituda > threshold]

    print(f"Ramka {i + 1}: Wykryte harmoniczne {harmoniczne.round(2)} Hz")

    # Jako że nigdzie nie ma informacji o fs to nie wiemy o wartości częstotliwości
    # Zakładamy więc że jest to f = (fs/2) = 36

    # i - indeks, r - zawartosc indeksu (ramka)
    X = np.fft.fft(r, N) / N  # r - ramka, N - ilosc punktow na dziedzinie czestotliwosci
    freq = np.fft.fftfreq(N, 1 / (fs / 2))[
           :N // 2]  # FFT zwraca wartości dla wielu częstotliwości, ale same wartości FFT to tylko amplitudy.
    # Aby wiedzieć, jaka częstotliwość odpowiada danej wartości FFT, musimy użyć fftfreq()

    # Pierwsza połowa (0 do N/2) – rosnące częstotliwości.
    # Druga połowa (N/2 do N-1) – ujemne częstotliwości (dla sygnałów zespolonych).
    # Ale ponieważ analizujemy rzeczywiste sygnały, zwykle bierzemy tylko pierwszą połowę wartości ([:N//2])
    axs.flatten()[i].plot(freq, np.abs(X[:N // 2]))  # Rysujemy widmo
    # Tablica axs jest dwuwymiarowa (4x2). Jeśli chcemy iterować po wszystkich wykresach jako po jednej liście, musimy ją "spłaszczyć"
    axs.flatten()[i].set_title(f'Ramka {i + 1}')
    axs.flatten()[i].set_xlabel('Częstotliwość [Hz]')
    axs.flatten()[i].set_ylabel('Amplituda')
    axs.flatten()[i].grid()

plt.tight_layout()
plt.show()
