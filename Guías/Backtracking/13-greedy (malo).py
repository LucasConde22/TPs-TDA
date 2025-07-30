from grafo import Grafo

def vertex_cover_min(grafo):
    grafo = copiar_grafo(grafo)
    resultado = []

    v = _mas_ady(grafo)
    while v:
        resultado.append(v)
        grafo.borrar_vertice(v)
        v = _mas_ady(grafo)
    return resultado

def _mas_ady(grafo):
    """
    Devuelve el vértice con más adyacentes, si ningún
    vértice tiene adyacentes retorna None.
    """
    max_v, cant_max = None, 0
    for v in grafo:
        cant_ady = len(grafo.adyacentes(v))
        if cant_ady > cant_max:
            max_v, cant_max = v, cant_ady
    return max_v

def copiar_grafo(grafo):
    nuevo = Grafo(False, grafo.obtener_vertices())
    for v in grafo:
        for a in grafo.adyacentes(v):
            if not nuevo.estan_unidos(v, a):
                nuevo.agregar_arista(v, a)
    return nuevo


def main():
    grafo = Grafo(False, ["A", "B", "C", "D", "E", "F", "G", "H"])
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("B", "E")
    grafo.agregar_arista("B", "F")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("C", "E")
    grafo.agregar_arista("D", "E")
    grafo.agregar_arista("D", "H")
    grafo.agregar_arista("F", "G")

    print(vertex_cover_min(grafo))

    g = Grafo(False, ['A', 'B', 'C', 'D'])   
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('A', 'D')
    g.agregar_arista('C', 'D')
    print(vertex_cover_min(g))

if __name__ == "__main__":
    main()
    