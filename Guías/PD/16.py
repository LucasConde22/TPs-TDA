def compra_venta(p):
    if len(p) == 0:
        return None, None

    matriz = [] # Las filas representan el día de compra del i-esimo elem. y las col. el día de venta.

    for fil in range(len(p)):
        matriz.append([])
        for col in range(len(p)):
            arr = matriz[fil-1][col] if fil > 0 else 0
            izq = matriz[fil][col-1] if col > 0 else 0
            act = p[col] - p[fil] if col > fil else 0
            matriz[fil].append(max(arr, izq, act)) # Me quedo con el máximo entre ady. izq., el de arriba y el actual.

    fil, col = len(matriz) - 1, len(matriz[0]) - 1

    while matriz[fil][col] != 0:
        if fil > 0 and matriz[fil][col] == matriz[fil - 1][col]:
            fil -= 1
            continue

        if col > 0 and matriz[fil][col] == matriz[fil][col - 1]:
            col -= 1
            continue

        return fil, col
    return 0, 0


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

if __name__ == "__main__":
    main()