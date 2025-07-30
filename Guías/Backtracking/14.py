from grafo import Grafo

def dominating_set_min(grafo):
    aproximacion = _hallar_aprox_greedy(grafo)

    if len(aproximacion) <= 1:
        return aproximacion
    
    return _hallar_ds_min_bt(0, grafo.obtener_vertices(), set(), len(aproximacion), grafo)

def _hallar_ds_min_bt(i, vertices, sol_parcial, tope, grafo):
    if len(sol_parcial) > tope:
        return None
    
    if _hay_solucion(sol_parcial, grafo):
        return list(sol_parcial)
    
    if i == len(vertices):
        return None

    sol_con, sol_sin = None, None
    if _es_compatible(vertices[i], sol_parcial, grafo):
        sol_parcial.add(vertices[i])
        sol_con = _hallar_ds_min_bt(i + 1, vertices, sol_parcial, tope, grafo)
        sol_parcial.remove(vertices[i])

    if sol_con:
        tope = len(sol_con)
    sol_sin = _hallar_ds_min_bt(i + 1, vertices, sol_parcial, tope, grafo)

    if sol_con and sol_sin:
        return sol_con if len(sol_con) < len(sol_sin) else sol_sin
    return sol_con or sol_sin

def _hay_solucion(solucion, grafo):
    visitados = solucion.copy()
    for v in solucion:
        for a in grafo.adyacentes(v):
            visitados.add(a)
    return len(visitados) == len(grafo.obtener_vertices())

def _es_compatible(v, solucion, grafo):
    for a in grafo.adyacentes(v):
        if a in solucion:
            return False
    return True

def _hallar_aprox_greedy(grafo):
    solucion = set()
    for v in grafo:
        if _es_compatible(v, solucion, grafo):
            solucion.add(v)
    return list(solucion)

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
    print(dominating_set_min(grafo))

    g = Grafo(False, ['A', 'B', 'C', 'D'])   
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('A', 'D')
    print(dominating_set_min(g))


    grafo = Grafo(False, ["A", "B", "C", "D", "E"])
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "B")
    grafo.agregar_arista("B", "E")
    print(dominating_set_min(grafo))

if __name__ == "__main__":
    main()