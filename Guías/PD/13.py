# Complejidad: O(N*W), siendo N la cantidad de elems. en P y W el largo de la mesa.
def bodegon_dinamico(P, W):
    if len(P) == 0:
        return []

    matriz = []

    for fil in range(len(P)):
        matriz.append([])
        
        for col in range(W + 1):
            anterior = matriz[fil - 1][col] if fil > 0 else 0 # Máximo sin el elem actual
            if P[fil] <= col:
                actual = P[fil] # Suma actual
                if fil > 0 and P[fil] < col:
                    actual += matriz[fil - 1][col - P[fil]] # Sumo "el restante" al actual
            else:
                actual = 0
            matriz[fil].append(max(anterior, actual))
        
        if matriz[-1][-1] >= W: # Si ya llegué, recorto
            break

    # Reconstrucción (debería estar en una funcióon aparte):
    fil, col = len(matriz) - 1, len(matriz[0]) - 1
    elegidos = []

    while fil >= 0 and col >= 0 and matriz[fil][col] != 0:
        if fil > 0 and matriz[fil][col] == matriz[fil - 1][col]:
            fil -= 1
            continue
        elegidos.append(P[fil])
        fil, col = fil - 1, col - P[fil]

    return elegidos[::-1]

def main():
    print(bodegon_dinamico([], 11))
    print(bodegon_dinamico([5], 11))
    print(bodegon_dinamico([5, 4, 6, 10], 11))
    print(bodegon_dinamico([30, 10, 4, 20, 15], 28))

if __name__ == "__main__":
    main()
