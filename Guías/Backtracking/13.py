from grafo import Grafo

"""
Algoritmo que encuentra Vertex Cover mínimo recortando con la
aproximación encontrada por un algoritmo Greedy como recorte.
"""
def vertex_cover_min(grafo):
    aproximacion = vertex_cover_aprox(grafo)

    if len(aproximacion) <= 1:
        return aproximacion

    return _hallar_cover(0, grafo.obtener_vertices(), [], contar_aristas(grafo),len(aproximacion), grafo)

def _hallar_cover(i, vertices, sol_parcial, restantes, min, grafo):
    if len(sol_parcial) > min: # Si ya no llega a ser solución, recorto
        return None
    
    if restantes == 0:
        return sol_parcial[:]
    
    if i == len(vertices): # Si ya recorrí todos los vértices y no encontré solución, recorto
        return None
    
    sol, sol2 = None, None
    if len(grafo.adyacentes(vertices[i])) != 0:
        sol_parcial.append(vertices[i])
        adyacentes = _borrar_aristas(vertices[i], grafo)
        sol = _hallar_cover(i + 1, vertices, sol_parcial, restantes - len(adyacentes), min, grafo)
        sol_parcial.pop()
        _agregar_aristas(vertices[i], adyacentes, grafo)

    if sol:
        min = len(sol)
    sol2 = _hallar_cover(i + 1, vertices, sol_parcial, restantes, min, grafo)

    if sol and sol2:
        return sol if len(sol) < len(sol2) else sol2
    return sol or sol2

def _borrar_aristas(v, grafo):
    adyacentes = []
    for a in grafo.adyacentes(v):
        grafo.borrar_arista(v, a)
        adyacentes.append(a)
    return adyacentes

def _agregar_aristas(v, adyacentes, grafo):
    for a in adyacentes:
            grafo.agregar_arista(v, a)

def contar_aristas(grafo):
    aristas = 0
    for v in grafo:
        aristas += len(grafo.adyacentes(v))
    return aristas // 2

# Algoritmo greedy usado para recorte:
def vertex_cover_aprox(grafo):
    grafo = copiar_grafo(grafo)
    resultado = []

    while True:
        elegido = None
        max_adyacentes = 0

        for v in grafo:
            cant_adyacentes = len(grafo.adyacentes(v))
            if cant_adyacentes > max_adyacentes:
                elegido = v
                max_adyacentes = cant_adyacentes

        if not elegido:
            break
        grafo.borrar_vertice(elegido)
        resultado.append(elegido)

    return resultado

def copiar_grafo(grafo):
    nuevo = Grafo(False, grafo.obtener_vertices())
    for v in grafo:
        for a in grafo.adyacentes(v):
            if not nuevo.estan_unidos(v, a):
                nuevo.agregar_arista(v, a)
    return nuevo

# ---------------------------------------------------------------------
def main():
    grafo = Grafo(False, ["A", "B", "C", "D", "E", "F", "G", "H"])
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("B", "E")
    grafo.agregar_arista("B", "F")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("C", "E")
    grafo.agregar_arista("D", "E")
    grafo.agregar_arista("D", "H")
    grafo.agregar_arista("F", "G")

    print(vertex_cover_min(grafo))

    g = Grafo(False, ['A', 'B', 'C', 'D'])   
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('A', 'D')
    g.agregar_arista('D', 'C')
    print(vertex_cover_min(g))


    g = Grafo(False, ['1', '2', '3', '4', '5', '6', '7'])   
    g.agregar_arista('1', '2')
    g.agregar_arista('1', '4')
    g.agregar_arista('2', '3')
    g.agregar_arista('2', '5')
    g.agregar_arista('3', '7')
    g.agregar_arista('3', '6')
    g.agregar_arista('5', '6')
    print(vertex_cover_min(g))

if __name__ == "__main__":
    main()