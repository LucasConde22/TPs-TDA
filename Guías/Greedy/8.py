"""
    Mi algoritmo, primero, ordena el arreglo de mayor a menor
según el ratio valor/peso. Luego, es Greedy ya que se itera
este mismo arreglo  buscando optimos locales considerando,
siempre, que el peso del nuevo elemento, sumado a lo que ya
se encuentra en la mochila, no supere el valor W. De manera
más sencilla, se puede decir que primero se guardarán los
elementos con mejor nro. de valor/peso, que consisten en
optimos locales, los cuales, formarán la solución global que
maximiza el valor guardado, sin superar el límite de peso, W.
    Además, el algoritmo es optimo puesto que, en cada proceso
de la iteración, se guarda el elemento que mayor valor me da,
por el menor peso posible (Al final se puede observar una
comparación entre este enfoque y uno que selecciona los
elementos priorizando primero los de menor peso).
    Como en ejrcicios anteriores, la "parte Greedy" presenta
una complejidad de O(n). Pero, como anteriormente realizo un
ordenamiento, la complejidad final del algoritmo resulta ser
O(n log n).

------------------------------------------------------------
EJEMPLO COMPARANDO SOLUCIÓN DE "MAYOR VALOR/PESO" (OPTIMA) Y DE
"MENOR PESO" (SUBOPTIMA):

W = 200
elementos = [(100, 20), (200, 35), (80, 100), (120, 100), (100, 21), (10, 5), (200, 200), (150, 150), (1, 99)]
valor/peso =  5          5,71       0,8        1,2         4,76       2        1           1           0,01

Seleccionando elementos por menor peso (y menor valor, en caso de pesar lo mismo:
(10, 5)
(100, 20)
(100, 21)
(200, 35)
(1, 99)
Valor | peso final: 411 | 180

Seleccionando elementos con mayor ratio valor/peso:
(200, 35)
(100, 20)
(100, 21)
(10, 5)
(120, 100)
Valor | peso final: 530 | 181
"""

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    guardados = []
    elementos.sort(key=lambda x: -(x[0] / x[1]))

    for elemento in elementos:
        if W - elemento[1] >= 0:
            guardados.append(elemento)
            W -= elemento[1]

    return guardados

def main():
    print(mochila([(100, 20), (200, 35), (80, 100), (120, 100), (100, 21), (10, 5), (200, 200), (150, 150), (1, 99)], 200))

if __name__ == "__main__":
    main()