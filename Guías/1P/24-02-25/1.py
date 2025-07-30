from heapq import heappush, heappop

"""
Complejidad:
            O(n*log(n))
            n = cantidad de proyectos y k = min(cantidad de equipos, n)

            I. Se ordena el arreglo de proyectos por tiempo de inicio -> O(n*log(n))
            II. Se itera el arreglo de proyectos, encolando y desencolando del heap que contiene un
                máximo de k elementos -> O(n*log(k))
            III. Se desencolan los k elementos del heap y se los apendea a un arreglo -> O(k*log(k))

            Como k <= n, la complejidad final resulta la ya mencionada.

¿Por qué es Greedy?:
            El algoritmo es Greedy ya que se busca minimizar el tiempo libre luego de la
            finalización de cada proyecto asignando a cada equipo el próximo compatible cuyo tiempo de
            inicio sea menor. De esta forma se toma la mejor decisión posible en cada momento,
            sin reconsiderar decisiones pasadas y se obtiene una sucesión de "óptimos" locales (tener
            asignados en cada momento la mejor combinación posible) que finalmente resulta en una
            solución global.

            Tanto el ordenamiento inicial, el uso de un heap y, en consecuencia, el "reformateo" final de
            las asignaciones resultan ser optimizaciones que no interfieren en la heuristica del algoritmo.
            De no utilizarse, la complejidad del mismo resultaría ser O(n^2*k).

¿Es óptimo?
            No, el algoritmo no es óptimo. Puede comprobarse en el ejemplo provisto en la función main().
"""
def maximizar_proyectos(proyectos, equipos):
    proyectos = sorted(proyectos, key= lambda x: x[0])
    heap = []
    
    for proyecto in proyectos:
        if heap and heap[0][0] <= proyecto[0]:
            _, asignados = heappop(heap)
            asignados.append(proyecto)
            heappush(heap, (proyecto[1], asignados))
        elif len(heap) < equipos:
            heappush(heap, (proyecto[1], [proyecto]))
    
    asignaciones = []
    while heap:
        _, asignados = heappop(heap)
        asignaciones.append(asignados)
    return asignaciones

def main():
    # Contraejemplo:
    print(maximizar_proyectos([(0, 6), (3, 4), (4, 5), (2, 6)], 2))

    # Caso en que funciona:
    print(maximizar_proyectos([(0, 1), (0, 2), (2, 3), (3, 4), (1, 5)], 2))

if __name__ == "__main__":
    main()