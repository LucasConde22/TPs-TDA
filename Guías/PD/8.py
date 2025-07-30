# Complejidad: O(N*M), siendo N la cantidad de monedas y M el monto.
def cambio(monedas, monto):
    if monto == 0:
        return []

    matriz = [] # Matriz donde cuando la cantidad minima de monedas necesarias para cada submonto.
    for _ in range(len(monedas)):
        matriz.append([])
        for _ in range(monto):
            matriz[-1].append(0)

    for i in range(len(monedas)):
        for j in range(monto):
            necesarias = (j + 1) // monedas[i] # Cantidad de monedas necesarias de la moneda en iteración.
            restante = (j + 1) % monedas[i]

            if restante == 0:
                nuevas = necesarias
            else:
                nuevas = necesarias + matriz[i-1][restante-1] # La cantidad de monedas restantes necesarias es seleccionada de lo calculado anteriormente.

            if i != 0:
                matriz[i][j] = min(nuevas, matriz[i-1][j]) # Si antes se usaban menos monedas, queda el nro. anterior.
            else:
                matriz[i][j] = nuevas
        
    return reconstruir_camino(monedas, monto, matriz)

def reconstruir_camino(monedas, monto, matriz):
    fil, col = len(monedas) - 1, monto - 1
    cambio = []

    while col != -1:
        if fil != 0 and matriz[fil][col] == matriz[fil - 1][col]: # Si un casillero es igual al de la fila anterior, no se uso esa moneda.
            fil = fil - 1
            continue

        usadas = (col + 1) // monedas[fil]
        restante = (col + 1) % monedas[fil]
        cambio += [monedas[fil]] * usadas # Guardo las K monedas utilizadas.
        fil, col = fil - 1, restante - 1 # Paso a la columna del restante en la fila anterior.

    return cambio

def main():
    print(cambio([1, 2, 7, 10], 15))
    print(cambio([1, 2, 7, 10], 14))
    print(cambio([1, 2, 5, 10], 30))
    print(cambio([1, 2, 3], 0))
    print(cambio([1, 2, 3], 2))
    print(cambio([2, 2, 2], 6))

if __name__ == "__main__":
    main()

