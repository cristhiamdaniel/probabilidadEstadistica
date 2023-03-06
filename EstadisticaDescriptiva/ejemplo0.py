'''
Un problema de contexto real para estudiantes de ingenier?a financiera en el que tengan que calcular medidas de tendencia central para 2 millones de datos podr?a ser el siguiente:

Un banco tiene una base de datos con informaci?n sobre los pr?stamos que ha otorgado en los ?ltimos cinco a?os. La base de datos contiene 2 millones de registros con informaci?n sobre el monto del pr?stamo, la tasa de inter?s, el plazo del pr?stamo, el tipo de garant?a, entre otros datos.

El banco desea analizar la informaci?n para determinar cu?l es el monto promedio de los pr?stamos otorgados, as? como el inter?s promedio que ha cobrado en los ?ltimos cinco a?os. Para ello, se requiere calcular las medidas de tendencia central, como la media y la mediana, para el monto del pr?stamo y la tasa de inter?s.

El an?lisis de esta informaci?n permitir? al banco tomar decisiones estrat?gicas para mejorar sus pol?ticas de otorgamiento de pr?stamos y evaluar el desempe?o de su cartera de pr?stamos en los ?ltimos a?os. Sin embargo, debido al gran volumen de datos, el c?lculo de estas medidas de tendencia central podr?a resultar un proceso tedioso y complejo para los estudiantes de ingenier?a financiera encargados de realizar este an?lisis.
'''

import random
import numpy as np

# Generar 2 millones de datos aleatorios entre 0 y 10000
data = [random.randint(0, 10000) for _ in range(2000000)]

# Calcular la media de los datos
mean = np.mean(data)
print(f"La media es: {mean}")

# Calcular la mediana de los datos
median = np.median(data)
print(f"La mediana es: {median}")
