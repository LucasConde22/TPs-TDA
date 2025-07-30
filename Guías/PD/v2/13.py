def bodegon_dinamico(P, W):
    asignacion = [0] * (W + 1)

    for i in range(len(P)):
        for j in range(1, W + 1):
            if P[i] > j:
                continue
            asignacion[j] = max(asignacion[i], P[i] + asignacion[j - P[i]])

    print(asignacion)
    return reconstruir(asignacion, P)

def reconstruir(asignacion, P):
    camino = []
    i = len(P) - 1
    j = len(asignacion) - 1

    while i >= 0:
        if j >= P[i] and asignacion[j] == P[i] + asignacion[j - P[i]]:
            camino.append(P[i])
            j -= P[i]
        i -= 1
    
    return camino[::-1]

def main():
    print(bodegon_dinamico([], 11))
    print(bodegon_dinamico([5], 11))
    print(bodegon_dinamico([5, 4, 6, 10], 11))
    print(bodegon_dinamico([30, 10, 4, 20, 15], 28))

if __name__ == "__main__":
    main()