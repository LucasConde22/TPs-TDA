"""
JUSTIFICACIÓN:
El ejecicio consta de tres partes:
    I. Busco un candidato: Esto lo hago sumando o restando
    1 cada vez que itero un elemento del arreglo, si el
    contador llega a 0, cambio de "candidato" por el nuevo
    elemento. El único candidato posible va a ser el que
    me termine quedando, ya que es imposible que otro apa-
    rezca más veces. Complejidad O(N)
    II. Contar apariciones: Recursivamente, utilizando DyC,
    cuento las apariciones del "candidato". Complejidad O(N)
    III. Comparo la cantidad de apariciones del candidato con
    las necesarias para lograr más de la mitad y devuelvo el
    resultado obtenido (True o False). Complejidad O(1)

Por lo tanto, la complejidad final es O(N). Ya que es la com-
plejidad máxima alcanzada con la búsqueda de candidato
(iterativa) y el conteo de apariciones (recursivo), el cuál
presenta la siguiente ecuación de recurrencia:
    T(N) = 2 * T(N/2) + O(1)
y, con el teorema maestro, puedo determinar que la complejidad
es O(N).
"""

def mas_de_la_mitad(arr):
    return _contar_apariciones(arr, _buscar_candidato(arr), 0, len(arr) - 1) > len(arr) // 2

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
    print(mas_de_la_mitad([1, 2, 1, 2, 3])) # False
    print(mas_de_la_mitad([1, 1, 2, 3])) # False
    print(mas_de_la_mitad([1, 2, 3, 1, 1, 1])) # True
    print(mas_de_la_mitad([1])) # True
    print(mas_de_la_mitad([4, 4])) # True
    print(mas_de_la_mitad([1, 2])) # False
    print(mas_de_la_mitad([1, 2, 1, 4, 1, 6, 1, 1])) # True

if __name__ == "__main__":
    main()
