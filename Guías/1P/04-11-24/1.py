def mochila_almenos_k(elementos, w, k):
    val_restante = sum(elementos[i][0] for i in range(len(elementos)))
    sol, _ = _mochila_almenos_k_bt(0, elementos, k, w, val_restante, [], 0, 0, None, float('-inf'))
    return sol

def _mochila_almenos_k_bt(i, elementos, k, w, val_restante, sol_parcial, val_parcial, peso_actual, sol_optima, val_optimo):
    # Si me pasé del peso máximo o ya no llego a mejorar la mejor solución, recorto:
    if peso_actual > w or val_parcial + val_restante < val_optimo:
        return sol_optima, val_optimo

    if w == peso_actual or i == len(elementos):
        if val_parcial > val_optimo and k <= 0:
            return sol_parcial[:], val_parcial
        return sol_optima, val_optimo
    
    # Con elemento:
    sol_parcial.append(elementos[i])
    sol_optima, val_optimo = _mochila_almenos_k_bt(i + 1, elementos, k - 1, w,
                                                val_restante - elementos[i][0], sol_parcial,
                                                val_parcial + elementos[i][0],
                                                peso_actual + elementos[i][1], sol_optima,
                                                val_optimo)
    sol_parcial.pop()
    # Sin elemento:
    sol_optima, val_optimo = _mochila_almenos_k_bt(i + 1, elementos, k, w,
                                                 val_restante - elementos[i][0],
                                                 sol_parcial, val_parcial, peso_actual,
                                                 sol_optima, val_optimo)
    
    return sol_optima, val_optimo

def main():
    print(mochila_almenos_k([(2, 1), (5, 4), (2, 3), (4, 3)], 10, 2))
    print(mochila_almenos_k([(2, 1), (5, 4), (2, 3), (4, 3)], 10, 0))
    print(mochila_almenos_k([(2, 1), (5, 4), (2, 3), (4, 3)], 10, 5))
    print(mochila_almenos_k([], 10, 4))
    print(mochila_almenos_k([(2, 3), (2, 1), (4, 3), (9,4)], 8, 3))
    print(mochila_almenos_k([(30, 3), (14, 2), (1, 1), (1, 1), (1, 1)], 4, 3))

if __name__ == "__main__":
    main()