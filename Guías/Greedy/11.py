from heapq import heappush, heappop

"""
    Mi algoritmo consiste en, iterativamente, ir guardando los elementos
de mayor peso en bolsas. A estas, primero se las intenta llenar y, si
no es posible guardar el elemento en una bolsa ya utilizada, se utiliza
una nueva. De esta forma se consigue un algoritmo que, mediante la
aplicación de la técnica Greedy, permite obtener una solución optima al
problema, en una complejidad máxima de O(n log n).

Productos: [4, 2, 1, 3, 5]
Peso max.: 5

CANDIDATO PRINCIPAL (OPTIMA):
Ordeno por mayor a menor peso y voy guardando en las bolsas ya usadas si sobra espacio o agarro una nueva si no sobra:
(5), (4), (3)
(5), (4), (3, 2)
(5), (4, 1), (3, 2)

OTRA OPCIÓN (NO OPTIMA):
Ordeno de menor a mayor peso y voy gardando en las bolsas ya usadas si sobra espacio o agarro una nueva si no sobra:
(1, 2), (3), (4), (5)
"""

def bolsas(capacidad, productos):
    productos.sort(key=lambda x: -x)
    bolsas = []

    for producto in productos:
        if bolsas and bolsas[0][0] + producto <= capacidad:
            espacio, elementos = heappop(bolsas)
            heappush(bolsas, (espacio + producto, elementos + [producto]))
        else:
            heappush(bolsas, (producto, [producto]))
    
    for i in range(len(bolsas)):
        bolsas[i] = bolsas[i][1]
    return bolsas

def main():
    print(bolsas(5, [4, 2, 1, 3, 5]))
    print(bolsas(5, []))

if __name__ == "__main__":
     main()