import copy

def negacion(c):
    if len(c) == 1:
        x = "~" + c
    else:
        x = c[-1]
    return x


def unitPropagate(S, I):

    bool = True

    while bool:
        for k in S:
            if len(k) == 0:
                #return "Insatisfacible", {}
                break

        contador = 0

        for i in S:
            if len(i) == 1:
                contador += 1
                liter = i[0]
                if len(liter) == 1:
                    pp = liter
                    comple = "~" + liter
                    valor = 1

                elif(len(liter) == 2):
                    pp = liter[1]
                    comple = liter[1]
                    valor = 0

                for j in S:
                    if j != i:
                        if liter in j:
                            S.remove(j)
                I[pp] = valor
                S.remove(i)
                #print(i)


        if contador == 0:
            bool = False
        else:
            for k in S:
                if comple in k:
                    k.remove(comple)
    return S, I

def DPLL(s, i):

    vacio = []

    s, i = unitPropagate(s,i)

    if void in s:
        return "Insatisfacible", {}

    elif len(s) == 0:
        return "Satisfacible", i

    lit = ""

    for y in s:
        for x in y:
            if x not in i.keys():
                lit = x

    lit_comp = negacion(lit)

    if lit == "":
        return None

    Sp = copy.deepcopy(s)

    Sp = [n for n in Sp if lit not in n]

    for q in Sp:
        if lit_comp in q:
            q.remove(negacion(lit))

    Ip = copy.deepcopy(i)

    if lit[0] == "-":
        Ip[lit[1]] = 0

    else:
        Ip[lit] = 1

    S1, I1 = DPLL(Sp, Ip)

    if S1 == "Satisfacible":
        return S1, I1

    else:
        Spp = copy.deepcopy(s)
        Spp = [q for q in Spp if negacion(lit) not in q]
        for h in Spp:
            if lit in h:
                h.remove(lit)
        Ipp = copy.deepcopy(i)
        if lit[0] == "-":
            Ipp[lit[1]] = 0
        else:
            Ipp[lit] = 1
        return DPLL(Spp, Ipp)
