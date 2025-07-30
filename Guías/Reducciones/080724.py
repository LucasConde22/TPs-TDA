from grafo import Grafo

# Complejidad: O(S^2)
# S = Cant. de vértices de la solución y en G2, cota superior cant. de vértices en G1.
def validador_subgrafo_isomorfico(g1, g2, solucion):
    if len(solucion) != len(g2) or len(solucion) > len(g1):
        return False
    
    visitados_g2 = set()
    visitados_g1 = set()
    for v, a in solucion.items():
        if v not in g1 or v in visitados_g1:
            return False
        visitados_g1.add(v)

        if a not in g2 or a in visitados_g2:
            return False
        visitados_g2.add(a)

        for w, y in solucion.items():
            if not w in g1:
                return False
            if g1.estan_unidos(v, w):
                if not y in g2 or not g2.estan_unidos(a, y):
                    return False
    return True

def main():
    g1 = Grafo(False, ['0', '1', '2', '3', '4'])
    g1.agregar_arista('0', '1')
    g1.agregar_arista('0', '2')
    g1.agregar_arista('1', '2')
    g1.agregar_arista('2', '3')
    g1.agregar_arista('2', '4')

    g2 = Grafo(False, ['a', 'b', 'c'])
    g2.agregar_arista('a', 'b')
    g2.agregar_arista('b', 'c')
    g2.agregar_arista('a', 'c')

    print(validador_subgrafo_isomorfico(g1, g2, {'0': 'a', '1': 'c', '2': 'b'}))
    print(validador_subgrafo_isomorfico(g1, g2, {'0': 'a', '1': 'a', '2': 'b', '3': 'c'}))
    print(validador_subgrafo_isomorfico(g1, g2, {'0': 'a', '1': 'b'}))

    g3 = Grafo(False, ['1', '2', '3'])
    g3.agregar_arista('1', '2')
    g3.agregar_arista('1', '3')
    
    print(validador_subgrafo_isomorfico(g1, g3, {'1': '1', '2': '2', '3': '3'}))

    g4 = Grafo(False, ['a', 'w', 'e', 'y'])
    g4.agregar_arista('w', 'a')
    g4.agregar_arista('w', 'e')
    g4.agregar_arista('a', 'y')
    g4.agregar_arista('e', 'y')

    print(validador_subgrafo_isomorfico(g1, g4, {'0': 'a', '1': 'w', '2': 'e', '3': 'y'}))

if __name__ == "__main__":
    main()
    