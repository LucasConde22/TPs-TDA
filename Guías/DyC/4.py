"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(N) = 1 * T(N/2) + O(1),
ya que divido en dos partes y llamo recursivamente
a una mitad o la otra dependiendo del resultado de
la comparación realizada.

con T.M: log2(1) = 0 -> O(log n)
"""

def posicion_pico(v, ini, fin):
    # Como el arreglo tiene largo necesariamente >= 3, no debería ser necesario resolver un caso base.
    medio = (ini + fin) // 2

    if v[medio] > v[medio + 1]:
        if v[medio] > v[medio - 1]:
            return medio
        return posicion_pico(v, ini, medio)
    return posicion_pico(v, medio + 1, fin)

def main():
    arr = [1, 2, 3, 1, 0, -2]
    print(posicion_pico(arr, 0, len(arr) - 1))


    arr = [1, 2, 3, 4, 5, 0]
    print(posicion_pico(arr, 0, len(arr) - 1))

    arr = [1, 2, 1, 0, -2]
    print(posicion_pico(arr, 0, len(arr) - 1))

    arr = [1, 0, -1]
    print(posicion_pico(arr, 0, len(arr) - 1))

if __name__ == "__main__":
    main()