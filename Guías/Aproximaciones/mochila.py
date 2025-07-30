def mochila_aproximada(elementos, W, epsilon):
    v_max = buscar_valor_maximo(elementos)
    b = (epsilon * v_max) / (2 * len(elementos))

    