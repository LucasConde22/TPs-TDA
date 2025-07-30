from grafo import Grafo

def contar_ordenamientos(grafo):
    return _buscar_orden(buscar_grados_entrada(grafo), [], grafo)
    
def _buscar_orden(grados, solucion_parcial, grafo):
    if len(grafo.obtener_vertices()) == 0:
        return 1

    soluciones = 0
    for v, grado in grados.items():
        if grado != 0:
            continue
        grados[v] = -1
        solucion_parcial.append(v)
        adyacentes = _quitar_vertice(v, grados, grafo)
        soluciones += _buscar_orden(grados, solucion_parcial, grafo)
        _agregar_vertice(v, adyacentes, grados, grafo)
        grados[v] = 0
        solucion_parcial.pop()

    return soluciones

def _quitar_vertice(v, grados, grafo):
    adyacentes = []
    for a in grafo.adyacentes(v):
        adyacentes.append(a)
        grados[a] = grados[a] - 1
    grafo.borrar_vertice(v)
    return adyacentes

def _agregar_vertice(v, adyacentes, grados, grafo):
    grafo.agregar_vertice(v)
    for a in adyacentes:
        grados[a] = grados[a] + 1
        grafo.agregar_arista(v, a)
    
def buscar_grados_entrada(grafo):
    grados = {}
    for v in grafo:
        if not v in grados:
            grados[v] = 0
        for a in grafo.adyacentes(v):
            grados[a] = 1 + grados.get(a, 0)
    return grados

def main():
    grafo = Grafo(True, ['A', 'B', 'C'])
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'C')
    print(contar_ordenamientos(grafo))


    grafo = Grafo(True, ['A', 'B', 'C', 'D', 'E'])
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'C')
    grafo.agregar_arista('C', 'D')
    grafo.agregar_arista('E', 'D')
    print(contar_ordenamientos(grafo))

if __name__ == "__main__":
    main()