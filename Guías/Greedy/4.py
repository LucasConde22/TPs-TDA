"""
FUNCIONAMIENTO, JUSTIFICACIÓN Y COMPLEJIDAD:
        El algoritmo ordena todas las charlas en base a su horario
    de finalización y selecciona, sucesivamente, la charla más
    temprana a finalizar siempre y cuando esta sea compatible con
    la última agregada. Para esto, la nueva charla debe tener un
    horario de inicio >= al de finalización de la anterior.
        Se trata de un algoritmo Greedy ya que, a medida que se
    itera, se van agregando charlas (soluciones parciales), todas
    compatibles entre si, que luego forman parte de la solución
    global optima.
        La complejidad del algoritmo es O(n log n), debido al
    ordenamento inicial de las charlas. Luego se realizan otras
    operaciones que, en conjunto, presentan una complejidad de
    O(n). Pero, como O(n log n) > O(n), la complejidad final es
    la que mencioné al comienzo de este párrafo.

OPTIMALIDAD:
        Para probar que el algoritmo es optimo voy a suponer que,
    para un determinado arreglo de charlas, tengos dos resultados:
    El dado por mi algoritmo, que tengo que probar si es optimo, y
    uno optimo "imaginado", que no conozco pero, por la naturaleza
    del ejercicio, puedo reconocer ciertas propiedades de este.
        Como voy a probar la optimalidad utilizando la técnica de
    inducción, voy a enforcarme primero en el caso inicial, la
    primera charla.
        En esta charla, por cómo está programado mi algoritmo, se que
    su tiempo de finalización va a ser <= que el tiempo de finalización
    de la primera charla de la solución optima imaginada. De esta forma,
    como cada charla debe tener tiempo de finalización <= que el tiempo
    de inicio de la charla siguiente, puedo determinar que la selecionada
    por mi algoritmo es optima. Puesto que si su tiempo de finalización
    es <= que el de la presente en el algoritmo imaginado, necesariamente
    tiene que ser <= al de inicio de la charla siguiente.
        Luego, si en la posición R mi algoritmo se mantiene optimo, es
    posible determinar que en la posición R+1 este también va a ser optimo.
    Esto es, como ya mencioné antes, debido a que F(R) en mi algoritmo es
    <= a F(R) en la solución optima. Y, por lo tanto, la siguiente charla
    seleccionada complirá que F(R) <= I(R+1), siendo F(R+1) en mi solución
    necesariamente <= a F(R+1) en la solución optima.
        De esta forma, puedo determinar que mi agoritmo es optimo y que,
    la cantidad de charlas en cada solución será la misma. Puestoo que si
    la solución optima inicial tuviera más elementos que la dada por mi
    algritmo, en algún momento se debería haber dado que F(J), en mi
    solución, > a I(J+1) en la solución imaginada, lo cuál, como prové
    anteriormente, sé que es imposible.
"""

def charlas(horarios):
    if not horarios:
        return []
    
    horarios.sort(key=lambda x: x[1])
    charlas = [horarios[0]]

    for charla in horarios[1:]:
        if charla[0] < charlas[-1][1]:
            continue
        charlas.append(charla)

    return charlas

def main():
    print(charlas([(1, 3), (2, 4), (5, 7), (7, 8), (7, 9)]))

if __name__ == "__main__":
    main()