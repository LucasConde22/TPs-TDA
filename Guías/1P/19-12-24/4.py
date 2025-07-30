def encontrar_limites(coordenadas):
    superior_der = (encontrar_max(coordenadas, 0, 0, len(coordenadas) - 1), encontrar_max(coordenadas, 1, 0, len(coordenadas) - 1))
    inferior_izq = (encontrar_min(coordenadas, 0, 0, len(coordenadas) - 1), encontrar_min(coordenadas, 1, 0, len(coordenadas) - 1))
    return inferior_izq, superior_der

def encontrar_max(coordenadas, param, ini, fin):
    if ini == fin:
        return coordenadas[ini][param]

    medio = (ini + fin) // 2

    if coordenadas[medio - 1][param] <= coordenadas[medio][param] >= coordenadas[medio + 1][param]:
        return coordenadas[medio][param]
    
    if coordenadas[medio][param] <= coordenadas[medio + 1][param] and coordenadas[medio + 1][param] >= coordenadas[medio - 1][param]:
        return encontrar_max(coordenadas, param, medio + 1, fin)
    
    return encontrar_max(coordenadas, param, ini, medio)

def encontrar_min(coordenadas, param, ini, fin):
    if ini == fin:
        return coordenadas[ini][param]

    medio = (ini + fin) // 2

    if coordenadas[medio - 1][param] > coordenadas[medio][param] < coordenadas[medio + 1][param]:
        return coordenadas[medio][param]
    
    if coordenadas[ini][param] < coordenadas[fin][param]:
            return encontrar_min(coordenadas, param, ini, medio)
    return encontrar_min(coordenadas, param, medio + 1, fin)

def main():
    # Formas raras:
    print(encontrar_limites([(7, 4), (8, 7), (5, 8), (2, 9), (3, 3), (6,2)]))
    print(encontrar_limites([(6,2), (7, 4), (8, 7), (5, 8), (2, 9), (3, 3)]))
    print(encontrar_limites([(1, 1), (5, 0), (4, 4), (2, 5)]))
    print(encontrar_limites([(0, 1), (1, 0), (2, 1), (2, 2), (0, 2)]))
    print(encontrar_limites([(2, 1), (2, 2), (0, 2), (0, 1), (1, 0)]))

    print(encontrar_limites([(4, 0), (4, 4), (2, 6), (0, 4), (0, 0)]))
    

    # Cuadrados / Rectángulos:
    print(encontrar_limites([ (0,0), (0,1), (1,1), (1,0)]))
    print(encontrar_limites([(0, 1), (0, 0), (2, 0), (2,1)]))

    # Triángulo:
    print(encontrar_limites([(6, 2), (5, 7), (0, 0)]))



if __name__ == "__main__":
    main()
    

    
