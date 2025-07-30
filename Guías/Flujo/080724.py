from grafo import Grafo
from algoritmos import *

# ambulancias = [(id_a1, ubi_a1), (id_a2, ubi_a2), ...]
# pedidos = [(id_p1, ubi_p1), (id_p2, ubi_p2), ...]
# distancias = {(ubi1, ubi2): 5, (ubi2, ubi3): 2} // Asumo que están cargadas (ubii, ubij) y (ubij, ubii) para mayor simplicidad.
# k = Máxima distancia trasladable.

# Complejidad: O((A + P) * E^2)
# A = Cant. de ambulancias.
# P = Cant. de pedidos.
# E = Cant. de posibles emparejamientos entre las ambulancias y los pedidos, cota superior: A*P + A + P.
def asignar_ambulancias(ambulancias, pedidos, distancias, k):
    sf, ss = "super_fuente", "super_sumidero"
    red = Grafo(True, [sf, ss])

    for a, ubia in ambulancias:
        red.agregar_vertice(a)
        red.agregar_arista(sf, a, 1)
        for p, ubip in pedidos:
            if distancias[(ubia, ubip)] > k:
                continue
            if not p in red:
                red.agregar_vertice(p)
                red.agregar_arista(p, ss, 1)
            red.agregar_arista(a, p, 1)
    
    f = flujo(red, sf, ss)
    asignaciones = []
    for a, _ in ambulancias:
        for p in red.adyacentes(a):
            if f[(a, p)] == 1:
                asignaciones.append((a, p))
    return asignaciones

def main():
    ambulancias = [("a1", "ubi1"), ("a2", "ubi2"), ("a3", "ubi3"), ("a4", "ubi9")]
    pedidos = [("p1", "ubi4"), ("p2", "ubi5"), ("p3", "ubi6"), ("p4", "ubi7"), ("p5", "ubi8")]
    distancias = {("ubi1", "ubi4"): 5, ("ubi1", "ubi5"): 6, ("ubi1", "ubi6"): 7, ("ubi1", "ubi7"): 13, ("ubi1", "ubi8"): 14,
                  ("ubi2", "ubi4"): 18, ("ubi2", "ubi5"): 13, ("ubi2", "ubi6"): 2, ("ubi2", "ubi7"): 13, ("ubi2", "ubi8"): 14,
                  ("ubi3", "ubi4"): 5, ("ubi3", "ubi5"): 19, ("ubi3", "ubi6"): 20, ("ubi3", "ubi7"): 10, ("ubi3", "ubi8"): 14,
                  ("ubi9", "ubi4"): 50, ("ubi9", "ubi5"): 60, ("ubi9", "ubi6"): 70, ("ubi9", "ubi7"): 13, ("ubi9", "ubi8"): 1,}
    print(asignar_ambulancias(ambulancias, pedidos, distancias, 12))

if __name__ == "__main__":
    main()

