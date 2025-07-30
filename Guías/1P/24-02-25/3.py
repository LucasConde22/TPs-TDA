def es_valido(texto, palabras):
    if len(texto) == 0:
        return False

    validez = [True] + [False] * len(texto)

    for ini in range(len(texto)):
        for fin in range(1, len(texto) + 1):
            validez[fin] = True if (validez[fin]) or (texto[ini : fin] in palabras and validez[ini]) else False
        if validez[-1]:
            return True
    return False

def main():
    print(es_valido("argentinacampeon", {"argentina", "campeon"}))
    print(es_valido("awanteboke", {"aguante", "caca", "boca", "bolivia"}))
    print(es_valido("estanoche", {"es", "esta", "estan", "tano", "noche"}))
    print(es_valido("aguanteracing", {"aguante", "racing"}))
    print(es_valido("aguanteracing", {"racing"}))

if __name__ == "__main__":
    main()