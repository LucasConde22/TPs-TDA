from grafo import Grafo

def independent_set(grafo):
    solucion = [[]]
    _buscar_max_id(grafo, grafo.obtener_vertices(), 0, solucion, [])
    return solucion[0]

def _chequear_compatibilidad(grafo, v, solucion):
    for a in solucion:
        if grafo.estan_unidos(v, a):
            return False
    return True

def _buscar_max_id(grafo, vertices, i, solucion, solucion_parcial):
    if i == len(vertices):
            if len(solucion_parcial) > len(solucion[0]):
                solucion[0] = list(solucion_parcial)
            return

    if _chequear_compatibilidad(grafo, vertices[i], solucion_parcial):
        solucion_parcial.append(vertices[i])
        _buscar_max_id(grafo, vertices, i + 1, solucion, solucion_parcial)
        solucion_parcial.pop()

    _buscar_max_id(grafo, vertices, i + 1, solucion, solucion_parcial)