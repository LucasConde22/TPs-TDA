import pulp

def juan_el_vago(m):
    d = [pulp.LpVariable(f"d{i}", cat ="Binary") for i in range(len(m))]
    
    problema = pulp.LpProblem("días a trabajar", pulp.LpMaximize)
    problema += pulp.lpSum([d[i] * m[i] for i in range(len(m))])
    for i in range(len(m) - 1):
        problema += d[i] + d[i + 1] <= 1

    problema.solve()
    return [m[i] for i in range(len(m)) if pulp.value(d[i]) == 1]

def main():
    print(juan_el_vago([100, 5, 50, 1, 1, 200]))

if __name__ == "__main__":
    main()
