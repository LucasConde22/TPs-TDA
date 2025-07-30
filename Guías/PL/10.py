import pulp

def buscar_k_cercanos(arr, k):
    # Variables:
    v = [pulp.LpVariable(f"v_{i}", cat ="Binary") for i in range(len(arr))]
    y = [pulp.LpVariable(f"y_{i}", cat ="Integer") for i in range(len(arr))]

    # Problema:
    problema = pulp.LpProblem("buscar_k_cercanos", pulp.LpMinimize)

    # Función objetivo:
    problema += pulp.lpSum(y[i] for i in range(len(arr)))

    # Restricciones (2n + 1):
    problema += pulp.lpSum(v[i] for i in range(len(arr))) == k
    for i in range(len(arr)):
        problema += (k - arr[i]) * v[i] <= y[i]
        problema += (arr[i] - k) * v[i] <= y[i]

    # Solución:
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    return [arr[i] for i in range(len(arr)) if pulp.value(v[i]) == 1]

def main():
    print(buscar_k_cercanos([1, 3, 4, 7, 8, 9, 12, 13, 14, 20, 30], 5))
    print(buscar_k_cercanos([-5, 3, 4, 7, 8, 9, 12, 13, 14, 20], 4))
    print(buscar_k_cercanos([1, 3, 4, 7, 8, 9, 12, 13, 14, 20, 30], 8))
    print(buscar_k_cercanos([1, 3, 4, 7, 8, 9, 12, 13, 14, 20, 30], 0))
    print(buscar_k_cercanos([20, 30, 40, 50, 60, 70], 3))
    print(buscar_k_cercanos([2, 3, 4, 5, 6, 7], 4))

if __name__ == "__main__":
    main()