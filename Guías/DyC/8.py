"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(N) = 2 * T(N/2) + O(N),
ya que llamo recursivamente 2 veces en cada
recursión y realizo operaciones O(N), mergear y
contar. Adicionalmente, también realizo la
operación de asignar indices al comienzo de la
función principal, la cual es O(N).

con T.M: log2(2) = 1 -> O(n log n)

Es, en esencia, un MergeSort modificado.
"""

def contar_inversiones(A, B):
    _, inversiones = _contar_inversiones(B, _encontrar_indices(A), 0, len(B) - 1)
    return inversiones

def _encontrar_indices(arr):
    indices = {}
    for i, elem in enumerate(arr):
        indices[elem] = i
    return indices

def _contar_inversiones(arr, indices, ini, fin):
    if ini >= fin:
        return arr[ini:fin+1], 0

    medio = (ini + fin) // 2
    izq, invi = _contar_inversiones(arr, indices, ini, medio)
    der, invd = _contar_inversiones(arr, indices, medio + 1, fin)
    arreglo, inv = _contar_y_mergear(indices, izq, der)
    return arreglo, inv + invi + invd

def _contar_y_mergear(indices, izq, der):
    arr, conteo = [], 0
    i, j = 0, 0
    while i < len(izq) and j < len(der):
        if indices[izq[i]] < indices[der[j]]:
            arr.append(izq[i])
            i += 1
        else:
            arr.append(der[j])
            j += 1
            conteo += len(izq) - i
    return arr + izq[i:] + der[j:], conteo

def main():
    print(contar_inversiones([1, 2, 3, 4, 5, 6, 7, 8], [7, 3, 5, 2, 1, 8, 4, 6]))
    print(contar_inversiones([1, 2, 3], [1, 3, 2]))
    print(contar_inversiones([1, 2, 3, 4], [1, 2, 3, 4]))
    print(contar_inversiones([1, 2, 3, 4, 5], [1, 3, 4, 5, 2]))

if __name__ == "__main__":
    main()