from grafo import Grafo

"""
El "problema de decisión" de Independent Set consiste en, dado un grafo no
dirigido con V vértices, E aristas y un entero K, determinar si existe un
conjunto de vértices independientes entre ellos (que cada par no este
unido por una arista), de tamaño, al menos, K.
"""

"""
Valida que una solución sea efectivamente un independent set de de un grafo
con tamaño de, al menos, K.
Complejidad: O(J^2), siendo J el nro. de vértices en la solución. Con
K <= J <= V.
"""
def validador_is(grafo, k, solucion):
    if len(solucion) < k:
        return False
    
    for v in solucion:
        if v not in grafo:
            return False
        for a in solucion:
            if v == a:
                continue
            if a not in grafo or grafo.estan_unidos(v, a):
                return False
    return True

def main():
    grafo = Grafo(False, ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("B", "E")
    grafo.agregar_arista("B", "F")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("C", "E")
    grafo.agregar_arista("D", "E")
    grafo.agregar_arista("D", "H")
    grafo.agregar_arista("F", "G")
    grafo.agregar_arista("A", "I")
    grafo.agregar_arista("I", "J")
    inds = ['A', 'B', 'D', 'G', 'J']
    print(f'IS: {inds} K: {5}, es válido?: {validador_is(grafo, 5, inds)}')
    print(f'IS: {inds} K: {7}, es válido?: {validador_is(grafo, 7, inds)}')
    inds = ['A', 'B', 'D', 'G', 'J', 'F']
    print(f'IS: {inds} K: {5}, es válido?: {validador_is(grafo, 5, inds)}')


if __name__ == "__main__":
    main()