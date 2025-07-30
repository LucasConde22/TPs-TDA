"""
    Mi algoritmo consiste en ordenar el arreglo e
iterarlo, seleccioando en cada iteración la opción
más optima en ese momento. Esta selección parcial
consiste en elegir el producto con mayor valor
disponible, ya que, con el pasar de los
días, es el que aumentará en mayor cantidad su
costo. De esta forma, logro aplicar un algoritmo
Greedy, que permite llegar a una solución optima
global, que minimizando costo total de comprar todos
los productos.
    La complejidad final del mismo es O(n log n),
debido al ordenamiento inicial. Puesto que, luego,
se realizan otrar operaciones pero, en conjunto,
solo ocupan una complejidad de O(n).
"""

def precios_inflacion(R):
    total = 0
    R.sort()
    for i in range(len(R)):
        total += R[len(R) - i - 1]**(i + 1)
    return total

def main():
    print(precios_inflacion([3, 9, 11, 2, 1, 20]))

if __name__ == "__main__":
    main()