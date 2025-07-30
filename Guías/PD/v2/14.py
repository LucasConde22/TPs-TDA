"""
OPT(i) =    0, si i = 0
            max(OPT(i - 1), OPT(i - 2) + Gi), si 1 <= i <= n
"""

def lunatico(ganancias):
    if len(ganancias) == 0:
        return []
    if len(ganancias) == 1:
        return [0]
    
    ganancia0 = [0] * (len(ganancias) - 1)
    ganancia1 = [0] * (len(ganancias) - 1)

    ganancia0[0] = ganancias[0]
    ganancia1[0] = ganancias[1]

    for i in range(1, len(ganancias) - 1):
        if i == 1:
            ganancia0[i] = max(ganancia0[i - 1], ganancias[i])
            ganancia1[i] = max(ganancia1[i - 1], ganancias[i + 1])
        else:
            ganancia0[i] = max(ganancia0[i - 1], ganancia0[i - 2] + ganancias[i])
            ganancia1[i] = max(ganancia1[i - 1], ganancia1[i - 2] + ganancias[i + 1])
    
    if ganancia0[-1] >= ganancia1[-1]:
        ganancia = ganancia0
        offset = 0
    else:
        ganancia = ganancia1
        offset = 1

    camino = []
    i = len(ganancia0) - 1
    while i >= 0:
        if i == 0 or ganancia[i] != ganancia[i - 1]:
            camino.append(i + offset)
            i -= 2
        else:
            i -= 1

    return camino[::-1]

def main():
    print(lunatico([]))
    print(lunatico([100]))
    print(lunatico([100, 120]))
    print(lunatico([100, 120, 150, 110, 110, 190]))
    print(lunatico([200, 250, 10]))
    print(lunatico([200, 50, 45, 200, 30]))

if __name__ == "__main__":
    main()