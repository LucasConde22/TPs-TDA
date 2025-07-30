"""
    Suposición: Ningún trabajo tiene peso negativo/neutro.
    Soluciones:
    0 trabajos: [].

    1 trabajo: Ese trabajo.

    2 trabajos: El que más pague.

    3 trabajos: El primero y el último o solo el del medio.

    4 trabajos: 1ro y 3ro
                2do y 4to
                1ro y 4to --> Tengo que chequear dos posiciones para atrás?

    5 trabajos: 1ro, 3ro y 5to
                2do y 4to
                1ro y 4to
                2do y 5to
                1ro y 5to no tendría sentido omitiendo el 3ro, entonces confirmo que solo debo ver dos posiciones para atrás.
    
    Ejemplo de RPL:
    100
    100, 100
    100, 100, 150
    100, 100, 150, 150
    100, 100, 150, 150, 151
    100, 100, 150, 150, 151, 350

    Entonces, solo necesito guardarme las últimas tres sumatorias.

    Conclusión posterior:
        No, no necesito guardarme la últimas tres sumatorias, con guardar
        las últimas dos es suficiente. Esto se debe a que siempre guardo
        las sumatorias que maximizan, por lo que i-2 va a tener siempre
        el valor que convenga.

    Complejidad: O(n)
    """
def juan_el_vago(trabajos):
    return _recontruir_camino(_obtener_maxima_ganancia(trabajos))

def _obtener_maxima_ganancia(trabajos):
    selecciones = []

    if len(trabajos) >= 1:
        selecciones.append(trabajos[0])
    if len(trabajos) >= 2:
        selecciones.append(max(trabajos[0], trabajos[1]))

    for i in range(2, len(trabajos)):
        selecciones.append(max(selecciones[i-1], trabajos[i] + selecciones[i-2]))

    return selecciones

def _recontruir_camino(selecciones):
    camino = []

    i = len(selecciones) - 1
    while i >= 0:
        if i == 0 or selecciones[i] > selecciones[i-1]:
            camino.append(i)
            i -= 2
        else:
            i -= 1
    return camino[::-1]

def main():
    print(juan_el_vago([100, 5, 50, 1, 1, 200]))
    print(juan_el_vago([]))
    

if __name__ == "__main__":
    main()