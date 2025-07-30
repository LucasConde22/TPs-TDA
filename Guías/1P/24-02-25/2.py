from copy import deepcopy

# Adicionalmente se puede usar el algoritmo Greedy del punto anterior como recorte.
def maximizar_proyectos(proyectos, k):
    equipos = []
    for i in range(k):
        equipos.append([])
    proyectos = sorted(proyectos, key= lambda x: x[0]) # Para que buscar compatibilidades sea menos cortoso.
    _, asignaciones = asignar_equipos(0, proyectos, equipos, 0, None, 0)
    return asignaciones
    

def asignar_equipos(i, proyectos, equipos, asignados, mejor_sol, max_asignados):
    if i == len(proyectos):
        return asignados, deepcopy(equipos)

    for equipo in equipos:
        if _es_compatible(proyectos[i], equipo): # Si no es compatible, no lo asigno.
            equipo.append(proyectos[i])
            nueva_cant, nueva_sol = asignar_equipos(i + 1, proyectos, equipos, asignados + 1, mejor_sol, max_asignados)
            if nueva_cant > max_asignados:
                max_asignados, mejor_sol = nueva_cant, nueva_sol
            equipo.pop()
    
    nueva_cant, nueva_sol = asignar_equipos(i + 1, proyectos, equipos, asignados, mejor_sol, max_asignados)
    if nueva_cant > max_asignados:
        max_asignados, mejor_sol = nueva_cant, nueva_sol
    
    return max_asignados, mejor_sol
    
def _es_compatible(proyecto, equipo):
    if not equipo:
        return True
    return equipo[-1][1] <= proyecto[0]

def main():
    print(maximizar_proyectos([], 2))
    print(maximizar_proyectos([(0, 6), (3, 4), (4, 5), (2, 6)], 2))
    print(maximizar_proyectos([(0, 1), (0, 2), (2, 3), (3, 4), (1, 5)], 2))

if __name__ == "__main__":
    main()
