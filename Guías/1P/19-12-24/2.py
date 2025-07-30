def cambio(n, monedas, cantidad_x_monedas):
    _, asignacion = _cambio(0, monedas, cantidad_x_monedas, 0, [], float('inf'), None, n)
    return asignacion


def _cambio(i, monedas, cantidad_x_monedas, asignadas_act, asignacion, necesarias_min, sol_min, restante):
    if restante == 0:
        return asignadas_act, asignacion[:]
    
    if i == len(monedas) or asignadas_act >= necesarias_min: # Si ya me pasé en cantidad, recorto.
        return necesarias_min, sol_min
    
    for usadas in range(cantidad_x_monedas[monedas[i]] + 1):
        nuevo_restante = restante - monedas[i] * usadas
        if nuevo_restante < 0: # Si ya me pasé en monto, me voy a seguir pasando, así que corto.
            break
        
        if usadas != 0:
            asignacion.append((monedas[i], usadas))

        necesarias_n, sol_n = _cambio(i + 1, monedas, cantidad_x_monedas, asignadas_act + usadas, asignacion, necesarias_min, sol_min, nuevo_restante)
        if necesarias_n < necesarias_min:
            necesarias_min = necesarias_n
            sol_min = sol_n

        if usadas != 0:
            asignacion.pop()
    
    return necesarias_min, sol_min

def main():
    print(cambio(14, [1, 3, 7, 10], {1: 5, 3: 2, 7: 3, 10: 2}))
    print(cambio(14, [1, 3, 7, 10], {1: 5, 3: 2, 7: 1, 10: 2}))
    print(cambio(14, [3, 7, 10], {3: 1, 7: 1, 10: 1}))


if __name__ == "__main__":
    main()
    
    
    

    
        