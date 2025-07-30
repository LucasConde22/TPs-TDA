"""
Ecuación de recurrencia:
    Parciales:
        londres(i) = min(londres(i - 1), california(i - 1) + M) + Li
        california(i) = min(california(i - 1), londres(i - 1) + M) + Ci
    Definitiva:
        OPT(i) = min(londres(i), california(i))
"""

def plan_operativo(arreglo_L, arreglo_C, costo_M): # O(N)
    if len(arreglo_L) == 0:
        return[]

    londres = [0] * len(arreglo_L)
    california = [0] * len(arreglo_C)

    for i in range(len(arreglo_L)):
        if i == 0:
            londres[i] = arreglo_L[i]
            california[i] = arreglo_C[i]
        else:
            londres[i] = min(londres[i - 1], california[i - 1] + costo_M) + arreglo_L[i]
            california[i] = min(california[i - 1], londres[i - 1] + costo_M) + arreglo_C[i]

    camino = []
    i = len(arreglo_L) - 1
    ult = "londres" if londres[i] <= california[i] else "california"

    while i >= 0:
        if (ult == "londres" and londres[i] <= california[i] + costo_M) or (ult == "california" and londres[i] + costo_M <= california[i]):
            camino.append("londres")
            ult = "londres"
        else:
            camino.append("california")
            ult = "california"
        i -= 1
    
    return camino[::-1]

def main():
    

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