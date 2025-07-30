"""
JUSTIFICACIÓN:
    Es, virtualmente, una búsqueda binaria con
    algunas modificaciones. Por lo tanto, la
    ecuación de recurrencia es:
    T(N) = 1 * T(N / 2) + O(1)

    y, con el T.M, puedo determinar que la
    complejidad es O(log N)
"""

def encontrar_joya(joyas):
    return _encontrar_joya(joyas, 0, len(joyas) - 1)

def _encontrar_joya(joyas, ini, fin):
    if ini == fin:
        return ini

    medio = (ini + fin) // 2
    ajuste = 0 # Creo que se tiene que poder prescidir de esta variable, pero no tengo ganas de pensar

    if (fin - ini) % 2 == 0:
        pesaje = balanza(joyas[ini : medio + 1], joyas[medio : fin + 1])
        ajuste = -1
    else:
        pesaje = balanza(joyas[ini : medio + 1], joyas[medio + 1 : fin + 1])

    if pesaje == 0:
        return medio
    if pesaje == 1:
        return _encontrar_joya(joyas, ini, medio + ajuste)
    return _encontrar_joya(joyas, medio + 1, fin)

def balanza(arr1, arr2):
    if len(arr1) != len(arr2):
        raise Exception("error!")
    
    suma1, suma2 = 0, 0
    for i in range(len(arr1)):
        suma1 += arr1[i]
        suma2 += arr2[i]

    if suma1 == suma2:
        return 0
    if suma1 > suma2:
        return 1
    return -1

def main():
    print(encontrar_joya([1, 1, 1, 2, 1]))
    print(encontrar_joya([1, 1, 1, 2, 1, 1, 1]))
    print(encontrar_joya([1, 2]))
    print(encontrar_joya([1, 1, 1, 1, 1, 2]))
    print(encontrar_joya([1, 0, 0]))

if __name__ == "__main__":
    main()
