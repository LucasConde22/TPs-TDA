import pulp

def buscar_incompatibilidad(charlas):
    incompatibles = {}
    charlas = sorted(charlas, key =  lambda x: x[1])
    for i, (_, fin, _) in enumerate(charlas):
        incompatibles[i] = []
        for j in range(i + 1, len(charlas)):
            ini2, _, _ = charlas[j]
            if ini2 < fin:
                incompatibles[j] = incompatibles.get(j, [])
                incompatibles[i].append(j)
                incompatibles[j].append(i)
    return incompatibles

def scheduling(charlas):
    # Constantes:
    incompatibles = buscar_incompatibilidad(charlas)
    M = len(charlas)

    # Variables:
    v = [pulp.LpVariable(f"v_{i}", cat ="Binary") for i in range(len(charlas))]

    # Problema:
    problema = pulp.LpProblem("scheduling_con_valores", pulp.LpMaximize)

    # Función objetivo:
    problema += pulp.lpSum(charlas[i][2] * v[i] for i in range(len(charlas)))

    # Restricciones (n):
    for i in range(len(charlas)):
        problema += v[i] + pulp.lpSum(v[j] for j in incompatibles[i]) <= 1 + M * (1 - v[i])

    # Solución:
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return [charlas[i] for i in range(len(charlas)) if pulp.value(v[i]) == 1]

def main():
    print(scheduling([(0, 2, 2), (1, 4, 4), (3, 5, 4), (1, 6, 7), (5, 8, 2), (5, 9, 1)]))
    print(scheduling([(0, 2, 2), (1, 6, 7)]))
    print(scheduling([(0, 2, 2)]))
    print(scheduling([]))
    print(scheduling([(0, 2, 2), (1, 6, 7), (10, 15, 5)]))


if __name__ == "__main__":
    main()