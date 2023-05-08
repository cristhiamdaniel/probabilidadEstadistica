import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

# Probabilidad de falla del componente del puente (éxito)
p = 0.01

# Crear una instancia de la distribución de Bernoulli
dist = bernoulli(p)

# Posibles resultados (0: no falla, 1: falla)
salidas = [0, 1]

# Calcular la probabilidad de masa (PMF) de cada resultado
PMF = dist.pmf(salidas)

# Calcular la función de distribución acumulativa (CDF)
CDF = dist.cdf(salidas)

# Graficar la PMF y la CDF
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.bar(salidas, PMF)
plt.xlabel('Resultado')
plt.ylabel('Probabilidad')
plt.title('Función de Masa de Probabilidad')
plt.subplot(1, 2, 2)
plt.bar(salidas, CDF)
plt.xlabel('Resultado')
plt.ylabel('Probabilidad')
plt.title('Función de Distribución Acumulativa')
plt.show()