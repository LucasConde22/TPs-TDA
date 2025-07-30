from grafo import Grafo
from algoritmos import flujo
from construir import construir_red_residual

def main():
    grafo = Grafo(True, ['SF', 'e', '0', '1', '2', '3', '4', '5', '6', '7', '8'])
    grafo.agregar_arista('SF', '0', 29)
    grafo.agregar_arista('SF', '8', 2)
    grafo.agregar_arista('0', '1', 16)
    grafo.agregar_arista('0', '2', 13)
    grafo.agregar_arista('1', '3', 12)
    grafo.agregar_arista('2', '1', 4)
    grafo.agregar_arista('2', '4', 14)
    grafo.agregar_arista('3', '6', 20)
    grafo.agregar_arista('4', '3', 7)
    grafo.agregar_arista('4', '6', 4)
    grafo.agregar_arista('4', 'e', 3)
    grafo.agregar_arista('e', '5', 3)
    grafo.agregar_arista('5', '2', 3)
    grafo.agregar_arista('5', '4', 7)
    grafo.agregar_arista('5', '7', 6)
    grafo.agregar_arista('7', '6', 5)
    grafo.agregar_arista('8', '5', 2)

    f = flujo(grafo, 'SF', '6')
    print(f)

    red_residual = construir_red_residual(grafo, f)
    red_residual.agregar_arista('2', '3', 9)

    for v in red_residual:
        print(f'v: {v}')
        for a in red_residual.adyacentes(v):
            print(f'   a: {a}, peso {red_residual.peso_arista(v, a)}')


if __name__ == "__main__":
    main()

