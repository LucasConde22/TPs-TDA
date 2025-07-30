from grafo import Grafo
from algoritmos import *

# O(V*E^2)
def asignar_turnos(turnos, medicos): # turnos = [(especialidad, [horarios])], medicos = [(especialidad, [horarios])]
    f, s = 'fuente', 'sumidero'
    red = Grafo(True, [f, s])

    for i, (especialidad, horarios) in enumerate(turnos):
        p = f'p{i}'
        red.agregar_vertice(p)
        red.agregar_arista(f, p)

        for horario in horarios:
            t = f'{especialidad},{horario}'
            if not red.hay_vertice(t):
                red.agregar_vertice(t)
            red.agregar_arista(p, t, 1)

    for i, (especialidad, horarios) in enumerate(medicos):
        m = f'm{i}'
        red.agregar_vertice(m)
        red.agregar_arista(m, s, len(horarios))

        for horario in horarios:
            t = f'{especialidad},{horario}'
            if not red.hay_vertice(t):
                continue # Si nadie solicitó un turno en ese horario y para esa especialidad, no es necesario crearlo.
            red.agregar_arista(t, m, 1)
    
    flujo_max = flujo(red, f, s)
    flujo_total = 0
    for paciente in red.adyacentes(f):
        flujo_total += flujo_max[(f, paciente)]
    return flujo_total

def main():
    turnos = [("A", ["14", "15"]), ("A", ["14", "16"]), ("A", ["15"]), ("B", ["13"]), ("A", ["16"])]
    medicos = [("A", ["14"]), ("A", ["15", "16"]), ("B", ["13", "14"])]
    print("Turnos asignados: ", asignar_turnos(turnos, medicos))

if __name__ == "__main__":
    main()
