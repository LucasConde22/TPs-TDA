"""
Complejidad:
O(n), siendo n el largo de la cadena.

¿Es Greedy?:
Mi algortimo es Greedy ya que dado el estado inicial, que es el de 0 secuencias
balanceadas, se itera la cadena tomando la decisión de agregar o no a la
cantidad de secuencias balanceadas encontradas hasta el momento de manera en que
se maximize el prefijo balanceado más largo hasta el momento y se avance, sin
necesidad de mirar atrás elgiendo siempre la opción localmente más óptima hasta
que, finalmente, se halle una solución óptima global.

¿Es óptimo?:
Si, empezar si o si desde el inicio de la cadena hace que siempre se encuentre
una solución óptima. En cambio, si se deseara encontrar el prefijo balanceado
más largo de la cadena, empezando desde cualquier posición, no se podría hallar
solución óptima utilizando una técnica Greedy.
"""

def prefijo_balanceado_mas_largo(cadena):
    mas_largo, balance = 0, 0

    for i in range(len(cadena)):
        if cadena[i] == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            break

        if balance == 0:
            mas_largo = i + 1

    return mas_largo

def main():
    print(prefijo_balanceado_mas_largo("()())(())()(()"))
    print(prefijo_balanceado_mas_largo("()()(())(("))
    print(prefijo_balanceado_mas_largo(")"))
    print(prefijo_balanceado_mas_largo("(()"))

if __name__ == "__main__":
    main()