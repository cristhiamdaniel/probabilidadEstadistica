"""
import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros del problema
resistencias_posibles = np.array([20, 24, 28, 32, 36, 40])  # en MPa
probabilidades = np.array([0.05, 0.15, 0.3, 0.35, 0.10, 0.05])

# Calcular la distribución acumulativa
distribucion_acumulativa = np.cumsum(probabilidades)
resistencia_minima = 30
probabilidad_resistencia_minima = 1 - distribucion_acumulativa[np.searchsorted(resistencias_posibles, resistencia_minima, side="right")-1]

# Graficar la distribución acumulativa
plt.plot(resistencias_posibles, distribucion_acumulativa, '-o')
plt.plot([resistencia_minima, resistencia_minima], [0, 1], '--r')
plt.annotate("{:.1f}%".format(probabilidad_resistencia_minima*100), xy=(resistencia_minima, probabilidad_resistencia_minima), xytext=(resistencia_minima+1, probabilidad_resistencia_minima+0.1),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel("Resistencia a la compresión (MPa)")
plt.ylabel("Probabilidad acumulativa")
plt.show()

print("La probabilidad de que la resistencia sea mayor o igual a {} MPa es de {:.2f}%".format(resistencia_minima, probabilidad_resistencia_minima*100))
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros del problema
tasa_interes = 0.03
crecimiento_deseado = 0.05
rendimientos_posibles = np.array([-0.1, -0.05, 0, 0.05, 0.1])
probabilidades = np.array([0.1, 0.3, 0.3, 0.2, 0.1])

# Calcular la distribución acumulativa
distribucion_acumulativa = np.cumsum(probabilidades)
rendimiento_minimo = tasa_interes + crecimiento_deseado
probabilidad_rendimiento_minimo = 1 - distribucion_acumulativa[np.searchsorted(rendimientos_posibles, rendimiento_minimo, side="right")-1]

# Graficar la distribución acumulativa
plt.plot(rendimientos_posibles, distribucion_acumulativa, '-o')
plt.plot([rendimiento_minimo, rendimiento_minimo], [0, 1], '--r')
plt.annotate("{:.1f}%".format(probabilidad_rendimiento_minimo*100), xy=(rendimiento_minimo, probabilidad_rendimiento_minimo), xytext=(rendimiento_minimo+0.01, probabilidad_rendimiento_minimo+0.1),
                arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel("Rendimiento anual")
plt.ylabel("Probabilidad acumulativa")
plt.show()

print("La probabilidad de que el rendimiento sea mayor o igual a {:.2f}% es de {:.2f}%".format(rendimiento_minimo*100, probabilidad_rendimiento_minimo*100))

