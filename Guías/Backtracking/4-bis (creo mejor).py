from grafo import Grafo

def independent_set(grafo):
    return _buscar_max_id(grafo, grafo.obtener_vertices(), 0, [])

def _chequear_compatibilidad(grafo, v, solucion):
    for a in solucion:
        if grafo.estan_unidos(v, a):
            return False
    return True

def _buscar_max_id(grafo, vertices, i, solucion_parcial):
    if i == len(vertices):
            return solucion_parcial[:]

    max = []
    if _chequear_compatibilidad(grafo, vertices[i], solucion_parcial):
        solucion_parcial.append(vertices[i])
        max = _buscar_max_id(grafo, vertices, i + 1, solucion_parcial)
        solucion_parcial.pop()

    solucion_sin_actual = _buscar_max_id(grafo, vertices, i + 1, solucion_parcial)
    if len(solucion_sin_actual) > len(max):
        max = solucion_sin_actual

    return max
    
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
    print(independent_set(grafo))

    g = Grafo(False, ['A', 'B', 'C', 'D'])   
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('A', 'D')
    print(independent_set(g))

if __name__ == "__main__":
    main()