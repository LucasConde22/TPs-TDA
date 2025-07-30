"""
Algoritmo explicado a la perfección:
https://www.youtube.com/watch?v=cJ21moQpofY

Complejidad: O(N*W), siendo N la cantidad de elementos y W el peso máximo.
"""

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    matriz = []
    for _ in range(len(elementos) + 1):
        matriz.append([])
        for _ in range(W + 1):
            matriz[-1].append(0)
    
    for i, elemento in enumerate(elementos):
        valor, peso = elemento
        for w in range(W + 1):
            sin_elemento = matriz[i][w] # Sería el casillero una fila antes y en = columna.
            if w - peso >= 0:
                con_elemento = matriz[i][max(w - peso, 0)] + valor # Sería lo que tiene el último casillero compatible sin el elemento + el elemento.
            else:
                con_elemento = sin_elemento
            matriz[i+1][w] = max(sin_elemento, con_elemento)

    return reconstruir_camino(elementos, matriz)

def reconstruir_camino(elementos, matriz):
    camino = []
    fil, col = len(matriz) - 1, len(matriz[0]) - 1

    while matriz[fil][col] != 0:
        if matriz[fil][col] != matriz[fil - 1][col]: # Si es distinto al de arriba, lo agrego a la solución y paso al "casillero anterior en diagonal".
            camino.append(elementos[fil - 1])
            fil, col = fil - 1, col - elementos[fil - 1][1]
        else: # Sino, paso al elemento de arriba.
            fil -= 1
    
    return camino[::-1]

def main():
    print(mochila([(9, 11), (2, 1), (8, 6), (1, 1), (5, 5), (4, 15)], 12))
    print(mochila([], 12))
    #print(mochila([(100, 20), (200, 35), (80, 100), (120, 100), (100, 21), (10, 5), (200, 200), (150, 150), (1, 99)], 200))
    print(mochila([(1, 1), (2, 1), (3, 1)], 2))
    print(mochila([(1, 2), (2, 3), (5, 5), (9, 8)], 11))

    elementos = [
    (58, 700),
    (15, 600),
    (51, 1200),
    (31, 200),
    (13, 1200),
    (89, 1500),
    (19, 900),
    (4, 1200),
    (75, 800),
    (50, 800)
    ]
    W = 1500
    print(mochila(elementos, W))

if __name__ == "__main__":
    main()