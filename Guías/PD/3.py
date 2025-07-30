# Complejidad: O(n)
def escalones(n):
    if n == 0 or n == 1:
        # Si n = 0, 1 manera de no moverme
        # Si n = 1, 1 solo paso
        return 1
    
    if n == 2:
        # Un paso doble o dos simples
        return 2
    
    if n == 3:
        # 3 pasos simples, 1 doble y 1 simple, 1 simple y 1 doble o 1 triple
        return 4
    
    # escalones(n - 1) + escalones(n - 2) + escalones(n - 3)
    menos3 = 1
    menos2 = 2
    menos1 = 4
    for _ in range(4, n + 1):
        actual = menos1 + menos2 + menos3
        menos3 = menos2
        menos2 = menos1
        menos1 = actual
    return menos1

def main():
    print(escalones(4))
    print(escalones(5))


if __name__ == "__main__":
    main()