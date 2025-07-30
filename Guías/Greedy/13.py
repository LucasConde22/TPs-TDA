"""
    Mi algoritmo resuelve el problema de la siguiente forma:
    1. Ordena el arreglo de casas de menor a mayor.
    2. Recorre el arreglo y, si la antena anterior está a
       distancia > a R, coloca una nueva y continúa con la
       iteración. De esta forma logra encontrar soluciones
       optimas locales que le brindan cobertura a cada casa
       y logran extenderla hacia adelante lo máximo posible.
       De esta forma, se minimiza el número de antenas
       utilizadas y se consigue una solución optima global
       mediante la utilización de un algoritmo Greedy.

    Supongamos que hay una mejor solución que la brindada
por este algoritmo. En este caso debería, al menor, haber
una antena que cubra más casas. Lo cuál es imposible, ya que
en este ubicamos las antenas lo más a la derecha posible,
extendiendo y aprovechando al máximo posible su cobertura.
    De esta manera, cualquier solución con menos antenas
dejaría alguna casa sin cobertura y no solventaría el
problema.

    La complejidad del algoritmo es O(n log n), ya que se
realiza un ordenamiento inicial, O(n log n), y luego
operaciones que en conjunto suman una complejidad de O(n).
"""

def cobertura(casas, R, K):
    casas.sort()
    antenas = []

    for casa in casas:
        if not antenas or casa - antenas[-1] > R:
            antenas.append(min(casa + R, K))

    return antenas

def main():
    print(cobertura([2, 3, 5, 7, 9], 4, 10))
    print(cobertura([185, 242, 156, 270, 194], 50, 1000))
    print(cobertura([10, 14], 3, 1000))

if __name__ == "__main__":
    main()


    