from grafo import Grafo
import pulp

def colorear(grafo):
    vertices = grafo.obtener_vertices()
    M = len(vertices) + 1
    indice = {v: i for i, v in enumerate(vertices)}

    v = [pulp.LpVariable(vertice, lowBound=1, cat ="Integer") for vertice in vertices]
    problema = pulp.LpProblem("coloreo_minimo", pulp.LpMinimize)
    v_max = pulp.LpVariable("v_max", lowBound=1, cat='Integer')
    problema += v_max

    visitados = set()
    for w in vertices:
        problema += v[indice[w]] <= v_max
        visitados.add(w)
        for a in grafo.adyacentes(w):
            if a in visitados:
                continue
            b = pulp.LpVariable(f"b_{w}_{a}", cat="Binary")
            problema += v[indice[w]] - v[indice[a]] >= 1 - M * b
            problema += v[indice[w]] - v[indice[a]] <= -1 + M * (1 - b)


    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return max([pulp.value(v[i]) for i in range(len(vertices))])

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
    print(colorear(grafo))

    g = Grafo(False, ['A', 'B', 'C', 'D'])   
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('A', 'D')
    print(colorear(g))

if __name__ == "__main__":
    main()