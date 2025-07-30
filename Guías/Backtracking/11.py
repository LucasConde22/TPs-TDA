def sumatorias_n(lista, n):
    resultados = []
    _sumar(0, 0, [], sum(lista), resultados, lista, n)
    return resultados

def _sumar(i, sum_act, lista_act, restantes, resultados, lista, n):
    if sum_act == n:
        resultados.append(lista_act[:])
        return

    if sum_act > n:
        return
    
    if sum_act + restantes < n:
        return

    lista_act.append(lista[i])
    _sumar(i + 1, sum_act + lista[i], lista_act, restantes - lista[i], resultados, lista, n)
    lista_act.pop()

    _sumar(i + 1, sum_act, lista_act, restantes - lista[i], resultados, lista, n)
                
def main():
    print(sumatorias_n([1, 2, 3, 4, 5, 6, 7, 8, 9], 12))
    print(sumatorias_n([7,5,2,6,1,3], 14))

if __name__ == "__main__":
    main()