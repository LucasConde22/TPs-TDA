from grafo import Grafo
import pulp

def independent_set(grafo):
    M = len(grafo) - 2
    vertices = grafo.obtener_vertices()
    indice = {v: i for i, v in enumerate(vertices)}

    v = [pulp.LpVariable(vertice, cat ="Binary") for vertice in vertices]
    problema = pulp.LpProblem("independent_set", pulp.LpMaximize)
    problema += pulp.lpSum(v[i] for i in range(len(vertices)))

    for w in vertices:
            problema += v[indice[w]] + pulp.lpSum(v[indice[a]] for a in grafo.adyacentes(w)) <= 1 + M * (1 - v[indice[w]])
    
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return [vertices[i] for i in range(len(vertices)) if pulp.value(v[i]) == 1]

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
    print(independent_set(grafo))

    g = Grafo(False, ['A', 'B', 'C', 'D'])   
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('A', 'D')
    print(independent_set(g))

if __name__ == "__main__":
    main()