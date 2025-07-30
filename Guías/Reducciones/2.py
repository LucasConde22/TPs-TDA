from grafo import Grafo
"""
El "problema de decisión" de Vertex Cover es: Dado un grafo con V vértices,
determinar si existe un subconjunto de estos de, a lo sumo, tamaño K, tal
que todas las aristas esten "cubiertas", es decir, que uno de sus extremos
(o los dos) formen parte de la solución.
"""

"""
Valida que una solución dada sea Vertex Cover de un grafo de, a lo sumo, tamaño K.
Complejidad: O(V + E + J), con J = #elems. en solución, 0 <= J <= K <= V
"""
def validador_vc(grafo, k, solucion):
    if len(solucion) > k:
        return False
    
    solucion = set(solucion)
    for v in grafo:
        for a in grafo.adyacentes(v):
            if v not in solucion and a not in solucion:
                return False
    return True

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
    vc = ['C', 'E', 'F', 'H']
    print(f'VC: {vc} K: {5}, es válido?: {validador_vc(grafo, 5, vc)}')
    print(f'VC: {vc} K: {3}, es válido?: {validador_vc(grafo, 3, vc)}')
    vc = ['C', 'E', 'F']
    print(f'VC: {vc} K: {5}, es válido?: {validador_vc(grafo, 5, vc)}')

if __name__ == "__main__":
    main()