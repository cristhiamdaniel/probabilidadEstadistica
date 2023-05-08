import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Función de densidad de probabilidad
def f(y):
    return (1/4) * np.exp(-y/4) if y >= 0 else 0

# Función de distribución acumulativa
def F(y):
    return (-1) * np.exp(-y/4) + 1

# Probabilidad de que no requiera reparación mayor antes del sexto año
P_Y_greater_6 = 1 - F(6)

# Probabilidad de que requiera reparación mayor durante el primer año
P_Y_less_equal_1 = F(1)

# Graficar la función de densidad de probabilidad
y_values = np.linspace(0, 10, 1000)
f_values = [f(y) for y in y_values]
plt.plot(y_values, f_values, label="f(y)")

# Área bajo la curva para P(Y ≤ 1)
y_fill_1 = np.linspace(0, 1, 100)
f_fill_1 = [f(y) for y in y_fill_1]
plt.fill_between(y_fill_1, f_fill_1, alpha=0.3, label=f"P(Y ≤ 1) ≈ {P_Y_less_equal_1:.4f}")

# Área bajo la curva para P(Y > 6)
y_fill_2 = np.linspace(6, 10, 100)
f_fill_2 = [f(y) for y in y_fill_2]
plt.fill_between(y_fill_2, f_fill_2, alpha=0.3, label=f"P(Y > 6) ≈ {P_Y_greater_6:.4f}")

plt.title("Función de densidad de probabilidad f(y)")
plt.xlabel("Tiempo (años)")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()

print(f"P(Y > 6) ≈ {P_Y_greater_6:.4f}")
print(f"P(Y ≤ 1) ≈ {P_Y_less_equal_1:.4f}")
