"""
    Este problema es, en esencia, el de "Set Cover" y, tal como vimos en
clase, este algoritmo de aproximación, que itera a los proveedores
eligiendo siempre el que más productos "no cubiertos" ofrece, consiste
en una H(d)-aproximación, siendo H la función armónica, acotada por
O(log n), y d el proveedor que más productos ofrece. Por lo tanto, se
puede garantizar que el peso obtenido es como mucho O(log n) veces el peso
óptimo.
    Además, está demostrado que no existe ningún algoritmo que pueda dar
una mejor aproximación a menos que P = NP.
"""

# Complejidad: O(E*P^2)
# P = Cant. de proveedores
# E: Cant. de productos
def elegir_proveedores(ofrecen): # ofrecen = {provedor0: [prod0, ..., prodn], ...}
    elegidos = set()
    cubiertos = set()

    while True:
        cant_prods = 0
        prov_max = None

        for proveedor, productos in ofrecen.items():
            if proveedor in elegidos:
                continue

            cubre = 0
            for prod in productos:
                if not prod in cubiertos:
                    cubre += 1
            
            if cubre > cant_prods:
                cant_prods = cubre
                prov_max = proveedor
        
        if cant_prods > 0:
            elegidos.add(prov_max)
            cubiertos.update(ofrecen[prov_max])
        else:
            break

    return list(elegidos)

def main():
    ofrecen = {'0': ['A', 'B', 'C'], '1': ['D'], '2': ['A', 'B', 'E'], '3': ['D'], '4': ['D', 'E']}
    print(elegir_proveedores(ofrecen))

    # ¿Cuando no es óptimo?:
    ofrecen = {'0': ['A', 'B'],
               '1': ['C', 'D', 'E', 'F'],
               '2': ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
               '3': ['A', 'C', 'D', 'G', 'H', 'I', 'J'],
               '4': ['B', 'E', 'F', 'K', 'L', 'M', 'N']}
    print(elegir_proveedores(ofrecen))

if __name__ == "__main__":
    main()
