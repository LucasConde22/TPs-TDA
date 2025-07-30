from grafo import Grafo

"""
Complejidad:
            O(V + E), siendo V el nro. de vértices y E el nro. de aristas (acotado por V^2 - 1).

Ecuación de recurrencia:
            OPT(v) = max(OPT(j) + peso(j, v), para todo j conectado hacia v)

Caso base:
            OPT(origen) = 0
"""
def encontrar_camino_max(origen, fin, grafo):
    orden = buscar_orden_topologico(origen, grafo)

    dist = {v: float('-inf') for v in grafo}
    dist[origen] = 0
    padre = {origen: None}

    for v in orden:
        for a in grafo.adyacentes(v):
            nueva_dist = dist[v] + grafo.peso_arista(v, a)
            if nueva_dist > dist[a]:
                dist[a] = nueva_dist
                padre[a] = v

    return reconstruir_camino(padre, fin)

def reconstruir_camino(padre, fin):
    camino = []
    actual = fin
    while actual != None:
        camino.append(actual)
        actual = padre[actual]

    return camino[::-1]

def buscar_orden_topologico(origen, grafo):
    pila = []
    orden_topologico(origen, pila, set(), grafo)
    return pila[::-1]

def orden_topologico(v, pila, visitados, grafo):
    visitados.add(v)
    for a in grafo.adyacentes(v):
        if a not in visitados:
            orden_topologico(a, pila, visitados, grafo)
    pila.append(v)

def main():
    grafo = Grafo(True, ['s', 'a', 'b', 'c', 'd', 't'])
    grafo.agregar_arista('s', 'a', 10)
    grafo.agregar_arista('s', 'b', 50)
    grafo.agregar_arista('a', 'b', 20)
    grafo.agregar_arista('b', 'c', 30)
    grafo.agregar_arista('d', 'c', 5)
    grafo.agregar_arista('c', 't', 40)
    print(encontrar_camino_max('s', 't', grafo))

if __name__ == '__main__':
    main()