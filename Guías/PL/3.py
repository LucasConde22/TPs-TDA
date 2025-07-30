import pulp
from grafo import Grafo

def vertex_cover_min(grafo):
    vertices = grafo.obtener_vertices()
    indice = {v: i for i, v in enumerate(vertices)}

    v = [pulp.LpVariable(vertice, cat ="Binary") for vertice in vertices]
    problema = pulp.LpProblem("vertex_cover", pulp.LpMinimize)
    problema += pulp.lpSum(v[i] for i in range(len(vertices)))

    # Versión "mala", E restricciones:
    """
    for w in vertices:
        for a in grafo.adyacentes(w):
            problema += v[indice[w]] + v[indice[a]] >= 1 
    """
    
    # Mejora, V restricciones:
    for w in vertices:
            problema += v[indice[w]] + pulp.lpSum(v[indice[a]] for a in grafo.adyacentes(w)) >= 1 + (len(grafo.adyacentes(w)) - 1) * (1 - v[indice[w]])


    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return [vertices[i] for i in range(len(vertices)) if pulp.value(v[i]) == 1]

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
    g.agregar_arista('D', 'C')
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