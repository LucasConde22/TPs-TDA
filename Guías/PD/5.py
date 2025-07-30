# Solución top-down:
# Complejidad temporal y espacial: O(N * M)
def laberinto2(matriz):
    if len(matriz) == 0:
        return 0
    return _laberinto(len(matriz) - 1, len(matriz[0]) - 1, {}, matriz)
    
def _laberinto(fil, col, memoization, matriz):
    if (fil, col) in memoization:
        return memoization[(fil, col)]

    if fil == 0 and col == 0:
        memoization[(0, 0)] = matriz[0][0]
        return matriz[0][0]
    
    if fil == 0:
        memoization[(0, col)] = _laberinto(0, col - 1, memoization, matriz) + matriz[0][col]
        return memoization[(0, col)]
    
    if col == 0:
        memoization[(fil, 0)] = _laberinto(fil - 1, 0, memoization, matriz) + matriz[fil][0]
        return memoization[(fil, 0)]

    memoization[(fil, col)] = max(_laberinto(fil - 1, col, memoization, matriz), _laberinto(fil, col - 1, memoization, matriz)) + matriz[fil][col]
    return memoization[(fil, col)]

# Solución bottom-up:
# Complejidad temporal y espacial: O(N * M)
def laberinto3(matriz):
    if len(matriz) == 0:
        return 0
    
    sumatorias = [[matriz[0][0]]]
    for fil in range(1, len(matriz)): # LLeno la máxima ganancia de los casilleros de la izquierda.
        sumatorias.append([sumatorias[fil-1][0] + matriz[fil][0]])

    for col in range(1, len(matriz[0])): # LLeno la máxima ganancia de los casilleros de arriba.
        sumatorias[0].append(sumatorias[0][col-1] + matriz[0][col])

    for fil in range(1, len(matriz)): # LLeno la ganancia de los demás casilleros.
        for col in range(1, len(matriz[0])):
            sumatorias[fil].append(max(sumatorias[fil - 1][col], sumatorias[fil][col - 1]) + matriz[fil][col])

    return sumatorias[len(matriz) - 1][len(matriz[0]) - 1]

# Solución bottom-up:
# Complejidad temporal: O(N * M)
# Complejidad espacial: O(N), con N = Nro. de colúmnas
def laberinto(matriz):
    if len(matriz) == 0:
        return 0
    
    sumatorias = [matriz[0][0]]
    for col in range(1, len(matriz[0])): # LLeno la máxima ganancia de los casilleros de arriba.
        sumatorias.append(sumatorias[col-1] + matriz[0][col])

    for fil in range(1, len(matriz)): # LLeno la ganancia de los demás casilleros.
        for col in range(0, len(matriz[0])):
            if col == 0:
                sumatorias[0] += matriz[fil][0]
                continue

            # sumatorias[col - 1] es el casillero de la izq y sumatorias[col] es el casillero de arriba:
            sumatorias[col] = max(sumatorias[col - 1], sumatorias[col]) + matriz[fil][col]

    return sumatorias[-1]

def main():
    matriz = [[5, 7],
              [6, 2]]
    print(laberinto(matriz)) # 14

    matriz = [[5, 2],
              [6, 2]]
    print(laberinto(matriz)) # 13

    matriz = [[5, 7, 4, 7]]
    print(laberinto(matriz)) # 23

    matriz = [[5],
              [6],
              [2]]
    print(laberinto(matriz)) # 13

    matriz = [[5]]
    print(laberinto(matriz)) # 5

    matriz = []
    print(laberinto(matriz)) # 0

    matriz = [[5, 7, 1],
              [6, 2, 4]]
    print(laberinto(matriz)) # 18

    matriz = [[5, 7, 4, 7],
              [6, 2, 4, 5],
              [2, 1, 8, 3]]
    print(laberinto(matriz))

if __name__ == "__main__":
    main()