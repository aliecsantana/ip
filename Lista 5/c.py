def derivada_termo(termo):
    if "x" not in termo:
        return "0"
    elif "^" in termo:
        coeficiente, expoente = termo.split("x^")
    else:
        coeficiente, expoente = termo.split("x")
        expoente = "1"

    if coeficiente == "" or coeficiente == "+":
        coeficiente = "1"
    elif coeficiente == "-":
        coeficiente = "-1"

    coeficiente = int(coeficiente)
    expoente = int(expoente)

    if expoente == 0:
        return "0"

    novo_coeficiente = coeficiente * expoente
    novo_expoente = expoente - 1

    if novo_expoente == 0:
        return str(novo_coeficiente)
    elif novo_expoente == 1:
        return f"{novo_coeficiente}x"
    else:
        return f"{novo_coeficiente}x^{novo_expoente}"

def derivada_polinomio(polinomio):
    termos = []
    termo_atual = ""

    for i in range(len(polinomio)):
        if (polinomio[i] == "+" or polinomio[i] == "-") and i > 0:
            termos.append(termo_atual)
            termo_atual = polinomio[i]
        else:
            termo_atual += polinomio[i]

    termos.append(termo_atual)

    derivada = ""

    for j in termos:
        derivada_termo_calculado = derivada_termo(j)
        if derivada_termo_calculado != "0":
            if derivada == "":
                derivada = derivada_termo_calculado
            else:
                if derivada_termo_calculado[0] == "-":
                    derivada += derivada_termo_calculado
                else:
                    derivada += "+" + derivada_termo_calculado

    if derivada == "":
        return "0"
    else:
        return derivada

def derivada_ordem_n(polinomio, k):
    if k == 0:
        return polinomio
    elif polinomio == "0":
        return "0"
    else:
        return derivada_ordem_n(derivada_polinomio(polinomio), k - 1) # Chama recursivamente a função para calcular a derivada de ordem 'k-1'

polinomio = input().strip()
k = int(input().strip())

resultado = derivada_ordem_n(polinomio, k)

print(f"A derivada de ordem {k} da função {polinomio} é:")
print(resultado)