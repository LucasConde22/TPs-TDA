from heapq import heappush, heappop

"""
Mismo algoritmo que el desarrollado en el ej. 11.
"""

def cajas(capacidad, libros):
    libros.sort(reverse=True)
    cajas = []

    for libro in libros:
        if cajas and cajas[0][0] + libro <= capacidad:
            espacio, elementos = heappop(cajas)
            heappush(cajas, (espacio + libro, elementos + [libro]))
        else:
            heappush(cajas, (libro, [libro]))
    
    for i in range(len(cajas)):
        cajas[i] = cajas[i][1]
    return cajas

def cajas2(capacidad, libros):
    libros.sort(reverse=True)
    cajas, cap_cajas = [], []

    for libro in libros:
        guardar_en_caja(libro, cajas, cap_cajas, capacidad)
    return cajas

def guardar_en_caja(producto, cajas, cap_cajas, capacidad):
    for i, caja in enumerate(cajas):
            if cap_cajas[i] + producto <= capacidad:
                caja.append(producto)
                cap_cajas[i] += producto
                return
    cajas.append([producto])
    cap_cajas.append(producto)

def main():
    print(cajas(5, [1, 3, 3, 5, 2, 3, 1]))

    cant = 6000
    libros = [i % 5 for i in range(cant)]
    resul = cajas(10, libros)
    cant_elem = 0
    for caja in resul:
        cant_elem += len(caja)
    print(cant_elem == cant)

if __name__ == "__main__":
    main()