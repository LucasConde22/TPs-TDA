def submarinos(matriz):
    return _poner_faros(0, 0, _buscar_submarinos(matriz), [], None, matriz)

def _poner_faros(fil, col, submarinos, faros, minima, matriz):
    if len(submarinos) == 0:
        return faros[:]
    
    if col == len(matriz[0]):
        if fil == len(matriz) - 1:
            return None # Significa que no encontró solución
        fil += 1
        col = 0

    cobertura = _buscar_cobertura(fil, col, submarinos)
    if len(cobertura) != 0: # Si la pos. no cubre nada, omite incluirla.
        submarinos.difference_update(cobertura)
        faros.append((fil, col))
        solucion = _poner_faros(fil, col + 1, submarinos, faros, minima, matriz)
        if solucion and (not minima or len(solucion) < len(minima)):
            minima = solucion
        submarinos.update(cobertura)
        faros.pop()

    solucion = _poner_faros(fil, col + 1, submarinos, faros, minima, matriz)
    if solucion and (not minima or len(solucion) < len(minima)):
        minima = solucion

    return minima

def _buscar_cobertura(fil, col, submarinos):
    combinaciones = [-2, -1, 0, 1, 2]
    cobertura = set()
    for i in combinaciones:
        for j in combinaciones:
            if (fil + i, col + j) in submarinos:
                cobertura.add((fil + i, col + j))
    return cobertura

def _buscar_submarinos(matriz):
    submarinos = set()
    for fil in range(len(matriz)):
        for col in range(len(matriz[0])):
            if matriz[fil][col]:
                submarinos.add((fil, col))
    return submarinos

def main():
    matriz = [[False, False, False, True],
              [False, False, False, False],
              [True, False, False, False]]
    
    print(submarinos(matriz))

if __name__ == "__main__":
    main()