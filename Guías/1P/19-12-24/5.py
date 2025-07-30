"""
Complejidad:
            O(V*E), siendo V el nro. de vértices y E el nro. de aristas (acotado por V^2 - 1).

Ecuación de recurrencia:
            OPT(v) = max(OPT(j) + peso(j, v), para todo j conectado hacia v)

Caso base:
            OPT(origen) = 0
"""
from grafo import Grafo

def encontrar_camino_max(origen, fin, grafo):
    dist = {v: float('-inf') for v in grafo}
    dist[origen] = 0
    padre = {origen: None}
    aristas = obtener_aristas(grafo)

    for _ in range(len(grafo)):
        for v, a, peso in aristas:
            nueva_dist = dist[v] + peso
            if nueva_dist > dist[a]:
                padre[a] = v
                dist[a] = nueva_dist

    return reconstruir_camino(padre, fin)

def reconstruir_camino(padre, fin):
    camino = []
    actual = fin
    while actual != None:
        camino.append(actual)
        actual = padre[actual]

    return camino[::-1]

def obtener_aristas(grafo):
    aristas = []
    for v in grafo:
        for a in grafo.adyacentes(v):
            aristas.append((v, a, grafo.peso_arista(v, a)))
    return aristas
        
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