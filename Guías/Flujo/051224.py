from grafo import Grafo
import algoritmos

def caminos_disjuntos(grafo, fuente, sumidero): # O(V*E^2)
    red = Grafo(True, grafo.obtener_vertices())
    intermedios = {}

    for v in grafo:
        if v == sumidero:
            continue # Al sumidero no le pongo aristas de salida.
        for a in grafo.adyacentes(v):
            if a == fuente:
                continue # A la fuente no le pongo aristas de entrada.
            if not red.estan_unidos(a, v):
                red.agregar_arista(v, a, 1) # Como busco caminos disjuntos, la capacidad debe ser 1. No importa si el grafo original es pesado.
            else:
                red.agregar_vertice(f'{v}_{a}')
                red.agregar_arista(v, f'{v}_{a}', 1)
                red.agregar_arista(f'{v}_{a}', a, 1)
                intermedios[f'{v}_{a}'] = (v, a)
    
    flujo = algoritmos.flujo(red, fuente, sumidero)

    for inter, (v, a) in intermedios.items(): # Si el flujo pasa por una misma arista dos veces lo anulo.
        if flujo[(v, inter)] == 1 and flujo[(a, v)] == 1:
            flujo[(a, v)] = 0
            flujo[(v, inter)] = 0
            flujo[(inter, a)] = 0

    caminos = []
    cant_caminos = 0
    for a in red.adyacentes(fuente):
        if flujo[(fuente, a)] == 1:
            cant_caminos += 1

    while len(caminos) < cant_caminos:
        camino, v = [fuente], fuente

        while v != sumidero:
            cambio = False

            for a in red.adyacentes(v):
                if flujo[(v, a)] == 0:
                    continue
                if a not in intermedios:
                    camino.append(a)
                flujo[(v, a)] = 0
                v, cambio = a, True
                break

            if not cambio:
                break

        if camino[-1] == sumidero:
            caminos.append(camino)
    
    return caminos, cant_caminos

def main():
    grafo = Grafo(False, ['A', 'B', 'C', 'D'])
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'C')
    grafo.agregar_arista('B', 'D')
    grafo.agregar_arista('C', 'D')
    print(caminos_disjuntos(grafo, 'A', 'D'))

if __name__ == "__main__":
    main()



