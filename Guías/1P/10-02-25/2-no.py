"""
Complejidad: O(n^2), siendo n el largo de la cadena.
Ecuación de recurrencia:
                OPT(j) = max(OPT(j - 1), B(j))
                Siendo j el índice de inicio, OPT(j) esta dado por el
                máximo entre el óptimo arrancando por el índice
                anterior (por eso se la memoriza) y la subsecuencia más
                larga arrancando por j (B(j)), que se encuentra
                utilizando el algoritmo greedy (con mínimas
                modificaciones) del ejercicio anterior.
"""

def prefijo_balanceado_mas_largo(cadena):
    maximo = 0
    ini = 0
    while ini < len(cadena):
        largo, fin = _busqueda_greedy(ini, cadena)
        maximo = largo if largo > maximo else maximo
        ini = fin

    return maximo


def _busqueda_greedy(ini, cadena):
    mas_largo, balance = 0, 0

    for i in range(ini, len(cadena)):
        if cadena[i] == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return mas_largo, i

        if balance == 0:
            mas_largo = i + 1 - ini

    return mas_largo, len(cadena)

def main():
    print(prefijo_balanceado_mas_largo("()())(())()(()"))
    print(prefijo_balanceado_mas_largo("()()(())(("))
    print(prefijo_balanceado_mas_largo(")"))
    print(prefijo_balanceado_mas_largo("(()"))

if __name__ == "__main__":
    main()