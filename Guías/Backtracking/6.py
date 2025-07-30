def resolver_sudoku(matriz):
    _asignar_faltantes(0,  _buscar_pos_a_completar(matriz), matriz)
    return matriz

def _asignar_faltantes(i, a_completar, matriz):
    if i == len(a_completar):
        return True

    disponibles = _buscar_compatibilidad(a_completar[i][0], a_completar[i][1], matriz)
    for disponible in disponibles:
        matriz[a_completar[i][0]][a_completar[i][1]] = disponible
        if _asignar_faltantes(i + 1, a_completar, matriz):
            return True
    
    matriz[a_completar[i][0]][a_completar[i][1]] = 0
    return False

def _buscar_compatibilidad(fil, col, matriz):
    disponibles = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    combinaciones = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4, 5], 4: [3, 5], 5: [3, 4], 6: [7, 8], 7: [6, 8], 8: [6, 7]}

    for usado in matriz[fil]:
        if usado in disponibles:
            disponibles.remove(usado)

    for i in range(len(matriz)):
        if matriz[i][col] in disponibles:
            disponibles.remove(matriz[i][col])

    for subfil in combinaciones[fil]:
        for subcol in combinaciones[col]:
            if matriz[subfil][subcol] in disponibles:
                disponibles.remove(matriz[subfil][subcol])

    return disponibles

def _buscar_pos_a_completar(matriz):
    a_completar = []
    for fil in range(len(matriz)):
        for col in range(len(matriz[0])):
            if matriz[fil][col] == 0:
                a_completar.append((fil, col))
    return a_completar


def main():
    sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    print(resolver_sudoku(sudoku))

    sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(resolver_sudoku(sudoku))

if __name__ == "__main__":
    main()