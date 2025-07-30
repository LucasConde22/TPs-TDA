"""
El algoritmo implementado consiste en iterar todas las celdas de la matriz
y seleccionar como óptimo local, que se agrega a la solución, la posición
que cubra la mayor cantidad de submarinos. De esta manera, el algoritmo
busca en cada iteración minimizar la cantidad de submarinos que se necesitan
tapar hasta que, eventualmente, se consigue una solución global al haberlos
tapado todos. Una vez agregado el nuevo faro, se actualiza el estado actual
borrando todos los submarinos que ya fueron cubiertos.

La complejidad del algoritmo resulta ser O(S*N*M), siendo:
    S la cantidad de submarinos.
    N la cantidad de filas.
    M la cantidad de columnas.

Por cada submarino (en el peor de los casos, porque podrían borrarse varios
en una misma iteración) se recorre toda la matriz, de tamaño N*M, y se realizan
varias operaciones de tiempo constante.
Borrar los submarinos que se cubren no aumenta la complejidad ya que reduce la
cantidad de iteraciones restantes en el "while" que corta cuando "sumarinos" ya
no posee elementos.

Resolver este problema implementando una solución Greedy no encuentra una
solución óptima en todos los casos, pero permite obtener aproximaciónes que
pueden utilizarse, por ejemplo, como recorte en una solución aplicando
Backtracking, que si encuentra soluciones óptima cualquiera sea el caso.
"""

def submarinos(matriz):
    submarinos = _buscar_submarinos(matriz)
    solucion = []

    while len(submarinos) != 0:
        max_cobertura, max_pos = [], None

        for fil in range(len(matriz)):
            for col in range(len(matriz[0])):
                cobertura = _buscar_cobertura(fil, col, submarinos)
                if len(cobertura) > len(max_cobertura):
                    max_cobertura, max_pos = cobertura, (fil, col)
        
        solucion.append(max_pos)
        submarinos.difference_update(max_cobertura)

    return solucion

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