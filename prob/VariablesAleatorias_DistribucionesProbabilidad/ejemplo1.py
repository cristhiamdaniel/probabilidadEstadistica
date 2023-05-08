"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (1/2000) * np.exp(-x/2000) if x >= 0 else 0

x_vals = np.linspace(0, 4000, 1000)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label="Función de densidad de probabilidad f(x)")

# Rellenar el área bajo la curva para X ≤ 2000
x_fill = np.linspace(0, 2000, 1000)
y_fill = [f(x) for x in x_fill]
plt.fill_between(x_fill, y_fill, alpha=0.3, label="P(X ≤ 2000)")

plt.xlabel("Horas (x)")
plt.ylabel("f(x)")
plt.title("Función de densidad de probabilidad y área bajo la curva")

# Calcular P(X ≤ 2000)
probabilidad = 1 - np.exp(-2000/2000)

# Agregar el valor del área bajo la curva al gráfico
plt.text(1200, 0.0002, f"P(X ≤ 2000) = {probabilidad:.4f}", fontsize=12, color='blue')

plt.legend()
plt.grid()
plt.show()
"""

"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3 * x**(-4) if x > 1 else 0

x_vals = np.linspace(0, 10, 1000)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label="Función de densidad de probabilidad f(x)")

# Rellenar el área bajo la curva para X > 4
x_fill = np.linspace(4, 10, 1000)
y_fill = [f(x) for x in x_fill]
plt.fill_between(x_fill, y_fill, alpha=0.3, label="P(X > 4)")

plt.xlabel("Tamaño de partícula (x, en micras)")
plt.ylabel("f(x)")
plt.title("Función de densidad de probabilidad y área bajo la curva")

# Calcular P(X > 4)
probabilidad = 1 - (1 - 4**(-3))

# Agregar el valor del área bajo la curva al gráfico
plt.text(4.5, 0.01, f"P(X > 4) = {probabilidad:.4f}", fontsize=12, color='blue')

plt.legend()
plt.grid()
#plt.ylim(0, 0.05)
plt.show()
"""

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
y_fill = np.linspace(0, 1, 100)
f_fill = [f(y) for y in y_fill]
plt.fill_between(y_fill, f_fill, alpha=0.3, label=f"P(Y ≤ 1) ≈ {P_Y_less_equal_1:.4f}")

plt.title("Función de densidad de probabilidad f(y)")
plt.xlabel("Tiempo (años)")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()

print(f"P(Y > 6) ≈ {P_Y_greater_6:.4f}")
print(f"P(Y ≤ 1) ≈ {P_Y_less_equal_1:.4f}")

