from grafo import Grafo

"""
NO SÉ SI EL ALGORITMO ES CORRECTO

Según un apunte random de la Universidad de Guadalajara:
    "Dos grafos son isomorfos si y solo si para alguna ordenación de vértices y
    lados sus matrices de incidencia son iguales."
"""
def hay_isomorfismo(g1, g2):
    v_g1 = g1.obtener_vertices()
    v_g2 = g2.obtener_vertices()

    if len(v_g1) != len(v_g2):
        return False
    if len(v_g1) == 0 and len(v_g2) == 0:
        return True

    for v in v_g1:
        for w in v_g2:
            if len(g1.adyacentes(v)) != len(g2.adyacentes(w)):
                continue
            if _hallar_isomorfismo(v, w, set(), set(), g1, g2):
                return True
    return False


def _hallar_isomorfismo(v, w, visitados, usados, g1, g2):
    visitados.add(v)
    usados.add(w)

    if len(visitados) == len(g1.obtener_vertices()):
        return True

    ady_w = None
    for a in g2.adyacentes(w):
        if not a in usados:
            ady_w = a
            break
            
    if not ady_w:
        return False
    
    for a in g1.adyacentes(v):
        if not a in visitados and len(g1.adyacentes(a)) == len(g2.adyacentes(ady_w)):
            if _hallar_isomorfismo(a, ady_w, visitados, usados, g1, g2):
                return True
    
    visitados.remove(v)
    usados.remove(w)
    return False

def main():
    g1 = Grafo(False, ['A', 'B', 'C', 'D'])   
    g1.agregar_arista('A', 'B')
    g1.agregar_arista('A', 'C')
    g1.agregar_arista('A', 'D')

    g2 = Grafo(False, ['a', 'b', 'c', 'd'])
    g2.agregar_arista('a', 'b')
    g2.agregar_arista('a', 'c')
    g2.agregar_arista('a', 'd')

    print(hay_isomorfismo(g1, g2))

    grafo = Grafo(False, ["B", "C", "D", "E", "F", "G", "H"])
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("B", "E")
    grafo.agregar_arista("B", "F")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("C", "E")
    grafo.agregar_arista("D", "E")
    grafo.agregar_arista("D", "H")
    grafo.agregar_arista("F", "G")

    grafo2 = Grafo(False, ["B", "C", "D", "E", "F", "G", "H"])
    grafo2.agregar_arista("B", "C")
    grafo2.agregar_arista("B", "E")
    grafo2.agregar_arista("B", "F")
    grafo2.agregar_arista("C", "D")
    grafo2.agregar_arista("C", "E")
    grafo2.agregar_arista("D", "E")
    grafo2.agregar_arista("D", "H")
    grafo2.agregar_arista("F", "G")

    print(hay_isomorfismo(grafo, grafo2))

if __name__ == "__main__":
    main()

        