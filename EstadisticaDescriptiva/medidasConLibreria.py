import statistics as stats
from collections import Counter
import numpy as np

# Ejemplo de uso con la lista de precios de terrenos
precios_terrenos = [300, 750, 350, 550, 800, 800, 500, 350, 950, 1500]

media = stats.mean(precios_terrenos)
print("La media es:", media)

mediana = stats.median(precios_terrenos)
print("La mediana es:", mediana)

frecuencias = Counter(precios_terrenos)
max_frecuencia = max(frecuencias.values())

modas = [valor for valor, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]

if len(modas) == 1:
    print("La moda es:", modas[0])
else:
    print("Las modas son:", modas)

media_geom = stats.geometric_mean(precios_terrenos)
print("La media geom?trica es:", media_geom)

media_arm = stats.harmonic_mean(precios_terrenos)
print("La media arm?nica es:", media_arm)

cuartiles = np.percentile(precios_terrenos, [25, 50, 75])
print("Los cuartiles son:", cuartiles)
