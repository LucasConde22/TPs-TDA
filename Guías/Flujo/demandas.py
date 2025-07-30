from grafo import Grafo
from algoritmos import flujo

def circulacion_con_demanda(red, demandas):
    red_alt = Grafo(True, red.obtener_vertices() + ['sf', 'ss'])

    for v in red:
        if demandas[v] < 0:
            red_alt.agregar_arista('sf', v, -demandas[v])
        elif demandas[v] > 0:
            red_alt.agregar_arista(v, 'ss', demandas[v])
        for a in red.adyacentes(v):
            red_alt.agregar_arista(v, a, red.peso_arista(v, a))
    
    fl_alt = flujo(red_alt, 'sf', 'ss')
    fl = {}
    for (v, a), f in fl_alt.items():
        if v == 'sf' or a == 'ss':
            continue
        fl[(v, a)] = f
    
    return fl

def main():
    grafo = Grafo(True, ['0', '1', '2', '3'])
    grafo.agregar_arista('0', '1', 3)
    grafo.agregar_arista('0', '2', 3)
    grafo.agregar_arista('1', '2', 2)
    grafo.agregar_arista('1', '3', 2)
    grafo.agregar_arista('2', '3', 2)
    demandas = {'0': -3, '1': -3, '2': 2, '3': 4}
    print(circulacion_con_demanda(grafo, demandas))

if __name__ == "__main__":
    main()