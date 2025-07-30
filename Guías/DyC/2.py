"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(n) = 1 * T(N/2) + O(1),
ya que divido en dos partes y llamo recursivamente
a una mitad o la otra dependiendo del resultado de
la comparación realizada.

con T.M: log2(1) = 0 -> O(log n)
"""

def indice_primer_cero(arr):
    return _indice_primer_cero(arr, 0, len(arr) - 1)

def _indice_primer_cero(arr, ini, fin):
    if ini > fin:
        return -1

    medio = (ini + fin) // 2

    if arr[medio] == 0:
        if medio == 0 or arr[medio - 1] == 1:
            return medio
        return _indice_primer_cero(arr, ini, medio - 1)
    return _indice_primer_cero(arr, medio + 1, fin)

def main():
    arr = [1, 1, 1, 1, 1, 1, 0, 0]
    print(indice_primer_cero(arr))

    arr = [0, 0]
    print(indice_primer_cero(arr))

    arr = [1]
    print(indice_primer_cero(arr))

    arr = [1, 1, 1, 1, 1, 1]
    print(indice_primer_cero(arr))

    arr = [1, 0, 0]
    print(indice_primer_cero(arr))

if __name__ == "__main__":
    main()