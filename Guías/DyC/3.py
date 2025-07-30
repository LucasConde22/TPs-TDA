"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(N) = 1 * T(N/2) + O(1),
ya que llamo recursivamente para un único rango
que contiene la solución. Este rango resulta de
partir a la mitad el rango anterior (inicialmente
es [0, N]). También realizo operaciones O(1)

con T.M: log2(1) = 0 -> O(log n)
"""

def parte_entera_raiz(n):
    return _parte_entera_raiz(0, n, n)

def _parte_entera_raiz(ini, fin,  buscado):
    medio = (ini + fin) // 2

    if medio * medio <= buscado:
        if (medio + 1) * (medio + 1) > buscado:
            return medio
        return _parte_entera_raiz(medio + 1, fin, buscado)
    return _parte_entera_raiz(ini, medio, buscado)

def main():
    print(parte_entera_raiz(10)) # 3
    print(parte_entera_raiz(25)) # 5
    print(parte_entera_raiz(2)) # 1
    print(parte_entera_raiz(1)) # 1
    print(parte_entera_raiz(0)) # 0
    print(parte_entera_raiz(81)) # 9
    print(parte_entera_raiz(17)) # 4
    print(parte_entera_raiz(60)) # 7

if __name__ == "__main__":
    main()