from grafo import Grafo

"""
OPT(s) = 0
OPT(i) = max(OPT(j) + peso(j, i) para todo j incidente en i),
            para todo vértice i != s que pueda formar parte de un camino entre s y t.
"""

def camino_peso_max(s, t, grafo): # O(V + E)
    incidencias = buscar_incidencias(grafo)
    peso_camino = {}
    caminos_pd_top_down(t, incidencias, peso_camino, s, grafo)
    return reconstruir(s, t, peso_camino, incidencias, grafo)

def caminos_pd_top_down(act, incidencias, peso_camino, s, grafo): # O(V + E)
    if act == s:
        peso_camino[s] = 0
        return
    
    peso_max = float('-inf')
    for a in incidencias[act]:
        if a not in peso_camino:
            caminos_pd_top_down(a, incidencias, peso_camino, s, grafo)
        peso_max = max(peso_max, peso_camino[a] + grafo.peso_arista(a, act))
    peso_camino[act] = peso_max

def reconstruir(s, t, peso_camino, incidencias, grafo): # O(V + E)
    camino = [t]
    act = t
    while act != s:
        for a in incidencias[act]:
            if peso_camino[act] - grafo.peso_arista(a, act) == peso_camino[a]:
                act = a
                break
        camino.append(a)
    return camino[::-1]

def buscar_incidencias(grafo): # O(V + E)
    incidencias = {}
    for v in grafo:
        if not v in incidencias:
            incidencias[v] = []
        for a in grafo.adyacentes(v):
            incidentes = incidencias.get(a, [])
            incidentes.append(v)
            incidencias[a] = incidentes
    return incidencias

def main():
    grafo = Grafo(True, ['0', 'a', 'b', 'c', 'd', '1'])
    grafo.agregar_arista('0', 'a', 2)
    grafo.agregar_arista('0', 'd', 4)
    grafo.agregar_arista('a', 'b', 5)
    grafo.agregar_arista('a', 'c', 4)
    grafo.agregar_arista('b', 'd', 3)
    grafo.agregar_arista('c', 'b', 2)
    grafo.agregar_arista('c', 'd', 3)
    grafo.agregar_arista('d', '1', 1)
    print(camino_peso_max('a', 'd', grafo))

if __name__ == "__main__":
    main()