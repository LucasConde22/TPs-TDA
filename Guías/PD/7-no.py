"""
0 elementos -> No guardo nada.
1 elemento -> Si entra, lo guardo,
2 elementos ->  Si entran los dos, los guardo.
                Si solo entra A, guardo A.
                Si solo entra B, guardo B.
                Si solo entra uno de los dos, guardo el que mayor valor tenga.

                
(9, 11), (2, 1), (8, 6), (1, 1), (5, 5) | W = 12

Ordeno:
(2, 1), (1, 1), (5, 5) (8, 6), (9, 11)

(2, 1)
(2, 1), (1, 1)
(2, 1), (1, 1), (5, 5)
(2, 1), (1, 1), (8, 6)
(2, 1), (1, 1), (8, 6) y no usa el (9, 11)

Me guado referencias al anterior compatible?
"""

# Solución bottom-up:
# Complejidad: O(N^2), pero se puede reducir a O(N*log(N)) aplicando una pseudo "búsqueda binaria".
def mochila(elementos, W):
    elementos.sort(key = lambda x: -(x[0]/x[1]))

    acumulado = [(0, 0)] # (valor acumulador, peso acumulado)

    for i in range(len(elementos)):
        if elementos[i][1] > W: # Si el peso del elemento por si solo ya es mayor a W, mantiene el acumulado anterior.
            acumulado.append(acumulado[-1])
            continue

        for j in range(i, -1, -1): # Busca el primero de los acumulados anteriores al que se le puede sumar.
            nuevo_acumulado = acumulado[j][1] + elementos[i][1]

            if nuevo_acumulado <= W:
                nuevo_valor = acumulado[j][0] + elementos[i][0]

                if nuevo_valor > acumulado[-1][0]: # Acumula el que sea más grande entre el acumulado anterior y el nuevo.
                    acumulado.append((nuevo_valor, nuevo_acumulado))
                else:
                    acumulado.append(acumulado[-1])
                break

    return reconstruir_elementos(acumulado, elementos)

def reconstruir_elementos(acumulado, elementos):
    acumulado_inverso = acumulado[-1]
    mochila = []
    for i in range(len(acumulado) - 1, 0, -1):
        if acumulado[i] == acumulado[i - 1] or acumulado_inverso != acumulado[i]: # Si es igual al anterior es porque no se agregó.
            continue
        mochila.append(elementos[i - 1])
        acumulado_inverso = (acumulado_inverso[0] - elementos[i - 1][0], acumulado_inverso[1] - elementos[i - 1][1]) # Sirve para ver cuál es efecticamente el siguiente en el "camino".
    # return mochila
    return sorted(mochila) # Uso el sorted para que pase las pruebas

def main():
    print(mochila([(9, 11), (2, 1), (8, 6), (1, 1), (5, 5), (4, 15)], 12))
    print(mochila([], 12))
    print(mochila([(100, 20), (200, 35), (80, 100), (120, 100), (100, 21), (10, 5), (200, 200), (150, 150), (1, 99)], 200))
    print(mochila([(1, 1), (2, 1), (3, 1)], 2))
    print(mochila([(1, 2), (2, 3), (5, 5), (9, 8)], 11))

if __name__ == "__main__":
    main()
