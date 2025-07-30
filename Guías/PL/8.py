from grafo import Grafo
import pulp

def clique_maximo(grafo):
    no_adyacentes = {}
    for v in grafo:
        no_adyacentes[v] = set()
        adyacentes = set(grafo.adyacentes(v))
        for w in grafo:
            if w == v or w in adyacentes:
                continue
            no_adyacentes[v].add(w)

    M = len(grafo) - 2
    vertices = grafo.obtener_vertices()
    indice = {v: i for i, v in enumerate(vertices)}

    # Variables:
    v = [pulp.LpVariable(vertice, cat ="Binary") for vertice in vertices]

    # Problema:
    problema = pulp.LpProblem("clique_maximo", pulp.LpMaximize)

    # Función objetivo:
    problema += pulp.lpSum(v[i] for i in range(len(vertices)))

    # Restricciones:
    for w in grafo:
        problema += v[indice[w]] + pulp.lpSum(v[indice[a]] for a in no_adyacentes[w]) <= 1 + M * (1 - v[indice[w]])

    # Solución:
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return [vertices[i] for i in range(len(vertices)) if pulp.value(v[i])]

def main():
    grafo = Grafo(False, ["1", "2", "3", "4", "5", "6"])
    grafo.agregar_arista("1", "2")
    grafo.agregar_arista("1", "5")
    grafo.agregar_arista("2", "5")
    grafo.agregar_arista("2", "3")
    grafo.agregar_arista("3", "4")
    grafo.agregar_arista("4", "5")
    grafo.agregar_arista("4", "6")
    print(clique_maximo(grafo))

if __name__ == "__main__":
    main()