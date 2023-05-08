"""
Programa para calcular la probabilidad condicional

P(A|B) = P(A and B) / P(B)

donde A y B son eventos aleatorios


"""

from random import random

def prob_condicional(A, B, N):
    """
    Calcula la probabilidad condicional

    P(A|B) = P(A and B) / P(B)

    donde A y B son eventos aleatorios

    Parametros:
    A (float): probabilidad del evento A
    B (float): probabilidad del evento B
    N (int): numero de iteraciones

    Retorna:
    float: probabilidad condicional
    """

    # Definimos las variables
    A_and_B = 0
    B = 0

    # Iteramos N veces
    for i in range(N):
        # Generamos un numero aleatorio
        r = random()

        # Verificamos si el numero generado es menor que la probabilidad del evento A
        if r < A:
            # Incrementamos el contador de A
            A_and_B += 1

        # Verificamos si el numero generado es menor que la probabilidad del evento B
        if r < B:
            # Incrementamos el contador de B
            B += 1

    # Calculamos la probabilidad condicional
    prob_cond = A_and_B / B

    # Retornamos el resultado
    return prob_cond

def main():
    # Definimos los eventos A y B
    A = 0.3
    B = 0.5

    # Definimos el numero de iteraciones
    N = 100000

    # Calculamos la probabilidad condicional
    prob_cond = prob_condicional(A, B, N)

    # Imprimimos el resultado
    print("La probabilidad condicional es: ", prob_cond)

if __name__ == "__main__":
    main()
