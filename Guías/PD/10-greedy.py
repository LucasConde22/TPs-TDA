from grafo import Grafo
import heapq

# Solución Greedy:
# Complejidad: O(N*log(N))
def plan_operativo(arreglo_L, arreglo_C, costo_M):
    n = len(arreglo_L)

    if n == 0:
        return []

    grafo = Grafo(False, ["INICIO", "FIN"])
    for i in range(n): # Agrego vertices y aristas dentro del mismo arreglo.
        v = f'{i}:L'
        w = f'{i}:C'
        grafo.agregar_vertice(v)
        grafo.agregar_vertice(w)
        if i != 0:
            a = f'{i - 1}:L'
            grafo.agregar_arista(v, a, arreglo_L[i])
            a = f'{i - 1}:C'
            grafo.agregar_arista(w, a, arreglo_C[i])
        else:
            grafo.agregar_arista("INICIO", f'{0}:L', arreglo_L[0])
            grafo.agregar_arista("INICIO", f'{0}:C', arreglo_C[0])

    grafo.agregar_arista("FIN", f'{n - 1}:L', 0)
    grafo.agregar_arista("FIN", f'{n - 1}:C', 0)

    for i in range(n - 1): # Aristas en diagonal con elementos del otro arreglo.
        grafo.agregar_arista(f'{i}:L', f'{i + 1}:C', arreglo_C[i + 1] + costo_M)
        grafo.agregar_arista(f'{i}:C', f'{i + 1}:L', arreglo_L[i + 1] + costo_M)

    anterior = dijkstra(grafo, "INICIO", "FIN")
    
    camino = []
    v = "FIN"
    while v is not None:
        if v[-1] == 'L':
            camino.append("londres")
        elif v[-1] == 'C':
            camino.append("california")
        v = anterior[v]

    return camino[::-1]


def dijkstra(grafo, inicio, fin):
    distancia = {v: float('inf') for v in grafo.vertices}
    distancia[inicio] = 0
    heap = [(0, inicio)]
    anterior = {inicio: None}

    while heap:
        _, v = heapq.heappop(heap)

        if v == fin:
            break

        for a in grafo.adyacentes(v):
            nueva = distancia[v] + grafo.peso_arista(v, a)

            if nueva < distancia[a]:
                distancia[a] = nueva
                anterior[a] = v
                heapq.heappush(heap, (nueva, a))

    return anterior
        
def main():
    print(plan_operativo([], [], 20))
    print(plan_operativo([5], [10], 20))
    print(plan_operativo([80, 50, 120, 60], [70, 120, 100, 50], 20))
    print(plan_operativo([80, 50, 100, 35, 120, 120], [70, 50, 130, 80, 25, 100], 10))

    londres = [100, 50]
    california = [75, 100]
    print(plan_operativo(londres, california, 75)) # ['londres', 'londres']

    londres = [50, 100]
    california = [100, 50]
    print(plan_operativo(londres, california, 25)) # ['londres', 'california']

    londres = [85, 15, 55, 5, 25, 35, 55, 35]
    california = [75, 25, 45, 5, 25, 35, 25, 55]
    print(plan_operativo(londres, california, 25)) # ['california']*8

    londres = [5, 46, 18, 88, 33, 13, 22, 35, 58]
    california = [20, 10, 65, 24, 55, 2, 28, 14, 94]
    print(plan_operativo(londres, california, 25)) # ['londres','londres','londres','california','california','california','california','california','londres'])"

if __name__ == "__main__":
    main()

"""
L = [80, 50, 100, 35, 120, 120]
C = [70, 50, 130, 80, 25, 100]
M = 10

n = 0 -> []
n = 1 -> [- costosa]

70:C
70:C -> 50:C
70:C -> 50:C -> (100:L + 10:M) -> 35:L -> (25:C + 10:M) -> 100:C


L = [80, 50, 120, 60]
C = [70, 120, 100, 50]
M = 20

70:C -> (50:L + 20:M) => Solución errónea.



"""