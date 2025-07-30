"""
Complejidad: O(n^2), pudiendose hace en O(n * log(n)) y con n = cantidad de charlas.
Ecuación de recurrencia:
                        OPT(i) = max(OPT(i - 1), Vi + OPT(P(i)),
                        siendo Vi el valor de i y P(i) el índice
                        de la última charla compatible con i.
"""
def scheduling(charlas):
    if len(charlas) == 0:
        return []

    charlas = sorted(charlas, key= lambda x: x[1])
    mejor = []

    for i in range(len(charlas)):
        actual = charlas[i][2]
        for j in range(i - 1, -1, -1):
            if charlas[j][1] <= charlas[i][0]:
                actual += mejor[j]
                break
        anterior = mejor[i - 1] if i > 0 else 0
        mejor.append(max(actual, anterior))

    seleccionadas = []
    restante = mejor[-1]
    i = len(mejor) - 1

    while i >= 0:
        if (i == 0 or mejor[i] != mejor[i - 1]) and (restante == mejor[i]):
            restante -= charlas[i][2]
            seleccionadas.append(charlas[i])
        i -= 1

    return seleccionadas[::-1]

def main():
    print(scheduling([(0, 2, 2), (1, 4, 4), (3, 5, 4), (1, 6, 7), (5, 8, 2), (5, 9, 1)]))
    print(scheduling([(0, 2, 2), (1, 6, 7)]))
    print(scheduling([(0, 2, 2)]))
    print(scheduling([]))
    print(scheduling([(0, 2, 2), (1, 6, 7), (10, 15, 5)]))


if __name__ == "__main__":
    main()
