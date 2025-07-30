"""
    Funcionamiento análogo al del ejercicio 13. Sin embargo,
a simple vista podría parecer que la complejidad es O(n^2),
pero esto no es así ya que, en el peor de los casos, se
recorre 2 veces el arreglo y como O(2n) = O(n) < O(n log n),
la complejidad final resultante es O(n log n).
"""

def bifurcaciones_con_patrulla(ciudades):
    ciudades.sort(key=lambda x: x[1])
    patrullas = []

    for i in range(len(ciudades)):
        if patrullas and ciudades[i][1] - patrullas[-1][1] <= 50:
            continue

        nueva = ciudades[i]
        for j in range(i + 1, len(ciudades)):
            if ciudades[i][1] + 50 >= ciudades[j][1]:
                nueva = ciudades[j]
            else:
                break

        patrullas.append(nueva)
        
    return patrullas
    

def main():
    print(bifurcaciones_con_patrulla([("C", 185), ("G", 242), ("L", 156), ("M", 270), ("S", 194)]))
    print(bifurcaciones_con_patrulla([("C", 185), ("G", 242), ("S", 194)]))
    ciudades = [("a", 51), ("b", 100), ("c", 149), ("d", 810), ("e", 850), ("f", 901)]
    print(bifurcaciones_con_patrulla(ciudades))

if __name__ == "__main__":
    main()
