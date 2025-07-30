from grafo import Grafo
import algoritmos

def listar_representantes(habitantes): # habitantes = [(habitante, [clubes], partido), ...]
    grafo = Grafo(True, ['s', 't'])
    agregados = set()
    for habitante, clubes, partido in habitantes:
        grafo.agregar_vertice(f'{habitante}_c')
        grafo.agregar_vertice(f'{habitante}_p')
        grafo.agregar_vertice(habitante)

        if not partido in agregados:
            grafo.agregar_vertice(partido)
            grafo.agregar_arista('s', partido, len(habitantes) // 2)
            agregados.add(partido)
        grafo.agregar_arista(partido, f'{habitante}_p', 1)

        for club in clubes:
            if not club in agregados:
                grafo.agregar_vertice(club)
                grafo.agregar_arista('s', club, 1)
                agregados.add(club)
        grafo.agregar_arista(club, f'{habitante}_c', 1)

        grafo.agregar_arista(f'{habitante}_c', habitante, 1)
        grafo.agregar_arista(f'{habitante}_p', habitante, 1)
        grafo.agregar_arista(habitante, 't', 2)

        flujo = algoritmos.flujo(grafo, 's', 't')
        representantes = []
        for habitante, _, _ in habitantes:
            if flujo[(habitante, 't')] != 0:
                representantes.append(habitante)
        return representantes
    
