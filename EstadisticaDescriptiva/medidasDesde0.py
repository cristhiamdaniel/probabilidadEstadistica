import math

def calcular_media(valores):
    media = sum(valores) / len(valores)
    return media

def calcular_mediana(valores):
    ordenados = sorted(valores)
    mediana = ordenados[len(valores) // 2]
    return mediana

def calcular_moda(valores):
    frecuencias = {}
    for x in valores:
        frecuencias[x] = frecuencias.get(x, 0) + 1
    modas = [x for x in frecuencias if frecuencias[x] == max(frecuencias.values())]
    if len(modas) == 1:
        return modas[0]
    else:
        return modas

def calcular_media_geometrica(valores):
    producto = 1
    for x in valores:
        producto *= x
    media_geom = producto ** (1 / len(valores))
    return media_geom

def calcular_media_armonica(valores):
    media_arm = len(valores) / sum(1 / x for x in valores)
    return media_arm

def calcular_cuartiles(valores):
    n = len(valores)
    ordenados = sorted(valores)
    q1 = ordenados[int(0.25 * n)]
    q2 = ordenados[int(0.5 * n)]
    q3 = ordenados[int(0.75 * n)]
    cuartiles = [q1, q2, q3]
    return cuartiles

def calcular_varianza(valores):
    media = calcular_media(valores)
    varianza = sum((x - media) ** 2 for x in valores) / len(valores)
    return varianza

def calcular_desviacion_estandar(valores):
    desviacion_estandar = math.sqrt(calcular_varianza(valores))
    return desviacion_estandar


# Ejemplo de uso con la lista de precios de terrenos
precios_terrenos = [300, 750, 350, 550, 800, 800, 500, 350, 950, 1500]

media = calcular_media(precios_terrenos)
print("La media es:", media)

mediana = calcular_mediana(precios_terrenos)
print("La mediana es:", mediana)

moda = calcular_moda(precios_terrenos)
if isinstance(moda, list):
    print("Las modas son:", moda)
else:
    print("La moda es:", moda)

media_geom = calcular_media_geometrica(precios_terrenos)
print("La media geom?trica es:", media_geom)

media_arm = calcular_media_armonica(precios_terrenos)
print("La media arm?nica es:", media_arm)

cuartiles = calcular_cuartiles(precios_terrenos)
print("Los cuartiles son:", cuartiles)

varianza = calcular_varianza(precios_terrenos)
print("La varianza es:", varianza)

desviacion_estandar = calcular_desviacion_estandar(precios_terrenos)
print("La desviaci?n est?ndar es:", desviacion_estandar)