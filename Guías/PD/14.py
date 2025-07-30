"""
Complejidad : O(N), siendo N la cantidad de casas en el arreglo 'ganancias'.
Ecuación de recurrencia:
        Si N == 0 -> []
        Si N = 1 -> [0]
        Si N = 2 -> [indice de max(G[0], G[1])]
        Si N >= 3 -> max(ganancia(G[:-1], ganancia[1:])),
                    donde cada OPT(j) = max(OPT(j-1), OPT(j-2) + G[j])

"""
def lunatico(ganancias):
    if len(ganancias) == 0:
        return []
    if len(ganancias) == 1:
        return [0]
    if len(ganancias) == 2:
        return [0] if ganancias[0] >= ganancias[1] else [1]

    sol1 = obtener_ganancias(0, len(ganancias) - 1, ganancias)
    sol2 = obtener_ganancias(1, len(ganancias), ganancias)
    if sol1[-1] >= sol2[-1]:
        sol, offset = sol1, 0
    else:
        sol, offset = sol2, 1

    casas, restante, i = [], sol[-1], len(sol) - 1
    while restante != 0:
        if sol[i] == sol[i - 1]:
            i -= 1
            continue

        casas.append(i + offset)
        restante -= ganancias[i + offset]
        i -= 2

    return casas[::-1]

def obtener_ganancias(ini, fin, ganancias):
    ante_anterior, anterior, sol = 0, 0, []
    for i in range(ini, fin):
        sol.append(max(ante_anterior + ganancias[i], anterior))
        ante_anterior, anterior = anterior, sol[-1]
    return sol


def main():
    print(lunatico([]))
    print(lunatico([100]))
    print(lunatico([100, 120]))
    print(lunatico([100, 120, 150, 110, 110, 190]))
    print(lunatico([200, 250, 10]))
    print(lunatico([200, 50, 45, 200, 30]))

if __name__ == "__main__":
    main()