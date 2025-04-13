import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction as TF, impulse, step

# Parametry
w3dB = 2 * np.pi * 100
w = np.arange(0.1, 2000, 0.1)
f = w / (2 * np.pi)
orders = [2, 4, 6, 8]
colors = ['r', 'b', 'g', 'k']
Hs = []
Hlogs = []
angles = []

plt.figure("Charakterystyki amplitudowe")
plt.subplot(1, 2, 1)
for i, N in enumerate(orders):
    poles = [w3dB * np.exp(1j * (np.pi/2 + (0.5 * np.pi / N) + (k * np.pi / N))) for k in range(N)]
    bm = np.array([1.0])  # Brak zer
    an = np.poly(poles)
    H = np.polyval(bm, 1j * w) / np.polyval(an, 1j * w)
    H /= np.max(np.abs(H))
    Hlog = 20 * np.log10(np.abs(H))
    angle_H = np.angle(H)
    Hs.append(np.abs(H))
    Hlogs.append(Hlog)
    angles.append(angle_H)
    plt.plot(f, np.abs(H), colors[i], label=f'N={N}')

plt.title('Skala liniowa |H(jω)|')
plt.xlabel('f [Hz]')
plt.ylabel('|H(jω)|')
plt.legend()
plt.xlim([0, f[-1]])

# Skala logarytmiczna
plt.subplot(1, 2, 2)
for i in range(len(orders)):
    plt.semilogx(f, Hlogs[i], colors[i], label=f'N={orders[i]}')
plt.title('Skala decybelowa 20*log10(|H(jω)|)')
plt.xlabel('f [Hz]')
plt.ylabel('H [dB]')
plt.legend()
plt.tight_layout()
plt.show()

# Charakterystyka fazowa
plt.figure("Charakterystyka fazowa")
for i in range(len(orders)):
    plt.plot(f, angles[i], colors[i], label=f'N={orders[i]}')
plt.title('Charakterystyka fazowo-częstotliwościowa')
plt.xlabel('f [Hz]')
plt.ylabel('Faza [rad]')
plt.legend()
plt.xlim([0, f[-1]])
plt.grid(True)
plt.show()

# Odpowiedź impulsowa i skokowa dla N=4
N = 4
poles = [w3dB * np.exp(1j * (np.pi/2 + (0.5 * np.pi / N) + (k * np.pi / N))) for k in range(N)]
bm = np.array([1.0])
an = np.poly(poles)
sys = TF(bm, an)

# Odpowiedź impulsowa
t_imp, y_imp = impulse(sys)
plt.figure("Odpowiedź impulsowa filtru N=4")
plt.plot(t_imp, y_imp)
plt.title("Odpowiedź impulsowa")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.grid(True)
plt.show()

# Odpowiedź skokowa
t_step, y_step = step(sys)
plt.figure("Odpowiedź skokowa filtru N=4")
plt.plot(t_step, y_step)
plt.title("Odpowiedź na skok jednostkowy")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.grid(True)
plt.show()
