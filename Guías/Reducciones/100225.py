from grafo import Grafo

def validador_hamiltonian_completition(grafo_original, k, grafo_mod, camino): # O(V + E + k)
    if len(grafo_original) != len(grafo_mod):
        return False
    
    visitados = set()
    aristas_extra = 0
    for v in grafo_original:
        if v not in grafo_mod:
            return False
        
        for a in grafo_original.adyacentes(v):
            if not a in grafo_mod or not grafo_mod.estan_unidos(v, a):
                return False
            
        for a in grafo_mod.adyacentes(v):
            if not a in grafo_original:
                return False
            if a in visitados and not grafo_mod.es_dirigido():
                continue
            if not grafo_original.estan_unidos(v, a):
                aristas_extra += 1
        visitados.add(v)

    if aristas_extra > k:
        return False
    
    return validador_ciclo_ham(grafo_mod, camino)

def validador_ciclo_ham(grafo, solucion): # O(V)
    if len(solucion) != len(grafo) + 1: # El +1 porque debe volver al 1er. vértice.
        return False
    
    if solucion[0] != solucion[-1]:
        return False
    
    visitados = set()
    for i in range(len(solucion) - 1):
        v = solucion[i]

        if v in visitados:
            return False
        
        if not v in grafo or not solucion[i + 1] in grafo:
            return False
        
        if not grafo.estan_unidos(v, solucion[i + 1]):
            return False

        visitados.add(v)
    
    return True

def main():
    grafo = Grafo(True, ['A', 'B', 'C'])
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'C')

    grafo2 = Grafo(True, ['A', 'B', 'C'])
    grafo2.agregar_arista('A', 'B')
    grafo2.agregar_arista('A', 'C')
    grafo2.agregar_arista('B', 'C')
    grafo2.agregar_arista('C', 'A')
    print(validador_hamiltonian_completition(grafo, 1, grafo2, ['A', 'B', 'C', 'A']))



    print(validador_ciclo_ham(grafo, ['A', 'B', 'C', 'A'])) # True
    print(validador_ciclo_ham(grafo, ['A', 'B', 'C', 'C'])) # False
    print(validador_ciclo_ham(grafo, ['A', 'B', 'C'])) # False
    print(validador_ciclo_ham(grafo, ['A', 'Z', 'C', 'A'])) # False
    print(validador_ciclo_ham(grafo, ['B', 'A', 'C', 'A'])) # False

if __name__ == "__main__":
    main()
