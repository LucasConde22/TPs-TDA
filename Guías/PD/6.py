from grafo import Grafo

# Solución top-down:
# Complejidad: O(n), siendo n el número de pulsaciones.
def numeros_posibles(k, n):
    if n == 0:
        return 0

    grafo = Grafo(False, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    grafo.agregar_arista('0', '8')
    grafo.agregar_arista('1', '2')
    grafo.agregar_arista('1', '4')
    grafo.agregar_arista('2', '3')
    grafo.agregar_arista('2', '5')
    grafo.agregar_arista('3', '6')
    grafo.agregar_arista('4', '5')
    grafo.agregar_arista('4', '7')
    grafo.agregar_arista('5', '6')
    grafo.agregar_arista('5', '8')
    grafo.agregar_arista('6', '9')
    grafo.agregar_arista('7', '8')
    grafo.agregar_arista('8', '9')

    return _numeros_posibles(str(k), n, {}, grafo)

def _numeros_posibles(k, n, memoization, grafo):
    if (k, n) in memoization:
        return memoization[(k, n)]

    if n == 1:
        return 1
    
    formas = _numeros_posibles(k, n - 1, memoization, grafo)
    for a in grafo.adyacentes(k):
        formas += _numeros_posibles(a, n - 1, memoization, grafo)

    memoization[(k, n)] = formas
    return formas

def main():
    print(numeros_posibles(5, 1)) # 1
    print(numeros_posibles(0, 2)) # 2
    print(numeros_posibles(3, 2)) # 3
    print(numeros_posibles(8, 2)) # 5
    print(numeros_posibles(5, 50)) # 22
    print(numeros_posibles(0, 3)) # < 22

if __name__ == "__main__":
    main()