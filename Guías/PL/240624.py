import pulp

def juan_el_vago(ganancias):
    # Variables:
    v = [pulp.LpVariable(f"v_{i}", cat ="Binary") for i in range(len(ganancias))]

    # Problema:
    problema = pulp.LpProblem("juan_el_vago", pulp.LpMaximize)

    # Función objetivo:
    problema += pulp.lpSum(ganancias[i] * v[i] for i in range(len(ganancias)))

    # Restricciones (n):
    for i in range(len(ganancias) - 2):
        problema += v[i] + v[i + 1] + v[i + 2] <= 2

    # Solución:
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return [i for i in range(len(ganancias)) if pulp.value(v[i]) == 1]

def main():
    print(juan_el_vago([2, 100, 120, 110, 5]))
    print(juan_el_vago([100, 5, 50, 1, 1, 200]))
    print(juan_el_vago([]))
    

if __name__ == "__main__":
    main()