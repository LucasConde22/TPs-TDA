MAS1 = "mas1"
POR2 = "por2"

def operaciones(k):
    matriz = []
    for i in range(k + 1):
        matriz.append([0] * (k + 1))

        for j in range(1, k + 1):
            if matriz[i-1][j] != 0:
                matriz[i][j] = matriz[i-1][j]
            elif j == i + 1:
                matriz[i][j] = 1
            elif j == i * 2:
                matriz[i][j] = 2

            if j > i * 2:
                break
        
        if matriz[i][k]:
            break

    return reconstruir_operaciones(matriz)

def reconstruir_operaciones(matriz):
    fil, col = len(matriz) - 1, len(matriz[0]) - 1

    camino = []
    while fil >= 0:
        if fil != 0 and matriz[fil][col] == matriz[fil - 1][col]:
            fil -= 1
            continue

        if matriz[fil][col] == 1:
            camino.append(MAS1)
        elif matriz[fil][col] == 2:
            camino.append(POR2)
        fil, col = fil - 1, fil
    
    return camino[::-1]

def main():
    print(operaciones(8))
    print(operaciones(2))
    print(operaciones(5))
    print(operaciones(20))
    print(operaciones(0))
    #print(operaciones(2000*1000))

if __name__ == "__main__":
    main()
