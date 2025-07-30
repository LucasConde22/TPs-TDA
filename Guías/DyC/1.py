"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(n) = 2 * T(N/2) + O(1),
ya que divido en dos partes y llamo recursivamente
para cada mitad. En cada llamado se realizan O(1)
operaciones. Por lo tanto, en el peor de los casos,
se "iteraría" cada elemento. Entonces, la complejidad
es O(n).

con T.M: log2(2) > 0 -> O(n)
"""

def elemento_desordenado(arr):
    return _elemento_desordenado(arr, 0, len(arr) - 1)

def _elemento_desordenado(arr, ini, fin):
    if ini >= fin:
        return None
    
    medio = (ini + fin) // 2

    if arr[medio] > arr[medio + 1]:
        if medio - 1 >= 0 and arr[medio + 1] < arr[medio - 1]:
            return arr[medio + 1]
        return arr[medio]
    
    izq = _elemento_desordenado(arr, ini, medio)
    if izq:
        return izq
    return _elemento_desordenado(arr, medio + 1, fin)

def main():
    arr = [1, 2, 3, 6, 4, 5]
    print(elemento_desordenado(arr)) # 6

    arr = [1, 2, 3, 4, 5]
    print(elemento_desordenado(arr)) # None

    arr = [1, 2, 3, 4, 5, 0]
    print(elemento_desordenado(arr)) # 0

    arr = [1, 2, 3, 0, 4, 5]
    print(elemento_desordenado(arr)) # 0

    arr = [3, 1, 2]
    print(elemento_desordenado(arr)) # 3

if __name__ == "__main__":
    main()