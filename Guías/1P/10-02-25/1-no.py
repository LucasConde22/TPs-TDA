"""
Complejidad:
O(n), siendo n el largo de la cadena.

¿Es Greedy?:
Mi algortimo es Greedy ya que dado el estado inicial, que es el de 0 secuencias
balanceadas, itera el arreglo (cadena) y para cada caracter decide si este finaliza
una secuencia, caso para el cuál aumenta el número de secuencias encontradas (suma 
2 porque cada secuencia se forma por dos caracteres), o si arranca una secuencia (caso
en el que se apila el nuevo caracter para luego seguir buscando su "cierre"). De esta
forma se logra encontrar la sucesión de secuencias balanceadas (óptimos locales) que
finalmente permiten determinar el número total del prefijo balanceado más largo.

¿Es óptimo?:
    El algoritmo es óptimo siempre y cuando se comience con una secuencia que luego
sea efectivamente terminada (cerrada). Por ejemplo, el siguiente ejemplo daría por
resultado un 2 cuando, en realidad, debería ser 0: ((). Ya que se contaria la parte
() de las posiciones 1 y 2, pero quedaría el ( de la posición 0, que debería anular toda
la solución.
"""

def prefijo_balanceado_mas_largo(cadena):
    contador = 0
    pila = []

    for c in cadena:
        if c == '(':
            pila.append('(')
        else:
            if pila and pila.pop() == '(':
                contador += 2
            else:
                return contador
    return contador

def main():
    print(prefijo_balanceado_mas_largo("()())(())()(()"))
    print(prefijo_balanceado_mas_largo("()()(())(("))
    print(prefijo_balanceado_mas_largo(")"))
    print(prefijo_balanceado_mas_largo("(()"))

if __name__ == "__main__":
    main()