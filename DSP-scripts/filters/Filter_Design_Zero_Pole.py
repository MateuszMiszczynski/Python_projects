import numpy as np
import matplotlib.pyplot as plt


# Zera i bieguny transmitancji
z = np.array([-1j*5, 1j*5, -1j*15, 1j*15])
p = np.array([-0.5 - 1j*9.5, -0.5 + 1j*9.5,
              -1 + 1j*10, -1 - 1j*10,
              -0.5 + 1j*10.5, -0.5 - 1j*10.5])

# Przestrzeń częstotliwości (s = jω)
w = np.arange(0.1, 20.1, 0.1)
jw = 1j * w

# Obliczenie wielomianów z zer i biegunów
bm = np.poly(z)  # wielomian licznikowy
an = np.poly(p)  # wielomian mianownikowy


plt.figure("Zera i bieguny")
plt.plot(np.real(z), np.imag(z), 'ro', label='Zera transmitancji')
plt.plot(np.real(p), np.imag(p), 'b*', label='Bieguny transmitancji')
plt.title('Zera i bieguny transmitancji')
plt.xlabel('Re')
plt.xlim(-2,1)
plt.ylabel('Im')
plt.grid(True)
plt.legend()
plt.show()



# Obliczenie wartości transmitancji H(jw)
H = np.polyval(bm, jw) / np.polyval(an, jw)
Hlog = 20 * np.log10(np.abs(H)+ 1e-12)

# Wykresy
plt.figure("Charakterystyka amplitudowo-częstotliwościowa")

# Skala liniowa
plt.subplot(1, 2, 1)
plt.plot(w, np.abs(H), 'b')
plt.title('Skala liniowa |H(jω)|')
plt.xlabel('ω [rad/s]')
plt.ylabel('|H(jω)|')
plt.grid(True)

# Skala decybelowa
plt.subplot(1, 2, 2)
plt.plot(w, Hlog, 'b')
plt.title('Skala decybelowa 20*log10|H(jω)|')
plt.xlabel('ω [rad/s]')
plt.ylabel('|H(jω)| [dB]')
plt.grid(True)

plt.tight_layout()
plt.show()



H2 = H / np.max(np.abs(H))  # normalizacja
Hlog2 = 20 * np.log10(np.abs(H2)+ 1e-12)

plt.figure("Charakterystyka amplitudowo-częstotliwościowa - modyfikacja")

# Skala liniowa po normalizacji
plt.subplot(1, 2, 1)
plt.plot(w, np.abs(H2), 'b')
plt.title('Skala liniowa |H(jω)| - znormalizowana')
plt.xlabel('ω [rad/s]')
plt.ylabel('|H(jω)|')
plt.ylim([0, 2.5])
plt.grid(True)

# Skala decybelowa po normalizacji
plt.subplot(1, 2, 2)
plt.plot(w, Hlog2, 'b')
plt.axhline(y=-52.5, color='k', linestyle='-')  # linia referencyjna
plt.title('Skala decybelowa 20*log10|H(jω)|')
plt.xlabel('ω [rad/s]')
plt.ylabel('|H(jω)| [dB]')
plt.grid(True)

plt.tight_layout()
plt.show()



# Obliczenie fazy
Hp = np.arctan(np.imag(H) / np.real(H))

plt.figure("Charakterystyka fazowo-częstotliwościowa")
plt.stem(w, Hp, basefmt=" ")
plt.title('Charakterystyka fazowo-częstotliwościowa')
plt.xlabel('ω [rad/s]')
plt.ylabel('Faza [rad]')
plt.grid(True)
plt.show()

