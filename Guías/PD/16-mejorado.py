# Complejidad: O(N^2), siendo N la cantidad de elementos del arreglo P.
def compra_venta(p):
    if len(p) == 0:
        return None, None

    ganancias = [0] * len(p)

    for k in range(len(p)):
        for j in range(k + 1, len(p)):
            ganancias[j] =  (max(ganancias[j-1], ganancias[j], p[j] - p[k]))

    d_compra, d_venta = 0, 0
    for i in range(len(ganancias) - 1, 0, -1):
        if ganancias[i] == ganancias[i - 1]:
            continue
        d_venta = i
        for j in range(i, -1, -1):
            if p[i] - ganancias[i] == p[j]:
                d_compra = j
                break
        break
    return d_compra, d_venta


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