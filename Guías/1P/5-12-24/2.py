from heapq import heapify, heappush, heappop

"""
Complejidad:
    O(n * log n), siendo n la cantidad de congeladores/compuestos inicial (que 
    inicialmente es la misma).

¿Es Greedy?
    Si, el algoritmo implementado es Greedy. Esto se debe a que dado el estado
    inicial, de n componentes en n congeladores, se busca acumular el mínimo costo de
    perdida siguiendo la sencilla regla de mover siempre el contenido del congelador
    cuya cantidad potencial de peridas sea menor hacia el segundo con menores perdidas
    potenciales. De esta manera, se obtiene una sucesión de óptimos locales que
    finalizan encontrando la solución global, que consiste en el número de perdidas
    totales minimizadas al máximo (y, si se guardaran los elementos, podríamos saber
    en qué congelador terminaron estos o, si se guardaran los movimientos, cuál debería
    ser la sucesión de movimientos que Tati debería realizar).

¿Es óptimo?
    Si, el algoritmo implementado el óptimo. Supongamos que se tienen tres congeladores,
    cada uno de ellos con un número de perdidas por unidad donde c1 < c2 < c3. Pero,
    ignorando a nuestro algoritmo, movemos el contenido del congelador 2 al congelador 3.
    Esto nos daría una perdida acumulada de c2 + c3 que, luego, al mover c1 al congelador
    3 obtendríamos una nueva perdida acumulada (y ahora final) de (c2 + c3) + (c1 + c2 + c3),
    que consisitiría en el costo del nuevo movimiento más el costo del movimiento anterior.
    En cambio, si hubiesemos seguido a nuestro algoritmo, primero habríamos movido el
    contenido del congelador 1 al congelador 2, con un costo de c1 + c2, y luego del
    congelador 2 al congelador 3, con un costo final de (c1 + c2) + (c1 + c2 + c3). Que,
    dada nuestra primera definición de que c1 < c2 < c3, se puede observar que implicaría
    un costo total menor al que conseguimos al no seguir a nuestro algoritmo.

Aclaración:
    Congeladores es una lista donde cada uno de sus elementos representa el costo de
    perdida por unidad de tiempo del componente en el i-esimo congelador. Durante mi
    algoritmo, a medida que acumulo componentes en un mismo congelador, acumulo sus
    valores de perdida en un único elemento (sin guardar qué elementos contiene).
    Esto consiste simplemente en una optimización, podrían mantenerse separados pero
    el costo de obtener la perdida total de mover estos resultaría O(k), siendo k la
    cantidad de compuestos en el congelador:

    Por ejemplo:
       Si
            congeladores = [pc1, pc2, pc3]
       Al mover c1 del primer congelador al segundo congelador:
            congeladores = [pc1 + pc2, pc3]

    Como se puede observar, los congeladores vacíos quedan descartados, ya que carece
    de sentido volverlos a utilizar.
"""
def obtener_minimas_perdidas(congeladores):
    congeladores = congeladores[:] # Realizo una copia para no modificar la lista original
    heapify(congeladores)

    costo_total = 0
    while len(congeladores) > 1:
        costo_movimiento = heappop(congeladores) + heappop(congeladores)
        costo_total += costo_movimiento
        heappush(congeladores, costo_movimiento)

    return costo_total

def main():
    print(obtener_minimas_perdidas([5, 4, 6, 2, 9]))

if __name__ == "__main__":
    main()
