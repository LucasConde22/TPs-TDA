"""
Ecuación de recurrencia:
    T(n) = 2 * T(n/2) + O(n)

Por teorema maestro, como log2(2) = 1 -> T(n) = O(n * log(n))
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
    compra_inter, venta_inter = _compra_venta_inter(ini, medio, fin, p)

    ganancia_izq = p[venta_izq] - p[compra_izq]
    ganancia_der = p[venta_der] - p[compra_der]
    ganancia_inter = p[venta_inter] - p[compra_inter]

    if ganancia_izq < ganancia_inter > ganancia_der:
        return compra_inter, venta_inter
    
    if ganancia_izq > ganancia_der:
        return compra_izq, venta_izq

    return compra_der, venta_der 

def _compra_venta_inter(ini, medio, fin, p):
    compra_inter, venta_inter = ini, medio + 1
    for i in range(ini + 1, medio + 1):
        compra_inter = i if p[i] < p[compra_inter] else compra_inter
    for i in range(medio + 2, fin + 1):
        venta_inter = i if p[i] > p[venta_inter] else venta_inter
    return compra_inter, venta_inter
 
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
    
    