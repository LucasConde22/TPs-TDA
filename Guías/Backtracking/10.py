"""
Complejidad temporal: O(6^n)
Complejidad espacial: O(6^n)
*Siendo 'n' la cantidad de tiros.
"""
def sumatoria_dados(n, s):
    combinaciones = []
    _sumar(0, 0, n, s, [], combinaciones)
    return combinaciones

def _sumar(tiradas, sumatoria, tiros, s, actualmente, combinaciones):
    if tiradas == tiros:
        if sumatoria == s:
            combinaciones.append(actualmente[:])
        return
    
    if sumatoria + 6 * (tiros - tiradas) < s: # Si ya no llego por este camino
        return
    
    for i in range(1, 7):
        if sumatoria + i > s:
            return
        actualmente.append(i)
        _sumar(tiradas + 1, sumatoria + i, tiros, s, actualmente, combinaciones)
        actualmente.pop()
    return

def main():
    print(sumatoria_dados(2, 7))
    print(sumatoria_dados(4, 10))
    print(sumatoria_dados(2, 2))
    print(sumatoria_dados(10, 55))

if __name__ == "__main__":
    main()