"""
Complejidad: O(n^2)
Ecuación de recurrencia:
    OPT(i) = max(max(j * (i - j), OPT(j)) * (i - j)) para todo j perteneciente a [1, i)
"""
def problema_soga(n):
    dp =[0, 1] # El 0 es para mayor comodidad en el manejo de índices.

    for i in range(2, n + 1):
        maximo = dp[-1]
        
        for j in range(i - 2, 0, -1):
            maximo = max(j * (i - j), dp[j] * (i - j), maximo) # Agarro el máximo entre cortarla en 2 partes o más.
        
        dp.append(maximo)

    return dp[-1]

def main():
    print(f'2: {problema_soga(2)}')
    print(f'3: {problema_soga(3)}')
    print(f'4: {problema_soga(4)}')
    print(f'5: {problema_soga(5)}')
    print(f'6: {problema_soga(6)}')
    print(f'7: {problema_soga(7)}')
    print(f'8: {problema_soga(8)}')
    print(f'9: {problema_soga(9)}')
    print(f'10: {problema_soga(10)}')

if __name__ == "__main__":
    main()