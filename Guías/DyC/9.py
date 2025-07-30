"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(N) = 2 * T(N/2) + O(N),
llamo recursivamente partiendo el arreglo en dos
partes, izq y der, hasta llegar al caso base (1
elemento). Luego, utilizo estos elementoa como
"candidatoa" y volviendo en la recursividad
"cuento" si alguno aparece mas de la mitad de las
veces.

con T.M: log2(2) = 1 -> O(n log n)
"""

def mas_de_la_mitad(arr):
    aparece, _ = _mas_de_la_mited(arr, 0, len(arr) - 1)
    return aparece

def _mas_de_la_mited(arr, ini, fin):
    if ini == fin:
        return True, arr[ini]
    
    medio = (ini + fin) // 2
    izq, ci = _mas_de_la_mited(arr, ini, medio)
    der, cd = _mas_de_la_mited(arr, medio + 1, fin)

    if izq and _aparece_mas_mitad(arr, ci, ini, fin):
        return True, ci
    if der and _aparece_mas_mitad(arr, cd, ini, fin):
        return True, cd
    return False, None

def _aparece_mas_mitad(arr, candidato, ini, fin):
    apariciones = 0
    for i in range(ini, fin + 1):
        if arr[i] == candidato:
            apariciones += 1
    return apariciones > (fin - ini + 1) // 2
    
def main():
    print(mas_de_la_mitad([1, 2, 1, 2, 3])) # False
    print(mas_de_la_mitad([1, 1, 2, 3])) # False
    print(mas_de_la_mitad([1, 2, 3, 1, 1, 1])) # True
    print(mas_de_la_mitad([1])) # True
    print(mas_de_la_mitad([4, 4])) # True
    print(mas_de_la_mitad([1, 2])) # False
    print(mas_de_la_mitad([1, 2, 1, 4, 1, 6, 1, 1])) # True


if __name__ == "__main__":
    main()