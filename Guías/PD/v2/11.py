"""
OPT(i) = 0, si i = 0
         min(OPT(i - 1), OPT(i / 2)), si i % 2 = 0
         OPT(i - 1), si i % 2 != 0
"""

def operaciones(k): # O(K)
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        if i % 2 != 0:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = min(dp[i - 1], dp[i // 2]) + 1

    return reconstruir(dp)

def reconstruir(dp):
    camino = []
    i = len(dp) - 1

    while i > 0:
        if dp[i] == dp[i - 1] + 1:
            camino.append("mas1")
            i -= 1
        else:
            camino.append("por2")
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