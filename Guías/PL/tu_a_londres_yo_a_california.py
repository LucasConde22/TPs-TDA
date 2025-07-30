import pulp

def plan_operativo(arreglo_L, arreglo_C, costo_M):
    # Variables:
    l = [pulp.LpVariable(f"l_{i}", cat ="Binary") for i in range(len(arreglo_L))]
    c = [pulp.LpVariable(f"c_{i}", cat ="Binary") for i in range(len(arreglo_C))]
    m = [pulp.LpVariable(f"m_{i}", cat ="Binary") for i in range(len(arreglo_L) - 1)]

    # Problema:
    problema = pulp.LpProblem("plan_operativo", pulp.LpMinimize)

    # Función objetivo:
    problema += pulp.lpSum(arreglo_L[i] * l[i] for i in range(len(arreglo_L))) + pulp.lpSum(arreglo_C[i] * c[i] for i in range(len(arreglo_C))) + pulp.lpSum(costo_M * m[i] for i in range(len(arreglo_L) - 1))

    # Restricciones (3*n):
    for i in range(len(arreglo_L)):
        problema += l[i] + c[i] == 1
        if i < len(arreglo_L) - 1:
            problema += l[i] - l[i + 1] <= m[i]
            problema += l[i + 1] - l[i] <= m[i]

    # Solución:
    problema.solve(pulp.PULP_CBC_CMD(msg=False))
    plan = []
    for i in range(len(arreglo_L)):
        if pulp.value(l[i]) == 1:
            plan.append("londres")
        else:
            plan.append("california")
    return plan

def main():
    print(plan_operativo([], [], 20))
    print(plan_operativo([5], [10], 20))
    print(plan_operativo([80, 50, 120, 60], [70, 120, 100, 50], 20))
    print(plan_operativo([80, 50, 100, 35, 120, 120], [70, 50, 130, 80, 25, 100], 10))

    londres = [100, 50]
    california = [75, 100]
    print(plan_operativo(londres, california, 75)) # ['londres', 'londres']

    londres = [50, 100]
    california = [100, 50]
    print(plan_operativo(londres, california, 25)) # ['londres', 'california']

    londres = [85, 15, 55, 5, 25, 35, 55, 35]
    california = [75, 25, 45, 5, 25, 35, 25, 55]
    print(plan_operativo(londres, california, 25)) # ['california']*8

    londres = [5, 46, 18, 88, 33, 13, 22, 35, 58]
    california = [20, 10, 65, 24, 55, 2, 28, 14, 94]
    print(plan_operativo(londres, california, 25)) # ['londres','londres','londres','california','california','california','california','california','londres'])"

if __name__ == "__main__":
    main()