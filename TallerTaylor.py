import matplotlib.pyplot as plt
import numpy as np


def taylor_ln(x, n):
  """Polinomio de Taylor de grado n de ln(x) alrededor de x0=1"""
  suma = 0
  for k in range(1, n + 1):
    suma += ((-1) ** (k + 1)) * ((x - 1) ** k) / k
  return suma

print(f"P_3(1.5) = {taylor_ln(1.5, 3):.6f}")
print(f"P_10(1.5) = {taylor_ln(1.5, 10):.6f}")
print(f"P_10(2.5) = {taylor_ln(2.5, 10):.6f}")

x_vals = np.linspace(0.1, 3, 400)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, np.log(x_vals), "k-", linewidth=2, label="ln(x)")
for n in [1, 2, 3, 6]:
  plt.plot(x_vals, taylor_ln(x_vals, n), "--", label=f"$P_{n}(x)$")

plt.plot(1, 0, "ro", label="Centro (1, 0)")
plt.ylim(-3, 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Aproximación de ln(x) mediante polinomios de Taylor en $x_0 = 1$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("grafica1.png", dpi=300)
plt.show()

grados = np.arange(1, 31)
err_15 = [abs(np.log(1.5) - taylor_ln(1.5, n)) for n in grados]
err_25 = [abs(np.log(2.5) - taylor_ln(2.5, n)) for n in grados]
cota_15 = [(0.5 ** (n + 1)) / (n + 1) for n in grados]

plt.figure(figsize=(8, 5))
plt.semilogy(grados, err_15, "o-", label="Error real en $x = 1.5$")
plt.semilogy(grados, err_25, "s-", label="Error real en $x = 2.5$")
plt.semilogy(grados, cota_15, "k--", label="Cota del error en $x = 1.5$")

plt.xlabel("Grado del polinomio (n)")
plt.ylabel("Error absoluto (escala logarítmica)")
plt.title("Evolución del error de Taylor para ln(x)")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.savefig("grafica2.png", dpi=300)
plt.show()
