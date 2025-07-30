from math import sqrt

"""
JUSTIFICACIÓN:
        Al inicio se realizan dos operaciones O(N log N), armar px y py.
    Luego, ya en la "función que importa", se realizan operaciones O(N)
    (siendo N la cantidad de elementos a trabajar en el llamado en
    cuestión), tales como armar qx, rx, qy y ry; así como también armar
    sx y sy. Además, calcular la distancia de los puntos de s también es
    O(N), ya que "realmente" se realizan 15 * N operaciones.
        Como se puede observar, la función utiliza la técnica de
    división y conquista partiendo el arreglo en dos mitades y llamado
    recursivamente. Por lo tanto, como se puede inferir, la ecuación de
    recurrencia de esta es:
        T(N) = 2 * T(N/2) + O(N)

        Y, utilizando el teorema maestro y sumando la complejidad de los
    ordenamientos iniciales, se puede concluir que la complejidad final
    del algoritmo resulta O(N log N).
"""

def puntos_mas_cercanos(puntos):
    return _puntos_mas_cercanos(sorted(puntos, key=lambda x: x[0]), sorted(puntos, key=lambda y: y[1]))

def _puntos_mas_cercanos(px, py):
    if len(px) <= 3:
        return mas_cercanos_fuerza_bruta(px)

    medio = len(px) // 2
    qx, rx, qy, ry = px[:medio], px[medio:], [], []
    dqx = set(qx) # O(N)
    for punto in py:
        if punto in dqx:
            qy.append(punto)
        else:
            ry.append(punto)

    q0, q1 = _puntos_mas_cercanos(qx, qy)
    r0, r1 = _puntos_mas_cercanos(rx, ry)
    d = min(calcular_dist(q0, q1), calcular_dist(r0, r1))

    sx, sy, dsx = [], [], set()
    for punto in px:
        if calcular_dist(punto, (px[medio - 1][0], punto[1])) <= d:
            sx.append(punto)
            dsx.add(punto)
    for punto in py:
        if punto in dsx:
            sy.append(punto)
        
    s0, s1 = None, None
    for i in range(len(py)):
        for j in range(i + 1, min(len(py), i + 16)):
            nd = calcular_dist(py[i], py[j])
            if nd < d:
                s0, s1, d = py[i], py[j], nd
    
    if s0:
        return [s0, s1]
    if calcular_dist(q0, q1) <= calcular_dist(r0, r1):
        return [q0, q1]
    return [r0, r1]
    
def mas_cercanos_fuerza_bruta(puntos):
    dist, p0, p1 = float('inf'), None, None
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            ndist = calcular_dist(puntos[i], puntos[j])
            if ndist < dist:
                dist, p0, p1 = ndist, puntos[i], puntos[j]
    return [p0, p1]

def calcular_dist(x0, x1):
    return sqrt((x0[0] - x1[0])**2 + (x0[1] - x1[1])**2)

def main():
    puntos = [(1, 4), (1, 2), (5, 6), (6, 6), (100, 0)]
    print(puntos_mas_cercanos(puntos))

if __name__ == "__main__":
    main()
