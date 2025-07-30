"""
    El algoritmo primero ordena el arreglo de mayor a menor y luego, recorre
el arreglo asignando la mayor cantidad de monedas que puede para "llenar" lo
máximo posible el monto restante. De esta forma, el algoritmo es Greedy, ya
que intenta, en la iteración de cada elemento, encuentrar optimos locales
(el máximo de monedas de cada denominación), que luego forman una solución
global.
    La solución global que acabo de mencionar sirve para aproximarse a un
resultado optimo y, en muchos casos, esta solución puede que sea optima.
Sin embargo, el problema no puede resolverse de forma Greedy encontrando
siempre soluciones optimas. Por ejemplo:
    Si el monto es 14 y las monedas disponibles son [10, 7, 3, 1], el
resultado será [10, 3, 1], el cuál no es optimo. En cambio, una solución
verdaderamente ooptima sería [7, 7].
    En cuanto a la complejidad, primero se realiza un ordenamiento
(O(n log n)) y luego se lo recorre, insertando en el resultado final las M
monedas necesarias de cada denominación. De esta forma se obtiene una
complejidad resultante de O(max(n log n, n*m)).
"""

def cambio(monedas, monto):
    monedas.sort(reverse=True)
    cambio = []

    for moneda in monedas:
        cambio += [moneda] * (monto // moneda)
        monto = monto % moneda

    return cambio

def main():
    print(cambio([2000, 1000, 500, 100, 200, 50, 25, 10000, 10], 4500))

if __name__ == "__main__":
    main()