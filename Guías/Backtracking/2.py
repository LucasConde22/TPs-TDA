from grafo import Grafo

# Complejidad: O(2^V)
def colorear(grafo, n):
    return _asignar_colores(grafo, grafo.obtener_vertices(), 0, {}, n)

def _validar_color(grafo, asignados, v):
    for a in asignados:
        if a == v:
            continue
        if grafo.estan_unidos(v, a) and asignados[a] == asignados[v]:
            return False
    return True

def _asignar_colores(grafo, vertices, i, asignados, n):
    if i == len(vertices):
        return True

    for color in range(n):
        asignados[vertices[i]] = color
        if _validar_color(grafo, asignados, vertices[i]):
            if _asignar_colores(grafo, vertices, i + 1, asignados, n):
                return True
    asignados.pop(vertices[i])
    return False

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
    

    print(colorear(grafo, 4)) # True
    print(colorear(grafo, 3)) # True
    print(colorear(grafo, 2)) # False

    g = Grafo(False, ['A', 'B', 'C', 'D'])   
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('A', 'D')
    resul = colorear(g, 2)
    print(resul) # True
    print(colorear(g, 1)) # False

if __name__ == "__main__":
    main()