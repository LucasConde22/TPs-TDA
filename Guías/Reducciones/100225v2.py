def validador_hamiltonian_completition(grafo, k, solucion): # O(V)
    if len(solucion) != len(grafo) + 1: # El +1 porque debe volver al 1er. vértice.
        return False
    
    if solucion[0] != solucion[-1]:
        return False
    
    visitados = set()
    aristas_extra = 0
    for i in range(len(solucion) - 1):
        v = solucion[i]

        if v in visitados:
            return False
        
        if not v in grafo or not solucion[i + 1] in grafo:
            return False
        
        if not grafo.estan_unidos(v, solucion[i + 1]):
            aristas_extra += 1

        if aristas_extra > k:
            return False

        visitados.add(v)
    
    return True