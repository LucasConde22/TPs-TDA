"""
COMPLEJIDAD:
    T(N) = 1 * T(N/2) + O(1)
    con T.M.: O(log N)
"""

def raiz(funcion, a, b):
    medio = (a + b) // 2

    result = funcion(medio)

    if result == 0:
        return medio
    if (funcion(a) <= 0 and result > 0) or (funcion(a) >= 0 and result < 0): # Si los signos del extremo izq y el medio son !=, voy por izq.
        return raiz(funcion, a, medio)
    return raiz(funcion, medio + 1, b)

def main():
    def f1(x):
        return x + 3
    print(raiz(f1, -5, 5)) # -3

    def f2(x):
        return 3*x - 6
    print(raiz(f2, -3, 10)) # 2

    def f3(x):
        return x*x - 2*x
    print(raiz(f3, -7, 7)) # 0 o 2
    print(raiz(f3, 1, 24)) # 2

    def f4(x):
        return -(x*x) + 25
    print(raiz(f4, -11, 7)) # -5 o 5

    def f5(x):
        return (x - 2) * (x - 8)
    print(raiz(f5, 0, 8)) # 2 u 8
    print(raiz(f5, 5, 11)) # 2 u 8
    print(raiz(f5, -100, 4))
    print(raiz(f5, -1, 4)) # 2 o 8

if __name__ == "__main__":
    main()