from grafo import Grafo

"""
Complejidad temporal:
            O(V)

Complejidad espacial:
            O(V)
            No, no se puede optimizar más. Esto se debe a que en ese
            caso solo podría obtenerse la suma mínima del dominating
            set pero no podría reconstruirse la solución.

Ecuación de recurrencia:
            OPT(i) = min(OPT(i - 1), OPT(i - 2)) + vi
            Entando todos los i-esimos vétices ordenados topologicamente,
            por su único orden válido.
"""
def ds_pd(grafo, valor):
    orden = obtener_orden_topologico(grafo)
    suma_ds = [0] * len(orden)
    suma_ds[0] = valor[orden[0]] # El primero solo puede ser dominado por si mismo.

    for i in range(1, len(orden)):
        ante_anterior = suma_ds[i - 2] if i > 1 else 0
        anterior = suma_ds[i - 1] if i > 0 else 0

        if anterior > ante_anterior:
            suma_ant = anterior
        else:
            suma_ant = ante_anterior + valor[orden[i - 1]]
        
        if ante_anterior + valor[orden[i - 1]] == anterior:
            suma_act = ante_anterior + valor[orden[i]]
        else:
            suma_act = anterior + valor[orden[i]]

        suma_ds[i] = min(suma_ant, suma_act)

    print(suma_ds)
    return suma_ds[-1], reconstruir_camino(suma_ds, orden, valor)

def reconstruir_camino(suma_ds, orden, valor):
    camino = [orden[0]]
    acumulado = valor[orden[0]]

    for i in range(1, len(suma_ds)):
        if acumulado + valor[orden[i]] == suma_ds[i]:
            camino.append(orden[i])
            acumulado += valor[orden[i]]
        elif acumulado + valor[orden[i - 1]] == suma_ds[i]:
            camino.append(orden[i - 1])
            acumulado += valor[orden[i - 1]]

    return camino



def obtener_orden_topologico(grafo):
    entrada = {grafo.adyacentes(v)[0]: 1 for v in grafo if len(grafo.adyacentes(v)) != 0}
    orden = [v for v in grafo if v not in entrada]
    while len(orden) != len(grafo):
        orden.append(grafo.adyacentes(orden[-1])[0])
    return orden

def main():
    grafo = Grafo(True, ['a', 'b', 'c', 'd'])
    grafo.agregar_arista('a', 'b')
    grafo.agregar_arista('b', 'c')
    grafo.agregar_arista('c', 'd')
    print(ds_pd(grafo, {'a': 2, 'b': 3, 'c': 2, 'd': 1}))

    grafo = Grafo(True, ['a', 'b', 'c', 'd'])
    grafo.agregar_arista('a', 'b')
    grafo.agregar_arista('b', 'c')
    grafo.agregar_arista('c', 'd')
    print(ds_pd(grafo, {'a': 2, 'b': 2, 'c': 20, 'd': 1}))

if __name__ == "__main__":
    main()
