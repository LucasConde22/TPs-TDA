from grafo import Grafo

"""
Complejidad:
            O(V + E)

Ecuación de recurrencia:
            OPT(v) = max(OPT(w) + 1) para todo vértice w conectado a v.
"""
def camino_mas_largo(vertices, grafo):
    dist = {v: 1 for v in vertices}
    padre = {v: None for v in vertices}
    max_v, max_dist = vertices[0], 1

    for v in vertices:
        for a in grafo.adyacentes(v):
            nueva_dist = dist[v] + 1
            if nueva_dist > dist[a]:
                padre[a] = v
                dist[a] = nueva_dist
                if nueva_dist > max_dist:
                    max_v, max_dist = a, nueva_dist
    
    camino, actual = [], max_v
    while actual != None:
        camino.append(actual)
        actual = padre[actual]

    return max_dist, camino[::-1]

def main():
    grafo = Grafo(True, ['v1', 'v2', 'v3', 'v4', 'v5'])
    grafo.agregar_arista('v1', 'v2')
    grafo.agregar_arista('v1', 'v4')
    grafo.agregar_arista('v2', 'v4')
    grafo.agregar_arista('v2', 'v5')
    grafo.agregar_arista('v3', 'v4')
    grafo.agregar_arista('v4', 'v5')
    print(camino_mas_largo(['v1', 'v2', 'v3', 'v4', 'v5'], grafo))

    grafo = Grafo(True, ['v1', 'v2', 'v3', 'v4'])
    grafo.agregar_arista('v1', 'v2')
    grafo.agregar_arista('v2', 'v3')
    grafo.agregar_arista('v1', 'v3')
    print(camino_mas_largo(['v1', 'v2', 'v3', 'v4'], grafo))

if __name__ == "__main__":
    main()
