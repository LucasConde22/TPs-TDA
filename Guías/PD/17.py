from math import isqrt

"""
Complejidad: 
            O(2^m), con m igual a la cantidad de bits necesarios para representar n. Se
            trata de un algoritmo pseudo-polinomial.

Ecuación de recurrecia:
            OPT(i) = min(1 + cuadrados[i - j^2] para todo j perteneciente a [1, raiz_entera(i)])

"""
def terminos(n):
    cuadrados = [i for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, isqrt(i) + 1):
            cuadrados[i] =  min(cuadrados[i], 1 + cuadrados[i - j**2])

    return cuadrados[-1]

"""
Solución Greedy, no óptima (pasa las pruebas, pero no debería):
"""
def terminos_greedy(n):
    cuadrados = [0]

    for i in range(1, n + 1):
            cuadrados.append(1 + cuadrados[i - isqrt(i)**2])

    return cuadrados[-1]


def main():
    print(terminos(5))
    print(terminos(4))
    print(terminos(9))
    print(terminos(3))
    print(terminos(10))
    print(terminos(1))
    print(terminos(0))
    print(terminos(12))

if __name__ == "__main__":
    main()