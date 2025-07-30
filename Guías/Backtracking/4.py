from grafo import Grafo

"""
Se reutiliza la fución del punto del punto 1,
iterando desde 1 hasta la cantidad de vértices
(máximo independent set posible).
"""
def independent_set(grafo):
    max = []
    for n in range (1, len(grafo.obtener_vertices()) + 1):
        solucion = no_adyacentes(grafo, n)
        if not solucion:
            return max
        max = solucion
    return max

def no_adyacentes(grafo, n):
    vertices = grafo.obtener_vertices()
    solucion = []
    _bt_no_ady(grafo, vertices, 0, solucion, n)

    return solucion

def _chequear_compatibilidad(grafo, v, solucion):
    for a in solucion:
        if grafo.estan_unidos(v, a):
            return False
    return True

def _bt_no_ady(grafo, vertices, i, solucion, n):
    if len(solucion) == n:
        return True
    
    if i == len(vertices):
        return False
    
    if len(solucion) + len(vertices) - i < n: # Si ya se que no llego, recorto
        return False

    if _chequear_compatibilidad(grafo, vertices[i], solucion):
        solucion.append(vertices[i])
        en_solucion = True
    else:
        en_solucion = False
    
    siguiente = _bt_no_ady(grafo, vertices, i + 1, solucion, n)
    if not siguiente and en_solucion:
        solucion.pop()
        siguiente = _bt_no_ady(grafo, vertices, i + 1, solucion, n)

    return siguiente

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
