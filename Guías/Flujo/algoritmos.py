from grafo import Grafo
from collections import deque

def flujo(grafo, fuente, sumidero):
    red_residual = Grafo(True, grafo.obtener_vertices())
    flujo = {}
    for v in grafo:
        for a in grafo.adyacentes(v):
            flujo[(v, a)] = 0
            red_residual.agregar_arista(v, a, grafo.peso_arista(v, a))
    
    while True:
        camino = buscar_camino(red_residual, fuente, sumidero)
        if not camino:
            break

        capacidad_camino = buscar_minimo(camino, red_residual)
        for i in range(len(camino) - 1):
            v, w = camino[i], camino[i + 1]
            if grafo.estan_unidos(v, w):
                flujo[(v, w)] += capacidad_camino
            else:
                flujo[(w, v)] -= capacidad_camino
            actualizar_red_residual(red_residual, camino[i], camino[i + 1], capacidad_camino)

    return flujo

def actualizar_red_residual(red_residual, v, w, valor):
    peso_anterior = red_residual.peso_arista(v, w)
    red_residual.borrar_arista(v, w)
    if peso_anterior > valor:
        red_residual.agregar_arista(v, w, peso_anterior - valor)
    
    if not red_residual.estan_unidos(w, v):
        peso_anterior = 0
    else:
        peso_anterior = red_residual.peso_arista(w, v)
        red_residual.borrar_arista(w, v)
    red_residual.agregar_arista(w, v, peso_anterior + valor)

def buscar_minimo(camino, red_residual):
    min = float('inf')
    for i in range(len(camino) - 1):
        min = red_residual.peso_arista(camino[i], camino[i+1]) if red_residual.peso_arista(camino[i], camino[i+1]) < min else min
    return min

def buscar_camino(grafo, origen, destino):
    cola = deque([origen])
    visitados = {origen}
    padre = {origen: None}

    while cola:
        v = cola.popleft()
        if v == destino:
            break
        for a in grafo.adyacentes(v):
            if a not in visitados:
                cola.append(a)
                visitados.add(v)
                padre[a] = v

    if destino not in padre:
        return None
    
    camino, v = [], destino
    while v != None:
        camino.append(v)
        v = padre[v]

    return camino[::-1]

def main():
    grafo = Grafo(True, ['0', '1', '2', '3', '4', '5'])
    grafo.agregar_arista('0', '1', 11)
    grafo.agregar_arista('0', '2', 12)
    grafo.agregar_arista('1', '3', 12)
    grafo.agregar_arista('2', '1', 2)
    grafo.agregar_arista('2', '4', 11)
    grafo.agregar_arista('3', '5', 19)
    grafo.agregar_arista('4', '3', 10)
    grafo.agregar_arista('4', '5', 4)
    print(flujo(grafo, '0', '5'))


    grafo = Grafo(True, ['Fu', 'A', 'C', 'E', 'F', 'J', 'K', 'Su'])
    grafo.agregar_arista('Fu', 'J', 1)
    grafo.agregar_arista('Fu', 'A', 8)
    grafo.agregar_arista('A', 'C', 10)
    grafo.agregar_arista('A', 'F', 1)
    grafo.agregar_arista('C', 'E', 9)
    grafo.agregar_arista('E', 'Su', 13)
    grafo.agregar_arista('F', 'Su', 1)
    grafo.agregar_arista('J', 'K', 1)
    grafo.agregar_arista('K', 'F', 1)
    print(flujo(grafo, 'Fu', 'Su'))

    grafo = Grafo(True, ["L", "S", "U", "Y", "X", "Z", "W", "V", "T"])
    grafo.agregar_arista('L', 'X', 3)
    grafo.agregar_arista('L', 'S', 9)
    grafo.agregar_arista('X', 'Z', 3)
    grafo.agregar_arista('S', 'V', 6)
    grafo.agregar_arista('S', 'U', 3)
    grafo.agregar_arista('Z', 'W', 1)
    grafo.agregar_arista('Z', 'Y', 4)
    grafo.agregar_arista('Y', 'U', 4)
    grafo.agregar_arista('U', 'Z', 2)
    grafo.agregar_arista('U', 'W', 6)
    grafo.agregar_arista('W', 'T', 6)
    grafo.agregar_arista('V', 'W', 1)
    grafo.agregar_arista('V', 'T', 3)
    print(flujo(grafo, "L", "T"))

    grafo = Grafo(True, ["A", "B", "C"])
    grafo.agregar_arista('C', 'A', 3)
    grafo.agregar_arista('A', 'B', 4)
    print(flujo(grafo, "C", "B"))

if __name__ == "__main__":
    main()

