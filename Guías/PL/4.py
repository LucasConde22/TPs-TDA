from grafo import Grafo
import pulp

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    indice = {v: i for i, v in enumerate(vertices)}

    v = [pulp.LpVariable(vertice, cat ="Binary") for vertice in vertices]
    problema = pulp.LpProblem("vertex_cover", pulp.LpMinimize)
    problema += pulp.lpSum(v[i] for i in range(len(vertices)))

    for w in vertices:
            problema += pulp.lpSum(v[indice[a]] for a in [w] + grafo.adyacentes(w)) >= 1
    
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
    print(dominating_set_min(grafo))

    g = Grafo(False, ['A', 'B', 'C', 'D'])   
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('A', 'D')
    print(dominating_set_min(g))

    grafo = Grafo(False, ["A", "B", "C", "D", "E"])
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "B")
    grafo.agregar_arista("B", "E")
    print(dominating_set_min(grafo))

if __name__ == "__main__":
    main()