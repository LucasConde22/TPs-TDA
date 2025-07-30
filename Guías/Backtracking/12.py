def max_sumatoria_n(lista, n):
    resultado, _ = _hallar_sumatoria(0, 0, [], lista, n)
    return resultado

def _hallar_sumatoria(i, sumatoria_act, lista_act, lista, n):
    if sumatoria_act == n or i == len(lista): # Devuelve la lista que suma n o su maximización
        return lista_act[:], sumatoria_act
    
    result, sum_obtenida = [], 0
    if sumatoria_act + lista[i] <= n: # Si me paso, recorto esta rama
        lista_act.append(lista[i])
        result, sum_obtenida = _hallar_sumatoria(i + 1, sumatoria_act + lista[i], lista_act, lista, n)
        if sum_obtenida == n: # Si ya encontré solución, devuelvo de una
            return result, sum_obtenida
        lista_act.pop()

    result2, sum_obtenida2 = _hallar_sumatoria(i + 1, sumatoria_act, lista_act, lista, n) # Busco una solución mejor
    if sum_obtenida2 > sum_obtenida:
        return result2, sum_obtenida2
    return result, sum_obtenida

def main():
    print(max_sumatoria_n([1, 4, 2, 7, 4, 5], 19))

if __name__ == "__main__":
    main()
