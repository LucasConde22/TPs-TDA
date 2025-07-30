import pulp

def compra_venta(precios):
    # Variables:
    v = []
    for i in range(len(precios)):
        v.append([])
        for j in range(len(precios)):
             v[-1].append(pulp.LpVariable(f"v_{i}_{j}", cat ="Binary")) if j >= i else v[-1].append(None)

    # Problema:
    problema = pulp.LpProblem("compra_venta", pulp.LpMaximize)

    # Función objetivo:
    problema += pulp.lpSum((v[i][j] * (precios[j] - precios[i])  for i in range(len(precios)) for j in range(i, len(precios))))

    # Restricción:
    problema += pulp.lpSum(v[i][j] for i in range(len(precios)) for j in range(i, len(precios))) == 1
    
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    for i in range(len(precios)):
        for j in range(i, len(precios)):
            if pulp.value(v[i][j]):
                return i, j
    return None, None

def main():
    print(compra_venta([]))
    print(compra_venta([50, 50]))
    print(compra_venta([50, 30, 60, 45, 60, 50]))
    p = [1, 2, 9, 1, 2, 7, 1, 2, 8]
    inicio, fin = compra_venta(p) # inicio = 0, fin = 2
    print(inicio, fin)

    p = [13, 15, 31, 22, 49, 35, 26, 27, 47, 30, 48, 16, 9, 11, 50, 28, 48, 42, 29, 7, 8]
    inicio, fin = compra_venta(p)
    print(inicio == 12)
    print(fin == 14)

    p = [10, 9, 8, 5, 2, 7, 9]
    inicio, fin = compra_venta(p)
    print(inicio, 3)
    print(fin, 6)

if __name__ == "__main__":
    main()