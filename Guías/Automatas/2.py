from automata import Automata

def automata_pares_1y0():
    a = Automata()

    # Estados:
    a.estado("Q0", es_inicial = True, es_final = True)
    a.estado("Q1")
    a.estado("Q2")
    a.estado("Q3")
    a.estado("Q4", es_final = True)

    # Transiciones:
    a.transicion_estado("Q0", "Q3", "1")
    a.transicion_estado("Q0", "Q2", "0")
    a.transicion_estado("Q1", "Q3", "0")
    a.transicion_estado("Q1", "Q2", "1")
    a.transicion_estado("Q2", "Q4", "0")
    a.transicion_estado("Q2", "Q1", "1")
    a.transicion_estado("Q3", "Q1", "0")
    a.transicion_estado("Q3", "Q4", "1")
    a.transicion_estado("Q4", "Q3", "1")
    a.transicion_estado("Q4", "Q2", "0")

    return a