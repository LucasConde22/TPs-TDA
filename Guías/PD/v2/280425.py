"""
Ecuación de recurrencia:
    OPT(i, P, W) = max(Vi + OPT(i - 1, P - Pi, W - Wi), OPT(i - 1, P, W))

Casos base:
    OPT(i, 0, W) = 0
    OPT(i, P, 0) = 0
"""

# Complejidad: O(N * P * W), pseudo-polinomial en función del largo P y W.
def mochila_3d(elementos, P, W): # elementos = (valor, precio, peso)
    matriz = [[[0] * (W + 1) for _ in range(P + 1)] for _ in range(len(elementos))]

    for i in range(len(elementos)):
        valor, precio, peso = elementos[i]
        for p in range(P + 1):
            for w in range(W + 1):
                
                anterior = 0 if i == 0 else matriz[i - 1][p][w]
                if i > 0 and precio <= p and peso <= w:
                    nuevo = valor + matriz[i - 1][p - precio][w - peso]
                else:
                    nuevo = 0

                matriz[i][p][w] = max(anterior, nuevo)
    
    return reconstruir(matriz, elementos)

# Complejidad: O(N)
def reconstruir(matriz, elementos):
    camino = []
    i, p, w = len(elementos) - 1, len(matriz[0]) - 1, len(matriz[0][0]) - 1

    while i >= 0 and matriz[i][p][w] != 0:
        if i == 0 or matriz[i][p][w] != matriz[i - 1][p][w]:
            camino.append(elementos[i])
            p -= elementos[i][1]
            w -= elementos[i][2]
        i -= 1

    return camino[::-1]

def main():

    productos = [(2, 10, 8), (8, 10, 8), (5, 2, 3), (1, 1, 1)]
    print(mochila_3d(productos, 11, 15))

if __name__ == "__main__":
    main()