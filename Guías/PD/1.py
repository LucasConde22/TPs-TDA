# Complejidad: O(n)
def fibonacci(n):
    if n == 0:
        return 1
    
    anterior = 0
    actual = 1

    for i in range(1, n + 1):
        siguiente = anterior + actual
        anterior = actual
        actual = siguiente
    return actual

def main():
    # 0, 1, 1, 2, 3, 5, 8
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(6))

if __name__ == "__main__":
    main()