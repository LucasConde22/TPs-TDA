from grafo import Grafo

def hallar_dominating_set_suma_min(grafo, valores):
    vertices = grafo.obtener_vertices()
    sol, _ = _dominating_set_bt(0, vertices, valores, grafo, set(), 0, vertices,
                                sum(valores[v] for v in vertices))
    return sol

def _dominating_set_bt(i, vertices, valores, grafo, sol_parcial, val_parcial, sol_optima,
                        val_optimo):

    if val_parcial >= val_optimo:
        return sol_optima, val_optimo
    
    if _es_ds(sol_parcial, grafo):
            return list(sol_parcial), val_parcial
    
    if i == len(vertices):
        return sol_optima, val_optimo
    
    sol_parcial.add(vertices[i])
    sol_optima, val_optimo = _dominating_set_bt(i + 1, vertices, valores, grafo, sol_parcial,
                                                val_parcial + valores[vertices[i]], sol_optima,
                                                val_optimo)
    sol_parcial.remove(vertices[i])

    sol_optima, val_optimo = _dominating_set_bt(i + 1, vertices, valores, grafo, sol_parcial,
                                                val_parcial, sol_optima, val_optimo)
    
    return sol_optima, val_optimo

def _es_ds(sol, grafo):
    dominados = set(sol)
    for v in sol:
        dominados.update(grafo.adyacentes(v))
    return len(dominados) == len(grafo)

def main():
    grafo = Grafo(False, ['a', 'b', 'c'])
    grafo.agregar_arista('a', 'b')
    grafo.agregar_arista('b', 'c')
    print(hallar_dominating_set_suma_min(grafo, {'a': 3, 'b': 5, 'c': 1}))

if __name__ == "__main__":
    main()
