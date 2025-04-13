import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import hamming, blackman, chebwin

# Parametry sygnału
N = 1000  # liczba próbek
fs = 1000  # częstotliwość próbkowania
T = N/fs
f1, f2 = 100, 125
A1, A2 = 1, 0.0001
p1, p2 = np.pi / 7, np.pi / 11
t = np.linspace(0, T, N, endpoint=False)
x = A1 * np.cos(2 * np.pi * f1 * t + p1) + A2 * np.cos(2 * np.pi * f2 * t + p2)



# Obliczanie DtFT
f = np.arange(0, 500.1, 0.1)
X = np.zeros(len(f), dtype=complex)


for i in range(len(f)):
    current_f = f[i]  # Aktualna częstotliwość
    exponent = np.exp(-1j * 2 * np.pi * current_f * np.arange(N) / fs)  # e^(-j2πfn/fs)
    X[i] = np.sum(x * exponent)  # Sumujemy wartości transformaty dla danej częstotliwości
X = X/N # (DtFT) sumuje N próbek sygnału, bez normalizacji amplituda widma będzie proporcjonalna do liczby próbek N

# Rysowanie widma
plt.figure(figsize=(10, 5))
plt.plot(f, np.abs(X), label='Widmo')
plt.title('Moduł DtFT sygnału')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.legend()
plt.grid()
plt.show()

# Okna
windows = {
    "Prostokątne": np.ones(N),
    "Hamming": hamming(N),
    "Blackman": blackman(N),
    "Czebyszewa 100 dB": chebwin(N, 100),
    "Czebyszewa 120 dB": chebwin(N, 120),
}

# Obliczanie i rysowanie widm dla różnych okien
plt.figure(figsize=(10, 5))
for name, win in windows.items():
    x_win = x * win
    X_win = np.array([np.sum(x_win * np.exp(-1j * 2 * np.pi * freq * np.arange(N) / fs)) for freq in f]) / N
    plt.plot(f, np.abs(X_win), label=name)

plt.title('Widma sygnału dla różnych okien')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.legend()
plt.grid()
plt.show()





# Powtórzenie zadania dla N=1000 i różnych okien Czebyszewa
N = 1000
T = N / fs
# Częstotliwości i amplitudy
f1, f2 = 100, 125
A1, A2 = 1, 0.0001
p1, p2 = np.pi / 7, np.pi / 11
t = np.linspace(0, T, N, endpoint=False)
x = A1 * np.cos(2 * np.pi * f1 * t + p1) + A2 * np.cos(2 * np.pi * f2 * t + p2)

windows_cheb = {
    "Czebyszewa 100 dB": chebwin(N, 100),
    "Czebyszewa 200 dB": chebwin(N, 200),
}

plt.figure(figsize=(10, 5))
for name, win in windows_cheb.items():
    x_win = x * win
    X_win = np.zeros(len(f), dtype=complex)

    for i in range(len(f)):
        current_f = f[i]  # Aktualna częstotliwość
        exponent = np.exp(-1j * 2 * np.pi * current_f * np.arange(N) / fs)  # e^(-j2πfn/fs)
        X_win[i] = np.sum(x_win * exponent)  # Sumujemy wartości transformaty dla danej częstotliwości
    X_win = X_win / N  # (DtFT) sumuje N próbek sygnału, bez normalizacji amplituda widma będzie proporcjonalna do liczby próbek N

    plt.plot(f, np.abs(X_win), label=name)

plt.title('Widma sygnału dla różnych okien Czebyszewa (N=1000)')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.legend()
plt.grid()
plt.show()


# Wysoką amplitude na wykresie widma widać tylko przy 100 Hz pomimo że mamy dwa
# sygnay tzn. 100 Hz i 125Hz dlatego że częstotliwości w DTF są dyskertne
# Przy 100 próbkach i fs = 1000 Hz częstotliwości analizowane w DTF
# są rozmieszczone co fs/N = 10 Hz a niestety zachodzi aliasing wewnętrzny
# to na wykresie nie zauwazymy tej czętotliwości. 125Hz wpada dokładnie między
# próbke 120Hz a 130Hz

# Matematycznie ucięcie sygnału w dziedzinie czasu odpowiada splotowi jego widma
# z widmem funkcji prostokątnej.

# A widmo funkcji prostokątnej to funkcja sinc (sinus cardinalis),
# która ma silne listki boczne

# Z tego powodu energia sygnału, która powinna być skupiona w jednym punkcie
# w widmie, zaczyna się rozlewać, powodując wyciek widmowy.

# Dzięki oknom wartości sygnału na końcach są stopniowo zmniejszane, co powoduje,
# że widmo ma mniejsze listki boczne, a wyciek jest znacznie ograniczony.


# Rysowanie samych okien
plt.figure(figsize=(10, 6))

t = np.arange(N)  # Oś czasu (próbki)

for name, win in windows.items():
    plt.plot(t, win, label=name)

plt.title("Porównanie różnych okien")
plt.xlabel("Numer próbki")
plt.ylabel("Wartość okna")
plt.legend()
plt.grid()
plt.show()

