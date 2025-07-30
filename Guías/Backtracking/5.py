from grafo import Grafo

# Para que un grafo tenga cammino hamiltoneano debe ser conexo.
def camino_hamiltoniano(grafo):
    vertices = grafo.obtener_vertices()
    visitados = set()
    for v in grafo:
        camino = []
        if _hallar_camino(v, camino, visitados, len(vertices), grafo):
            return camino
    return None

def _hallar_camino(v, camino, visitados, n, grafo):
    visitados.add(v)
    camino.append(v)

    if len(camino) == n:
        return True

    for a in grafo.adyacentes(v):
        if not a in visitados:
            if _hallar_camino(a, camino, visitados, n, grafo):
                return True
    
    visitados.remove(v)
    camino.pop()
    return False

def main():
    grafo = Grafo(False, ["B", "C", "D", "E", "F", "G", "H"])
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("B", "E")
    grafo.agregar_arista("B", "F")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("C", "E")
    grafo.agregar_arista("D", "E")
    grafo.agregar_arista("D", "H")
    grafo.agregar_arista("F", "G")
    print(camino_hamiltoniano(grafo))

if __name__ == "__main__":
    main()
        
    



