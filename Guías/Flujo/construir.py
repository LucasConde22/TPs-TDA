from grafo import Grafo

def construir_red_residual(grafo, flujos):
    red_residual = Grafo(True, grafo.obtener_vertices())
    for (v, w), flujo in flujos.items():
        if flujo > 0:
            red_residual.agregar_arista(w, v, flujo)
        if grafo.peso_arista(v, w) > flujo:
            red_residual.agregar_arista(v, w, grafo.peso_arista(v, w) - flujo)
    return red_residual


def construir_dicc_flujos(red_residual, grafo_original):
    flujos = {}
    for v in grafo_original:
        for a in grafo_original.adyacentes(v):
            if red_residual.estan_unidos(a, v):
                flujos[(v, a)] = red_residual.peso_arista(a, v)
            else:
                flujos[(v, a)] = 0
    return flujos

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
    flujos = {("0", "1"): 11, ("0", "2"): 12, ("1", "3"): 12, ("3", "5"): 19,
              ("4", "5"): 4, ("2", "4"): 11, ("2", "1"): 1, ("4", "3"): 7}
    red_residual = construir_red_residual(grafo, flujos)

    for v in red_residual:
        for a in red_residual.adyacentes(v):
            print(f'{v} -> {a}: {red_residual.peso_arista(v, a)}')

    print(construir_dicc_flujos(red_residual, grafo))

if __name__ == "__main__":
    main()
