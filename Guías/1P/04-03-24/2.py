"""
Ecuación de recurrencia:
    OPT(ini, fin) = max -> v[ini] + min(OPT(ini + 2, fin), OPT(ini + 1, fin - 1))
                        -> v[fin] + min(OPT(ini + 1, fin - 1), OPT(ini, fin - 2))
"""
def maximizar_valor(monedas):
    return _maximizar_valor_rec(0, len(monedas) - 1, monedas, {})

def _maximizar_valor_rec(ini, fin, monedas, memoization):
    if ini > fin:
        return 0

    if (ini, fin) in memoization:
        return memoization[(ini, fin)]
    
    # Elije la primera y el hermano la primera o última buscando minimizar la ganancia de Pepe
    ganancia_primera = monedas[ini] + min(_maximizar_valor_rec(ini + 2, fin, monedas, memoization),
                                          _maximizar_valor_rec(ini + 1, fin - 1, monedas, memoization))
    
    # Elije la última y el hermano la primera o última buscando minimizar la ganancia de Pepe
    ganancia_ultima = monedas[fin] + min(_maximizar_valor_rec(ini + 1, fin - 1, monedas, memoization),
                                          _maximizar_valor_rec(ini, fin - 2, monedas, memoization))

    ganancia = max(ganancia_primera, ganancia_ultima)
    memoization[(ini, fin)] = ganancia
    return ganancia

def main():
    print(maximizar_valor([5, 2]))
    print(maximizar_valor([5, 2, 8, 6, 7, 3, 4]))

if __name__ == "__main__":
    main()