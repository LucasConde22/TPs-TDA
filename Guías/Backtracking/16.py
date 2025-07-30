from grafo import Grafo

def pintar_colectivos(colectivos, paradas):
    grafo = modelar_grafo(colectivos, paradas)
    return _asignar_colores(grafo, grafo.obtener_vertices(), 0, {}, 0, len(colectivos))

def _validar_color(grafo, asignados, v):
    for a in asignados:
        if a == v:
            continue
        if grafo.estan_unidos(v, a) and asignados[a] == asignados[v]:
            return False
    return True

def _asignar_colores(grafo, vertices, i, asignados, cant_asignados, limite):
    if cant_asignados >= limite:
        return limite
    
    if i == len(vertices):
        return cant_asignados

    for color in range(1, limite):
        asignados[vertices[i]] = color
        if not _validar_color(grafo, asignados, vertices[i]):
            continue

        limite = _asignar_colores(grafo, vertices, i + 1, asignados, max(cant_asignados, color), limite)

    del asignados[vertices[i]]
    return limite

def modelar_grafo(vertices, conexiones):
    grafo = Grafo(False, vertices)
    for conexion in conexiones:
        for v in conexion:
            for a in conexion:
                if v == a or grafo.estan_unidos(v, a):
                    continue
                grafo.agregar_arista(v, a)
    return grafo

def main():
    colectivos = ["C1", "C2", "C3", "C4"]
    paradas = [
        ["C1", "C2"],  # C1 y C2 comparten una parada
        ["C2", "C3"],  # C2 y C3 comparten una parada
        ["C3", "C4"],  # C3 y C4 comparten una parada
        ["C1", "C4"]   # C1 y C4 comparten una parada
    ]
    print(pintar_colectivos(colectivos, paradas))

    c1 = ['0', '1', '2', '3', '4', '5', '6']
    paradas_grafo_1 = [
    ['0', '1', '3'],
    ['1', '2'],
    ['2', '5'],
    ['3', '4'],
    ['4', '5'],
    ['6'],
    ]
    print(pintar_colectivos(c1, paradas_grafo_1))

    c2 = ['0', '1', '2', '3', '4', '5', '6']
    paradas_grafo_2 = [
    ['0', '1', '3'],
    ['1', '2'],
    ['2', '5'],
    ['3', '4'],
    ['4', '5'],
    ['6', '2'],
    ['6', '3'],
    ['6', '5'],
    ]
    print(pintar_colectivos(c1, paradas_grafo_1))


if __name__ == "__main__":
    main()