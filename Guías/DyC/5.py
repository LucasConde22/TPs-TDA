"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(N) = 2 * T(N/2) + O(N),
ya que divido en dos partes que luego llamo
recursivamente. En cada llamado se realizan O(N)
operaciones.

con T.M: log2(2) = 1 -> O(n log n)
"""

def merge_sort(arr):
    if not arr:
        return []
    return _merge_sort(arr, 0, len(arr) - 1)

def _merge_sort(arr, ini, fin):
    if ini == fin:
        return [arr[ini]]

    medio = (ini + fin) // 2
    return _merge(_merge_sort(arr, ini, medio), _merge_sort(arr, medio + 1, fin))

def _merge(izq, der):
    arr = []
    i, j = 0, 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            arr.append(izq[i])
            i += 1
        else:
            arr.append(der[j])
            j += 1
    return arr + izq[i:] + der[j:]


def main():
    print(merge_sort([1, 5, 3, 8, 0, 1, 20, 4]))

    print(merge_sort([]))

    print(merge_sort([1]))

    print(merge_sort([1, 2, 3]))

    print(merge_sort([8, 2, 4, 0, 100, 60, 70, -1, 70]))

if __name__ == "__main__":
    main()