from grafo import Grafo

"""
Complejidad final del algoritmo: O(V + E)

La solución es optima. Supongamos que existe una solución mejor.
En ese caso, la solución debería tener más invitados pero, como
todos deben tener >= 4 conocidos y mi solución solo elimina a
los posibles invitados con < 4 conocidos (que también conocen a
< 4 personas), es imposible que exista una solución más optima.
"""

# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):
    invitados = Grafo(False)

    # Modelo un grafo: (Posible invitado) <-conoce-> (Posible invitado).
    # O(2V) -> O(V)
    for pareja in conocidos:
        if not pareja[0] in invitados:
            invitados.agregar_vertice(pareja[0])
        if not pareja[1] in invitados:
            invitados.agregar_vertice(pareja[1])
        if not invitados.estan_unidos(pareja[0], pareja[1]):
            invitados.agregar_arista(pareja[0], pareja[1])

    # Acá commienza la parte Greedy, donde itero a los presuntos invitados
    # y voy, de manera "codiciosa", borrando a los que no cumplen los
    # requisitos (conocer a >= 4 invitados). De est manera, me acerco en
    # cada iteración a una solución optima global.
    # O(4(V + E)) -> O(V + E)
    while True:
        borrables = []
        for persona in invitados:
            if len(invitados.adyacentes(persona)) < 4: # En mi implementación, obtener los adyacentes es O(E).
                borrables.append(persona)
        
        if not borrables:
            break

        for persona in borrables:
            invitados.borrar_vertice(persona)
        
    # Una vez descartados los no invitados, solo queda devolver los
    # invitados restantes.
    return invitados.obtener_vertices()
    
def main():
    lista = [("1", "a"),
             ("1, 2"),
             ("2", "3"),
             ("2", "4"),
             ("2", "5"),
             ("4", "5"),
             ("a", "b"),
             ("a", "c"),
             ("a", "d"),
             ("a", "e"),
             ("a", "f"),
             ("b", "c"),
             ("b", "d"),
             ("b", "e"),
             ("b", "f"),
             ("c", "d"),
             ("c", "f"),
             ("d", "f")]
    print(obtener_invitados(lista))


    conocidos = [("A", "B"),("B", "C"),("C", "D"),("A", "C"),("A", "D"),("B", "D")]
    print(obtener_invitados(conocidos))

if __name__ == "__main__":
    main()