def knight_tour(n):
    for fil in range(n):
        for col in range(n):
            if il_cavallino_rampante(fil, col, {(fil, col)}, n):
                return True
    return False

def il_cavallino_rampante(fil, col, visitadas, n):
    if len(visitadas) == n*n:
        return True

    for disponible in _buscar_pos_disp(fil, col, visitadas, n):
        visitadas.add(disponible)
        if il_cavallino_rampante(disponible[0], disponible[1], visitadas, n):
            return True
        visitadas.remove(disponible)
    
    return False


def _buscar_pos_disp(fil, col, visitadas, n):
    disponibles = set()

    nfil, ncol = fil - 2, col - 1
    if _validar_pos(nfil, ncol, visitadas, n):
        disponibles.add((nfil, ncol))

    nfil, ncol = fil - 2, col + 1
    if _validar_pos(nfil, ncol, visitadas, n):
        disponibles.add((nfil, ncol))
    
    nfil, ncol = fil + 2, col - 1
    if _validar_pos(nfil, ncol, visitadas, n):
        disponibles.add((nfil, ncol))

    nfil, ncol = fil + 2, col + 1
    if _validar_pos(nfil, ncol, visitadas, n):
        disponibles.add((nfil, ncol))

    nfil, ncol = fil - 1, col + 2
    if _validar_pos(nfil, ncol, visitadas, n):
        disponibles.add((nfil, ncol))

    nfil, ncol = fil + 1, col + 2
    if _validar_pos(nfil, ncol, visitadas, n):
        disponibles.add((nfil, ncol))

    nfil, ncol = fil + 1, col - 2
    if _validar_pos(nfil, ncol, visitadas, n):
        disponibles.add((nfil, ncol))

    nfil, ncol = fil - 1, col - 2
    if _validar_pos(nfil, ncol, visitadas, n):
        disponibles.add((nfil, ncol))

    return disponibles

def _validar_pos(fil, col, visitadas, n):
    rango_min, rango_max = 0, n - 1
    if rango_min <= fil <= rango_max and rango_min <= col <= rango_max and (fil, col) not in visitadas:
        return True
    return False

def main():
    print(knight_tour(3))
    print(knight_tour(2))
    print(knight_tour(4))
    print(knight_tour(5))
    print(knight_tour(1))

if __name__ == "__main__":
    main()