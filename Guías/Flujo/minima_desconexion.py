from grafo import Grafo
from collections import deque
from algoritmos import flujo
from construir import construir_red_residual


def obtener_minima_desconexion(red, fuente, sumidero):
    red_alt = Grafo(True, [fuente, sumidero])
    mapeo = {}

    for v in red:
        if v == fuente or v == sumidero:
            mapeo[v] = (v, v)
            continue
        v_in, v_out = f'{v}_in', f'{v}_out'
        red_alt.agregar_vertice(v_in)
        red_alt.agregar_vertice(v_out)
        mapeo[v] = (v_in, v_out)
        red_alt.agregar_arista(v_in, v_out, 1)

    for v in red:
        for a in red.adyacentes(v):
            red_alt.agregar_arista(mapeo[v][1], mapeo[a][0], float('inf'))

    red_residual = construir_red_residual(red_alt, flujo(red_alt, fuente, sumidero))
    distancias = _bfs(red_residual, fuente)
    a_eliminar = []
    for v, (v_in, v_out) in mapeo.items():
        if distancias[v_in] < float('inf') and distancias[v_out] >= float('inf'):
            a_eliminar.append(v)

    return a_eliminar

def _bfs(grafo, origen):
    distancia = {origen: 0}
    cola = deque([origen])

    while cola:
        v = cola.popleft()
        for a in grafo.adyacentes(v):
            if a not in distancia:
                distancia[a] = distancia[v] + 1
                cola.append(a)
        
    for v in grafo:
        if v not in distancia:
            distancia[v] = float('inf')
    
    return distancia

def main():
    grafo = Grafo(True, ['0', '2', '3', '5', '6', '7'])
    grafo.agregar_arista('0', '2', 1)
    grafo.agregar_arista('0', '3', 1)
    grafo.agregar_arista('2', '6', 1)
    grafo.agregar_arista('3', '6', 1)
    grafo.agregar_arista('5', '7', 1)
    grafo.agregar_arista('6', '5', 1)
    print(obtener_minima_desconexion(grafo, '0', '7'))

    grafo = Grafo(True, ['0', '1', '2', '3'])
    grafo.agregar_arista('0', '1', 1)
    grafo.agregar_arista('0', '2', 1)
    grafo.agregar_arista('1', '3', 1)
    grafo.agregar_arista('2', '3', 1)
    print(obtener_minima_desconexion(grafo, '0', '3'))

    grafo = Grafo(True, ['0', '1', '2', '3'])
    grafo.agregar_arista('0', '1', 1)
    grafo.agregar_arista('0', '2', 1)
    grafo.agregar_arista('1', '3', 1)
    grafo.agregar_arista('2', '1', 1)
    print(obtener_minima_desconexion(grafo, '0', '3'))

if __name__ == "__main__":
    main()


             