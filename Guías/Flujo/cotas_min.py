from grafo import Grafo
from algoritmos import flujo

def flujo_con_cotas_min(red, fuente, sumidero, cotas):
    red_alt = Grafo(True, red.obtener_vertices() + ['sf', 'ss'])

    for v in red:
        for a in red.adyacentes(v):
            if (v, a) in cotas and cotas[(v, a)] > 0:
                red_alt.agregar_arista('sf', a, cotas[(v, a)])
                red_alt.agregar_arista(v, 'ss', cotas[(v, a)])
                red_alt.agregar_arista(v, a, red.peso_arista(v, a) - cotas[(v, a)])
            else:
                red_alt.agregar_arista(v, a, red.peso_arista(v, a))

    pesos_fuente = sum(red.peso_arista(fuente, a) for a in red.adyacentes(fuente))
    red_alt.agregar_arista('sf', fuente, pesos_fuente)
    pesos_sumidero = 0
    for v in red:
        if red.estan_unidos(v, sumidero):
            pesos_sumidero += red.peso_arista(v, sumidero)
    red_alt.agregar_arista(sumidero, 'ss', pesos_sumidero)

    fl = flujo(red_alt, 'sf', 'ss')
    for (v, a), cota in cotas.items():
        if cota <= 0:
            continue
        fl[(v, a)] += cota
        fl.pop(('sf', a))
        fl.pop((v, 'ss'))
    fl.pop(('sf', fuente))
    fl.pop((sumidero, 'ss'))
    return fl

def main():
    grafo = Grafo(True, ['S', 'A', 'B', 'T'])
    grafo.agregar_arista('S', 'A', 5)
    grafo.agregar_arista('S', 'B', 4)
    grafo.agregar_arista('A', 'T', 5)
    grafo.agregar_arista('A', 'B', 3)
    grafo.agregar_arista('B', 'T', 4)
    cotas = {('A', 'B'): 1}
    print(flujo_con_cotas_min(grafo, 'S', 'T', cotas))

if __name__ == "__main__":
    main()