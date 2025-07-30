from automata import Automata

def expresion():
    a = Automata()

    # Estados:
    a.estado("Q0", es_inicial = True, es_final = True)
    a.estado("Q1")
    a.estado("Q2", es_final = True)
    a.estado("Q3")
    a.estado("Q4", es_final = True)
    a.estado("Q5", es_final = True)
    a.estado("Q6")

    # Transiciones:
    a.transicion_estado("Q0", "Q1", "a")
    a.transicion_estado("Q0", "Q5", "b")
    a.transicion_estado("Q0", "Q6", "a")

    a.transicion_estado("Q1", "Q2", "b")

    a.transicion_estado("Q2", "Q3", "b")
    a.transicion_estado("Q2", "Q1", "a")
    a.transicion_estado("Q2", "Q5", "b")

    a.transicion_estado("Q3", "Q4", "a")

    a.transicion_estado("Q4", "Q5", "b")
    a.transicion_estado("Q4", "Q3", "b")
    a.transicion_estado("Q4", "Q6", "a")
    a.transicion_estado("Q4", "Q4", "a")

    a.transicion_estado("Q5", "Q5", "b")
    a.transicion_estado("Q5", "Q6", "a")

    a.transicion_estado("Q6", "Q5", "b")

    return a