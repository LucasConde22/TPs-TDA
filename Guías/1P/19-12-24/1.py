"""
Complejidad:
            O(n * m)

¿Por qué es Greedy?
            El algoritmo es Gredy ya que dado el estado inicial, de no tener ningún guardia
            colocado, itera cada posición con la heuristica de si debe o no colocar un
            guardia. Para esto simplemente verifica las celdas que este vigilaría y si no
            hay ningún otro guardia en alguna de ellas, coloca uno nuevo. Cabe destacar que,
            como en todo algoritmo Greedy, los guardias ya colocados nunca son
            "descolocados" por lo que todas las deciciones son las mejores en el momento
            dado (óptimos locales) y finalmente permiten llegar a una solución general que,
            como explico a continuación, no es óptima.

¿Es óptimo?
            Si, el algoritmo es óptimo. Esto se debe a que como buscamos maximizar la cantidad
            de guardias, simplemente colocamos uno en cada posición donde es posible (sin
            importarnos, por ejemplo, si una celda la cubren dos guardias). En cambio, si el
            problema se tratase de minimizar la cantiddad de guardias necesarios para vigilar
            todo el tablero si se trataría de un problema cuya solución Greedy no sería óptima
            (incluso podría plantearse este mismo algoritmo como posible solución).
"""
def colocar_guardias(n, m):
    guardias = []
    suelo = suelo = [[False] * m for _ in range(n)]
    
    for fil in range(len(suelo)):
        for col in range(len(suelo[0])):
            arr = suelo[fil - 1][col] if fil > 0 else False
            arr_izq = suelo[fil - 1][col - 1] if fil > 0 and col > 0 else False
            arr_der = suelo[fil - 1][col + 1] if fil > 0 and col < len(suelo[0]) - 1 else False
            izq = suelo[fil][col - 1] if col > 0 else False
            der = suelo[fil][col + 1] if col < len(suelo[0]) - 1 else False
            ab = suelo[fil + 1][col] if fil < len(suelo) - 1 else False
            ab_izq = suelo[fil + 1][col - 1] if fil < len(suelo) - 1 and col > 0 else False
            ab_der = suelo[fil + 1][col + 1] if fil < len(suelo) - 1 and col < len(suelo[0]) - 1 else False

            if arr or arr_izq or arr_der or izq or der or ab or ab_izq or ab_der:
                continue
            else:
                suelo[fil][col] = True
                guardias.append((fil, col))

    return guardias



def main():
    print(colocar_guardias(5, 4))

if __name__ == "__main__":
    main()