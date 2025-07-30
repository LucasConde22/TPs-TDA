from compatibles import *

def obtener_combinaciones(materias):
    combinaciones = []
    _combinar_materias(0, materias, [], combinaciones)
    return combinaciones

def _combinar_materias(i, materias, seleccionadas, combinaciones):
    if i == len(materias):
        combinaciones.append(seleccionadas[:])
        return

    for curso in materias[i]:
        if _es_compatible(curso, seleccionadas):
            seleccionadas.append(curso)
            _combinar_materias(i + 1, materias, seleccionadas, combinaciones)
            seleccionadas.pop()

def _es_compatible(curso, seleccionadas):
    for seleccionada in seleccionadas:
        if not son_compatibles(curso, seleccionada):
            return False
    return True