"""
EXPLICACIÓN:
        Se divide el arreglo, recursivamente, hasta llegar a dos bloques
    de dos elementos, uno en izquierda y otro en derecha, sobre el cual
    se realiza el intercambio. Este consiste en cambiar el segundo
    elemento del bloque de izq. por el primero del de der. y viceversa.
        Para los llamados recursivos, primero se encuentra la mitad de
    la porción de arreglo en proceso y se llama dos veces a la función
    con: I. Primera mitad izq. y primera mitad der.
         II. Segunda mitdad izq. y segunda mitad der.
        Posteriormente, para concluir con el correcto alternamiento de
    los números, se intercambian las posiciones de la primera mitad der.
    por las de la segunda mitad izq. (es decir, la última parte de
    cambiado en el primer llamado y la primera parte de lo cambiado en
    el segundo llamado).
        Adicionalmente, traté el caso borde de que se llame a la función
    con solo dos elementos (C1, D1). En esta situación, no se realiza
    ninguna modificación en el arreglo.

SEGUIMIENTO:
    C1 C2 C3 C4 C5 C6 C7 C8 D1 D2 D3 D4 D5 D6 D7 D8
    C1 C2 C3 C4 C5 C6 C7 C8 | D1 D2 D3 D4 D5 D6 D7 D8
    C1 C2 C3 C4 | C5 C6 C7 C8 | D1 D2 D3 D4 | D5 D6 D7 D8
    C1 C2 | C3 C4 | C5 C6 | C7 C8 | D1 D2 | D3 D4 | D5 D6 | D7 D8
    C1 D1 | C3 D3 | C5 D5 | C7 D7 | C2 D2 | C4 D4 | C6 D6 | C8 D8
    C1 D1 C3 D3 | C5 D5 C7 D7 | C2 D2 C4 D4 | C6 D6 C8 D8
    C1 D1 C2 D2 | C5 D5 C6 D6 | C3 D3 C4 D4 | C7 D7 C8 D8
    C1 D1 C2 D2 C5 D5 C6 D6 | C3 D3 C4 D4 C7 D7 C8 D8
    C1 D1 C2 D2 C3 D3 C4 D4 | C5 D5 C6 D6 C7 D7 C8 D8
    C1 D1 C2 D2 C3 D3 C4 D4 C5 D5 C6 D6 C7 D7 C8 D8

COMPLEJIDAD:
        Llamo recursivamente dos veces, con la mitad de los elementos,
    en cada llamado y recorro e intercambio elementos en la mitad de la
    porción en ejecución. Por lo tanto, la ecuación de recurrencia es:

    T(N) = 2 * T(N/2) + O(N)

    Con el teorema maestro, como log2(2) = 1 -> complejidad final: O(N log N)
"""


def alternar(arr):
    if len(arr) == 2:
        return
    _alternar(arr, 0, (len(arr)-1)//2, len(arr)//2, len(arr)-1)

def _alternar(arr, ii, fi, id, fd):
    if fi - ii == 1:
        arr[fi], arr[id] = arr[id], arr[fi]
        return

    mi = (fi + ii) // 2
    md = (fd + id) // 2

    _alternar(arr, ii, mi, id, md)
    _alternar(arr, mi + 1, fi, md + 1, fd)

    for i in range(md - id + 1):
        arr[id + i], arr[mi + i + 1] = arr[mi + i + 1], arr[id + i]


def main():
    arr = ["C1", "C2", "D1", "D2"]
    alternar(arr)
    print(arr)

    arr = ["C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]
    alternar(arr)
    print(arr)

    arr = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
    alternar(arr)
    print(arr)

if __name__ == "__main__":
    main()