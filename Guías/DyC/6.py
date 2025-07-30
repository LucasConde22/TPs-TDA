"""
JUSTIFICACIÓN:
Ecuación de recurrencia: T(N) = 3 * T(N/2) + O(N),
ya que en cada llamado realizo operaciones O(N)
(convertir nro a string) y llamo recursivamente
3 veces con nros que representan particiones por
mitades de los nros del llamado anterior.

con T.M: log2(3) > 1 -> O(n^1,59)
"""

def multiplicar(a, b):
    if a < 10 or b < 10:
        return a * b
    
    m = max(len(str(a)), len(str(b))) // 2

    x1, x0 = a // 10 ** m, a % 10 ** m
    y1, y0 = b // 10 ** m, b % 10 ** m

    x1y1 = multiplicar(x1, y1)
    x0y0 = multiplicar(x0, y0)
    p = multiplicar(x1 + x0, y1 + y0)

    return x1y1 * 10**(m * 2) + (p - x1y1 - x0y0) * 10**m + x0y0

def main():
    print(multiplicar(5467, 8210))
    print(multiplicar(20, 10))
    print(multiplicar(128, 303))
    print(multiplicar(-200, 100))

if __name__ == "__main__":
    main()
 
