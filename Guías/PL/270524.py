import pulp
from grafo import Grafo

def dominating_set_minimo(grafo, valores):
    vertices = grafo.obtener_vertices()
    indices = {v: i for i, v in enumerate(vertices)}

    # Variables:
    v = [pulp.LpVariable(f"v_{i}", cat ="Binary") for i in range(len(vertices))]

    # Problema:
    problema = pulp.LpProblem("ds_min", pulp.LpMinimize)

    # Función objetivo:
    problema += pulp.lpSum(valores[vertices[i]] * v[i] for i in range(len(vertices)))

    # Restricciones (n):
    for i in range(len(vertices)):
        problema += v[i] + pulp.lpSum(v[indices[a]] for a in grafo.adyacentes(vertices[i])) >= 1

    # Solución:
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return [vertices[i] for i in range(len(vertices)) if pulp.value(v[i]) == 1]

def main():
    grafo = Grafo(False, ['A', 'B', 'C'])
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    valores = {'A': 5, 'B': 1, 'C': 1}
    print(dominating_set_minimo(grafo, valores))

    valores = {'A': 1, 'B': 1, 'C': 1}
    print(dominating_set_minimo(grafo, valores))

if __name__ == "__main__":
    main()