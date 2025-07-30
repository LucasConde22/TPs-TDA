from grafo import Grafo

def vertex_cover_min(grafo):
    grafo = copiar_grafo(grafo)
    resultado = []

    while True:
        elegido = None
        max_adyacentes = 0

        for v in grafo:
            cant_adyacentes = len(grafo.adyacentes(v))
            if cant_adyacentes > max_adyacentes:
                elegido = v
                max_adyacentes = cant_adyacentes

        if not elegido:
            break
        grafo.borrar_vertice(elegido)
        resultado.append(elegido)

    return resultado

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


    g = Grafo(False, ['1', '2', '3', '4', '5', '6', '7'])   
    g.agregar_arista('1', '2')
    g.agregar_arista('1', '4')
    g.agregar_arista('2', '3')
    g.agregar_arista('2', '5')
    g.agregar_arista('3', '7')
    g.agregar_arista('3', '6')
    g.agregar_arista('5', '6')
    print(vertex_cover_min(g))

if __name__ == "__main__":
    main()