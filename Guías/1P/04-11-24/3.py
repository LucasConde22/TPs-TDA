"""
[50, 50]
[50, 30, 60, 45, 60, 50]
[1, 2, 9, 1, 2, 7, 1, 2, 8]


[50, 30, 60, 45, 60, 50]

[50, 30, 60] [45, 60, 50]

[50, 30] [60]     [45, 60] [50]

[50]   [30]   [60]   [45]  [60]   [50]

50     30      60     45    60     50
50     30      60     45    60     50

  30        60        45      50
  30        60        60      50

  30                    45
  60                    60

        30
        60
"""

def compra_venta(p):
    if len(p) == 0:
        return None, None
    return _compra_venta_dyc(0, len(p) - 1, p)

def _compra_venta_dyc(ini, fin, p):
    if ini == fin:
        return ini, fin
    
    medio = (ini + fin) // 2

    compra_izq, venta_izq = _compra_venta_dyc(ini, medio, p)
    compra_der, venta_der = _compra_venta_dyc(medio + 1, fin, p)

    ganancia_izq = p[venta_izq] - p[compra_izq]
    ganancia_der = p[venta_der] - p[compra_der]
    
    ganancia_inter = 0
    venta_inter = compra_izq
    for i in range(compra_izq + 1, venta_der + 1):
        if p[i] - p[compra_izq] > ganancia_inter:
            ganancia_inter = p[i] - p[compra_izq]
            venta_inter = i

    if ganancia_izq == ganancia_inter == ganancia_der:
        if p[compra_izq] < p[compra_der]:
            return compra_izq, venta_der
        return compra_der, venta_der

    if ganancia_izq < ganancia_inter > ganancia_der:
        return compra_izq, venta_inter

    if ganancia_izq > ganancia_der:
        return compra_izq, venta_izq

    return compra_der, venta_der
    

def main():
    print(compra_venta([]))
    print(compra_venta([50, 50]))
    print(compra_venta([50, 30, 60, 45, 60, 50]))
    p = [1, 2, 9, 1, 2, 7, 1, 2, 8]
    inicio, fin = compra_venta(p) # inicio = 0, fin = 2
    print(inicio, fin)

    p = [9, 11, 50, 28]
    inicio, fin = compra_venta(p)
    print(inicio)
    print(fin)

    p = [10, 9, 8, 5, 2, 7, 9]
    inicio, fin = compra_venta(p)
    print(inicio, 3)
    print(fin, 6)

    p = [2, 2, 9, 1, 2, 17, 1, 2, 8]
    inicio, fin = compra_venta(p)
    print(inicio)
    print(fin)


if __name__ == "__main__":
    main()