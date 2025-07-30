# La entrega que hice en RPL funciona pero no mediante PD.
def cambio(monedas, monto):
    if monto == 0:
        return []

    monedas.sort()
    memoization = {}
    min_cambio = None

    for i in range(len(monedas)):
        cambio, restante = [], monto
       
        for j in range(i, -1, -1):
            if (monedas[j], monto) in memoization:
                cambio += [monedas[j]] * memoization[(monedas[j], monto)][0]
                restante = memoization[(monedas[j], monto)][1]
            else:
                necesarias = restante // monedas[j]
                restante = restante % monedas[j]

                cambio += [monedas[j]] * necesarias
                memoization[(monedas[j], monto)] = (necesarias, restante)

        if not min_cambio or len(cambio) < len(min_cambio):
            min_cambio = cambio[:]

    return min_cambio

def main():
    print(cambio([10, 2, 7, 1], 15))

if __name__ == "__main__":
    main()


