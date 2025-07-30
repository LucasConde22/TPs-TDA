def validador_maximo(arreglo, max): # O(N)
    esta = False
    for num in arreglo:
        if num > max:
            return False
        elif num == max:
            esta = True
    return esta

def validador_ordenado(original, ordenado): # O(N)
    if len(original) != len(ordenado):
        return False
    
    if len(original) == 0:
        return True

    elementos = {}
    for n in original:
        elementos[n] = elementos.get(n, 0) + 1

    if ordenado[0] not in elementos:
        return False
    else:
        elementos[ordenado[0]] -= 1

    for i in range(1, len(ordenado)):
        if ordenado[i] not in elementos or ordenado[i] < ordenado[i - 1] or elementos[ordenado[i]] == 0:
            return False
        elementos[ordenado[i]] -= 1
    return True

def validador_nreinas(reinas, n): # O(N^2)
    if len(reinas) > n:
        return False

    for i, (x1, y1) in enumerate(reinas):
        for j, (x2, y2) in enumerate(reinas):
            if i == j:
                continue
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True

def main():
    print("Pruebas validador_maximo:")
    arr, n = [1, 3, 2, 8, 10, 11, -3], 11
    print(f'{arr} y {n}: True -> {validador_maximo(arr, n)}')  
    n = 15
    print(f'{arr} y {n}: False -> {validador_maximo(arr, n)}')
    n = 8
    print(f'{arr} y {n}: False -> {validador_maximo(arr, n)}')

    print("\nPruebas validador ordenado:")
    arr, arr2 = [1, 3, 2, 8, 10, 11, -3], [-3, 1, 2, 3, 8, 10, 11]
    print(f'{arr} y {arr2}: True -> {validador_ordenado(arr, arr2)}')  
    arr2 = [1, -3, 2, 3, 8, 10, 11]
    print(f'{arr} y {arr2}: False -> {validador_ordenado(arr, arr2)}') 
    arr2 = [-3, 1, 2, 3, 8, 10, 12]
    print(f'{arr} y {arr2}: False -> {validador_ordenado(arr, arr2)}') 
    arr2 = [1, -3, 2, 3, 8, 11, 10]
    print(f'{arr} y {arr2}: False -> {validador_ordenado(arr, arr2)}') 

    print("\nPruebas validador_nreinas:")
    reinas, n = [(0, 1), (1, 3), (2, 0), (3, 2)], 4
    print(f'{reinas} y {n}: True -> {validador_nreinas(reinas, n)}') 
    n = 3
    print(f'{reinas} y {n}: False -> {validador_nreinas(reinas, n)}') 
    reinas, n = [(0, 1), (0, 3), (2, 0), (3, 2)], 4
    print(f'{reinas} y {n}: False -> {validador_nreinas(reinas, n)}') 
    reinas, n = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3), (5, 8), (6, 10), (7, 12), (8, 17), (9, 19), (10, 21), (11, 18), (12, 20), (13, 9), (14, 7), (15, 5), (16, 22), (17, 6), (18, 15), (19, 11), (20, 14), (21, 16), (22, 13)], 23
    print(f'{reinas} y {n}: True -> {validador_nreinas(reinas, n)}') 

if __name__ == "__main__":
    main()