def nreinas(n):
    solucion = []
    _colocar_reinas(0, solucion, n)
    return solucion

def _validar_reina(fil, col, solucion):
    for rfil, rcol in solucion:
        if rcol == col: # Si están en la misma columna
            return False
        if abs(fil - rfil) == abs(col - rcol): # Si están en la misma diagonal
            return False
    return True

def _colocar_reinas(fil, solucion, n):
    if fil == n:
        return True

    for col in range(n):
        if _validar_reina(fil, col, solucion):
            solucion.append((fil, col))
            if _colocar_reinas(fil + 1, solucion, n):
                return True
            else:
                solucion.pop()
    return False

def main():
    print(nreinas(4))
    print(nreinas(23))

if __name__ == "__main__":
    main()