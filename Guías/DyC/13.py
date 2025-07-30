"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(N) = 2 * T(N/2) + O(N),
llamo recursivamente partiendo el arreglo en dos
partes, izq y der, hasta llegar al caso base (1
elemento). Volviendo en la recursión, encuentro el
subarreglo de suma máxima entre la intersección del
subarreglo izq. y el der (O(N)). Finalmente, retorno
el rango del subarreglo (los rangos) con suma máxima.

con T.M: log2(2) = 1 -> O(N log N)
"""

def max_subarray(arr):
   inicio, fin, _ = _max_subarray(arr, 0, len(arr) - 1)
   return arr[inicio : fin + 1]

def _max_subarray(arr, ini, fin):
    if ini == fin:
        return ini, fin, arr[ini]
    
    medio = (ini + fin) // 2
    ii, fi, si = _max_subarray(arr, ini, medio)
    id, fd, sd = _max_subarray(arr, medio + 1, fin)

    iinter, finter, sinter = _hallar_suma(arr, ii, medio, fd) # Hallo la suma de la intersección de izq. y der.

    if sinter > si and sinter > sd:
        return iinter, finter, sinter
    if si > sd:
        return ii, fi, si
    return id, fd, sd

def _hallar_suma(arr, ini, medio, fin):
    ni, si, sact = None, float('-inf'), 0
    for i in range(medio, ini - 1, -1):
        sact += arr[i]
        if sact > si:
            si = sact
            ni = i
    
    nf, sd, sact = None, float('-inf'), 0
    for i in range(medio + 1, fin + 1):
        sact += arr[i]
        if sact > sd:
            sd = sact
            nf = i

    return ni, nf, si + sd

def main():
    print(max_subarray([5, 3, 2, 4, -1]))
    print(max_subarray([5, 3, -5, 4, -1]))
    print(max_subarray([5, -4, 2, 4, -1]))
    print(max_subarray([5, -4, 2, 4]))
    print(max_subarray([-3, 4, -1, 2, 1, -5]))

    print(max_subarray([-3, 4, -1, 2, 1, -5, 4])) # [4, -1, 2, 1]

if __name__ == "__main__":
    main()