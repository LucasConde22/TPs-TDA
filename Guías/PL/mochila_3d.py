import pulp

def mochila_3d(productos, precio_max, capacidad_max): # productos = [(precio, peso, valor), ...]
    # Variables:
    v = [pulp.LpVariable(f"v_{i}", cat ="Binary") for i in range(len(productos))]

    # Problema:
    problema = pulp.LpProblem("mochila_3d", pulp.LpMaximize)

    # Función objetivo:
    problema += pulp.lpSum(productos[i][2] * v[i] for i in range(len(productos)))

    # Restricciones (n):
    problema += pulp.lpSum(productos[i][0] * v[i] for i in range(len(productos))) <= precio_max
    problema += pulp.lpSum(productos[i][1] * v[i] for i in range(len(productos))) <= capacidad_max

    # Solución:
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return [productos[i] for i in range(len(productos)) if pulp.value(v[i]) == 1]

def main():
    productos = [(10, 8, 2), (10, 8, 8), (2, 3, 5), (1, 1, 1)]
    print(mochila_3d(productos, 11, 15))
    

if __name__ == "__main__":
    main()