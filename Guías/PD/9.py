# Complejidad O(N*V), siendo N la cantidad de elementos y V el número a maximizar.
def subset_sum(elementos, v):
    matriz = []
    for _ in range(len(elementos) + 1): # Agrego una fila inicial con el elemento 0 para mayor comodidad en el manejo de índices.
        matriz.append([])
        for _ in range(v + 1): # Agrego una columna inicial con el número 0 para mayor comodidad en el manejo de índices.
            matriz[-1].append(0)

    for i in range(1, len(elementos) + 1):
        for j in range(v + 1):
            if elementos[i - 1] > j:
                matriz[i][j] = matriz[i-1][j] # Si el actual se pasa, el mejor va a ser el anterior.
            else:
                matriz[i][j] = max(matriz[i-1][j], elementos[i - 1] + matriz[i - 1][j - elementos[i-1]]) # El mejor va a ser el que maximize entre el anterior y el nuevo + lo que sobre.
    
    return reconstruir_camino(elementos, matriz)

def reconstruir_camino(elementos, matriz):
    fil, col = len(matriz) - 1, len(matriz[0]) - 1
    usados = []

    while matriz[fil][col] != 0:
        if matriz[fil][col] == matriz[fil-1][col]:
            fil -= 1
            continue
        usados.append(elementos[fil - 1])
        fil, col = fil - 1, col - elementos[fil - 1]
    
    return usados[::-1]


def main():
    print(subset_sum([], 11))
    print(subset_sum([2], 11))
    print(subset_sum([2, 4], 11))
    print(subset_sum([2, 4, 7], 11))
    print(subset_sum([2, 4, 7], 12))
    print(subset_sum([2, 4, 7], 0))
    print(subset_sum([2, 4, 7], 1))
    print(subset_sum([1, 5, 9, 10, 9], 30))

if __name__ == "__main__":
    main()
