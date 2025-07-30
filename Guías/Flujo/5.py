import algoritmos
import construir
from grafo import Grafo

def aumentar_flujo(red, flujo, fuente, sumidero): # Podría buscar la fuente y el sumidero en lugar de recibirlos.
    red_residual = construir.construir_red_residual(red, flujo)
    camino = algoritmos.buscar_camino(red_residual, fuente, sumidero)
    capacidad_camino = algoritmos.buscar_minimo(camino, red_residual)
    for i in range(len(camino) - 1):
        v, w = camino[i], camino[i + 1]
        if red.estan_unidos(v, w):
            flujo[(v, w)] += capacidad_camino
        else:
            flujo[(w, v)] += capacidad_camino
    return flujo
        
def main():
    grafo = Grafo(True, ["A", "B", "C"])
    grafo.agregar_arista('C', 'A', 4)
    grafo.agregar_arista('A', 'B', 4)
    flujo = {("C", "A"): 3, ("A", "B"): 3}
    print(aumentar_flujo(grafo, flujo, "C", "B"))

if __name__ == "__main__":
    main()
