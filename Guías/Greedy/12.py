"""
    Posee la misma lógica que el ejercicio de scheduling. Primero,
se ordena la lista y luego, la parte Greedy, consiste en iterarla
seleccionando, en cada caso, la mafia cuyo fin se encuentre más
próximo y su inicio sea compatible con el fin de la anterior. De
esta manera, agarro optimos locales que luego conforman una
solución global optima que maximiza la cantidad de pedidos
otorgados, ignorando la cantidad de kilómetros otorgados.
    La complejidad final del algoritmo es O(n log n), debido a
que presenta un ordenamiento en el comienzo. Luego, la parte
Greedy, es O(n) y, por lo tanto, no influye a la complejidad
final.
"""

# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
    pedidos.sort(key=lambda x: x[1])
    asignacion = []

    for pedido in pedidos:
        if not asignacion or asignacion[-1][1] <= pedido[0]:
            asignacion.append(pedido)

    return asignacion

def main():
    print(asignar_mafias([(1, 3.5), (3.33, 8), (5, 8), (9, 10), (1, 5)]))

if __name__ == "__main__":
    main()
