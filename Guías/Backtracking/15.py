def max_grupos_bodegon(P, W):
    aproximacion, restantes = _aprox_greedy(P, W)
    if restantes == 0:
        return aproximacion
    solucion, _ = _hallar_grupos_bt(0, P, [], W, restantes, sum(P))
    return solucion

def _hallar_grupos_bt(i, P, sol_parcial, dif_actual, dif_tope, sum_restantes):
    if dif_actual < 0:
        return None, float('inf')
    
    if dif_actual - sum_restantes > dif_tope:
        return None, float('inf')
    
    if i == len(P):
        return sol_parcial[:], dif_actual

    sol_parcial.append(P[i])
    sol_con, dif_con = _hallar_grupos_bt(i + 1, P, sol_parcial, dif_actual - P[i], dif_tope, sum_restantes - P[i])
    sol_parcial.pop()

    sol_sin, dif_sin = _hallar_grupos_bt(i + 1, P, sol_parcial, dif_actual, min(dif_tope, dif_con), sum_restantes - P[i])

    if dif_con <= dif_sin:
        return sol_con, dif_con
    return sol_sin, dif_sin

def _aprox_greedy(P, W):
    # Desactivo ordenamiento previo porque hace fallar pruebas de RPL
    # P = sorted(P, reverse=True)
    seleccionados = []
    for cant_personas in P:
        if W - cant_personas >= 0:
            W -= cant_personas
            seleccionados.append(cant_personas)
    return seleccionados, W

def main():
    print(max_grupos_bodegon([5, 4, 6, 10], 11))

if __name__ == "__main__":
    main()