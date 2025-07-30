"""
    Mi algoritmo comienza dandole un formato "más cómodo" a los
parámetros, formando una lista de tuplas de la forma
(duración, deadline). Posteriormente, ordena esta lista
ascendentemente, en función al deadline de las tareas.
    Ya en la parte "Greedy", el algoritmo itera la lista
minimizando, en cada paso, la latencia de la tarea en iteración
(optimos locales), logrando, finalmente, una solución global.
    Se trata de una solución optima ya que, al "elegir" primero
las tareas con un deadline más próximo se lograr acumular la
menor latencia posible en cada tarea para así, a medida que se
avanza en la iteración, lograr latencias menores que las que se
conseguirían utilizando otros enfoques (ver ejemplos al final).
    En cuanto a la complejidad, esta está dada por el
ordenamiento inicial, el cuál se lleva a cabo en O(n log n).
Luego, la parte Greedy se lleva a cabo en O(n), por lo que no
influye en la complejidad final.

Ejemplos de soluciones a este problema utilizando diferentes
enfoques:

Tareas (duración, deadline):
(5, 8)
(1, 3)
(3, 7)
(6, 6)

Primero tareas con deadline más próximo (OPTIMO):
(1, 3): 1, 1-3 = 0
(6, 6): 7, 7-6 = 1
(3, 7): 10, 10-7 = 3
(5, 8): 15, 15-8 = 7

Primero tareas con menor duración (SUBOPTIMO):
(1, 3): 1, 1-3 = 0
(3, 7): 4, 4-7 = 0
(5, 8): 9, 9-8 = 1
(6, 6): 15, 15-6 = 9

Primero tareas con menor (deadline - duración) (SUBOPTIMO):
(6, 6): 6, 6-6 = 0
(1, 3): 7, 7-3 = 4
(5, 8): 12, 12-8 = 4
(3, 7): 15, 15-7: 8

Primero tareas con mayor (deadline - duración) (SUBOPTIMO):
(3, 7): 3, 3-7 = 0
(5, 8): 8, 8-8 = 0
(1, 3): 9, 9-3 = 6
(6, 6): 15, 15-6: 9
"""

def minimizar_latencia(L_deadline, T_tareas):
    tuplas = []
    for i in range(len(L_deadline)):
        tuplas.append((T_tareas[i], L_deadline[i]))
    tuplas.sort(key=lambda x: x[1])

    actual = 0
    for i, tupla in enumerate(tuplas):
        actual += tupla[0]
        tuplas[i] = (tupla[0], max(actual - tupla[1], 0))

    return tuplas

def main():
    print(minimizar_latencia([8, 3, 7, 6], [5, 1, 3, 6]))

if __name__ == "__main__":
    main()