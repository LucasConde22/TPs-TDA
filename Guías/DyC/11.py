"""
JUSTIFICACIÓN:
Ver ej. anterior, son exactamente iguales.
"""

def mas_de_dos_tercios(arr):
    return _contar_apariciones(arr, _buscar_candidato(arr), 0, len(arr) - 1) > len(arr) * (2/3)

def _buscar_candidato(arr):
    candidato, apariciones = arr[0], 1
    for elem in arr[1:]:
        if candidato == elem:
            apariciones += 1
        else:
            apariciones -= 1
            if apariciones == 0:
                candidato = elem
                apariciones = 1
    return candidato

def _contar_apariciones(arr, elem, ini, fin):
    if ini == fin:
        if arr[ini] == elem:
            return 1
        return 0
    
    medio = (ini + fin) // 2
    return _contar_apariciones(arr, elem, ini, medio) + _contar_apariciones(arr, elem, medio + 1, fin)

def main():
    print(mas_de_dos_tercios([1, 2, 1, 2, 3])) # False
    print(mas_de_dos_tercios([1, 1, 2, 3])) # False
    print(mas_de_dos_tercios([1, 2, 3, 1, 1, 1])) # False
    print(mas_de_dos_tercios([1, 2, 3, 1, 1, 1, 1])) # True
    print(mas_de_dos_tercios([1])) # True
    print(mas_de_dos_tercios([4, 4])) # True
    print(mas_de_dos_tercios([1, 2])) # False
    print(mas_de_dos_tercios([1, 2, 1, 4, 1, 6, 1, 1])) # False

if __name__ == "__main__":
    main()