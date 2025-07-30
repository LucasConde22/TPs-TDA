"""
Misma justificación y complejidad que ej. 7.
"""

def precios_deflacion(R):
    total = 0
    R.sort()
    for i, producto in enumerate(R):
        total += producto / (2**i)
    return total

def main():
    print(precios_deflacion([3, 9, 11, 2, 1, 20]))

if __name__ == "__main__":
    main()