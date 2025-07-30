"""
Complejidad:
    _buscar_donde_insertaria -> O(log(n)) (Búsqueda binaria)
    _definir_mas_cercanos -> O(k) (hago k iteraciones de elems. del arreglo)

    buscar_k_cercanos -> O(log(n) + k) = O(min(log(n), k)) (con k < n)
"""

def buscar_k_cercanos(arr, k):
    return _definir_mas_cercanos(arr, _buscar_donde_insertaria(arr, k, 0, len(arr) - 1), k)

def _buscar_donde_insertaria(arr, k, ini, fin):
    if ini >= fin:
        return ini

    medio = (ini + fin) // 2

    if arr[medio] <= k <= arr[medio + 1]:
        return medio
    
    if k < arr[medio]:
        return _buscar_donde_insertaria(arr, k, ini, medio)
    
    return _buscar_donde_insertaria(arr, k, medio + 1, fin)
    
def _definir_mas_cercanos(arr, pos, k):
    selecionados = []
    izq, der = pos, pos + 1

    while len(selecionados) < k:
        if izq < 0 or arr[der] - k <= k - arr[izq]:
            selecionados.append(arr[der])
            der += 1
        else:
            selecionados.append(arr[izq])
            izq -= 1

    return selecionados

def main():
    print(buscar_k_cercanos([1, 3, 4, 7, 8, 9, 12, 13, 14, 20, 30], 5))
    print(buscar_k_cercanos([1, 3, 4, 7, 8, 9, 12, 13, 14, 20, 30], 8))
    print(buscar_k_cercanos([1, 3, 4, 7, 8, 9, 12, 13, 14, 20, 30], 0))
    print(buscar_k_cercanos([20, 30, 40, 50, 60, 70], 3))
    print(buscar_k_cercanos([2, 3, 4, 5, 6, 7], 4))

if __name__ == "__main__":
    main()