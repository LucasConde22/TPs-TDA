"""
Complejidad:
    O(n*2^m), siendo n la cantidad de elementos y m la cantidad de bits necesarios para
    representar la capacidad de la mochila. Como se puede observar, se trata de un
    algoritmo pseudo-polinomial.

Ecuación de recurrencia:
    OPT(i, w) = max(vi + OPT(i, w - pi), OPT(i - 1, w))
"""
def mochila_multiple(elementos, capacidad):
    if len(elementos) == 0:
        return 0, []

    guardados = []
    for _ in range(len(elementos)):
        guardados.append([0] * (capacidad + 1))

    for j, (valor, peso) in enumerate(elementos):
        for i in range(capacidad + 1):
            nuevo = valor + guardados[j][i - peso] if peso <= i else 0
            anterior = guardados[j - 1][i] if j > 0 else 0
            guardados[j][i] = max(nuevo, anterior)
    
    return guardados[-1][-1], reconstruir_camino(elementos, guardados)

def reconstruir_camino(elementos, guardados): # O(n + w)
    camino = []
    fil, col = len(guardados) - 1, len(guardados[0]) - 1

    while guardados[fil][col] != 0:
        if fil > 0 and guardados[fil][col] == guardados[fil - 1][col]:
            fil -= 1
            continue
        camino.append(elementos[fil])
        col -= elementos[fil][1]
    
    return camino[::-1]

def main():
    print(mochila_multiple([(2, 3), (2, 1), (4, 3), (9,4)], 7))
    print(mochila_multiple([(2, 3)], 7))
    print(mochila_multiple([], 7))
    print(mochila_multiple([(30, 3), (14, 2)], 4))

if __name__ == "__main__":
    main()
