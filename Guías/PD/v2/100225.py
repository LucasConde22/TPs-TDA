"""
OPT(0) = 0
OPT(i) = max(OPT(i - 1), secuencia(i))

Caso base:
El óptimo de una expresión de largo 0 es 0.

Caso general:
El óptimo en la i-ésima posible posición de inicio
consiste en el ópimo entre el largo de la secuencia
balanceada más larga de su predecesor (i - 1) y el
largo de la obtenida iniciando en la posición i.
"""

def secuencia_balanceada_mas_larga(expresion):
    pila = []
    mejor, inicio = 0, 0
    for i in range(len(expresion)):
        if expresion[i] == "(":
            pila.append("(")
        else:
            if len(pila) == 0:
                inicio = i
            else:
                pila.pop()
                if len(pila) == 0:
                    mejor = max(mejor, i - inicio)
    return mejor

def main():
    print(secuencia_balanceada_mas_larga("()())(())()(()"))

if __name__ == "__main__":
    main()
