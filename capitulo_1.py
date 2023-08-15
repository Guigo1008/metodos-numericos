import math
import numpy as np

# Algorítmo 1:

def algoritmo_1(N):
    n = int(math.log2(N)) + 1
    P = N
    a = np.array()

    for i in range(n):
        M = P/2.
        P = int(M)
        # Isso é igual a fazer P%2 (que existe em python)
        a.append(int(2*(M-P)))

    return a


def teste_algoritmo_1(lista_bin):
    n = 0
    for i in range(len(lista_bin)):
        n += lista_bin[i] * 2**i

    return n


""" lista_binaria = algoritmo_1(10)
print(lista_binaria)
print(teste_algoritmo_1(lista_binaria)) """


# Algoritmo 2
def algoritmo_2(N):
    n = 0
    pot = 1
    while pot <= N:
        n = n + 1
        pot = 2 * pot
    n = n - 1

    pot = 2**n
    M = N - pot
    a = np.zeros((n+1))
    a[n] = 1.

    for i in range(n):
        pot = pot/2
        if M < pot:
            a[n-1] = 0.
        else:
            a[n-1] = 1.
            M = M - pot

    return a

print(algoritmo_2(3))


