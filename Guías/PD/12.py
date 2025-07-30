"""
Complejidad: O(N * 2^log2(P)), algoritmo pseudo-polinomial -> exponencial
Ecuación de recurrencia:
                    Si c = 0:
                        0
                    Si c > 0:
                        OPT(c, P) -> max(OPT(c-1, P), OPT(c-1, P-Ci) + Gi),
                        con P >= Ci, siendo Ci = costo y Gi = ganancia.

                        OPT(i, j) -> OPT(i - 1, j) ∨ OPT(i - 1, j - i)
"""

# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
    if len(c_publicitaria) == 0:
        return []

    matriz = []

    for fil in range(len(c_publicitaria)):
        matriz.append([])
        for col in range(P + 1):
            sin = matriz[fil - 1][col] if fil > 0 else 0
            actual = c_publicitaria[fil][0] if col >= c_publicitaria[fil][1] else 0
            restante = matriz[fil - 1][col - c_publicitaria[fil][1]] if fil > 0 and col >= c_publicitaria[fil][1] else 0
            matriz[-1].append(max(sin, actual + restante))

    for fil in matriz:
        print(fil)
    
    seleccionadas = []
    fil, col = len(matriz) - 1, len(matriz[0]) - 1
    while fil >= 0 and matriz[fil][col] != 0:
        if fil != 0 and matriz[fil][col] == matriz[fil - 1][col]:
            fil -= 1
            continue
        
        seleccionadas.append(c_publicitaria[fil])
        fil, col = fil - 1, col - c_publicitaria[fil][1]
    
    return seleccionadas[::-1]


def main():
    #print(carlitos([], 20))
    #print(carlitos([(100, 5), (200, 1), (300, 7)], 20))
    #print(carlitos([(100, 5), (200, 1), (500, 14), (300, 7), (100, 3), (1, 3)], 20))
    print(carlitos([(5, 5), (3, 3), (7, 7)], 10))

if __name__ == "__main__":
    main()

