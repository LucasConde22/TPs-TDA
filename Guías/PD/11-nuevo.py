MAS1 = "mas1"
POR2 = "por2"

"""      
Ecuación de recurrencia:
                        Siendo OPT(K) = Cantidad de operaciones necesarias para llegar a K.
                        Si K = 0,
                                    0.
                        Si K > 0,
                                    OPT(K) = min(OPT(K-1), OPT(K / 2)) + 1 (Si K es impar no debería evaluarse OPT(K / 2)).

Solución bottom-up:
    Complejidad: O(K)
"""
def operaciones(k):
    pasos = [0] * (k + 1)

    for i in range(k + 1):
        # Actualizo el siguiente, si no se había llegado a el anteriormente:
        if i < k and pasos[i + 1] == 0:
            pasos[i + 1] = pasos[i] + 1

        # Actualizo el doble, si no se había llegado a el anteriormente:
        if i != 0 and i * 2 <= k and pasos[i * 2] == 0:
            pasos[i * 2] = pasos[i] + 1
        
        if pasos[k] != 0:
            break

    return reconstruir_operaciones(pasos)

def reconstruir_operaciones(pasos):
    i = len(pasos) - 1

    camino = []
    while pasos[i] != 0:
        if pasos[i] - 1 == pasos[i - 1]:
            camino.append(MAS1)
            i -= 1
        else:
            camino.append(POR2)
            i = i // 2
    
    return camino[::-1]

def main():
    print(operaciones(3))
    print(operaciones(8))
    print(operaciones(2))
    print(operaciones(5))
    print(operaciones(20))
    print(operaciones(0))
    print(operaciones(2000*1000))

if __name__ == "__main__":
    main()
