# Função para descriptografar a fórmula
def descriptografar_formula(texto, deslocamento):
    resultado = ""
    for i in texto:
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        indice = 0
        while indice < 26:
            if alfabeto[indice] == i: # Se o caractere atual for encontrado no alfabeto
                nova_posicao = indice - deslocamento
                while nova_posicao < 0:
                    nova_posicao += 26
                resultado += alfabeto[nova_posicao] # Adiciona o caractere descriptografado ao resultado
            indice += 1
    return resultado # Retorna o texto descriptografado

# Função para calcular o dano
def calcular_dano(precisao, resistencia, poder, fator):
    return round(precisao * (poder / resistencia) * fator) # Calcula e retorna o dano arredondado

# Função para ordenar os ataques
def ordenar_ataques(nomes, danos):
    for i in range(len(nomes)):
        for j in range(len(nomes) - 1):
            if danos[j] < danos[j + 1]:
                nome_temporario = nomes[j]
                dano_temporario = danos[j]
                nomes[j] = nomes[j + 1]
                danos[j] = danos[j + 1]
                nomes[j + 1] = nome_temporario
                danos[j + 1] = dano_temporario

n_ataques = int(input())

if n_ataques == 0:
    print("Piltover em paz... por enquanto.")
else:
    nomes_alvos = []
    danos_ataques = []

    for i in range(n_ataques):
        entrada = input().split(", ")
        nome = entrada[0]
        precisao = int(entrada[1])
        resistencia = int(entrada[2])
        poder = int(entrada[3])
        formula = entrada[4]
        deslocamento = int(entrada[5])

        formula_decifrada = descriptografar_formula(formula, deslocamento) # Descriptografa a fórmula
        print(f"Decifrando: {formula_decifrada}")

        fator = 1
        if formula_decifrada == "ALTO":
            fator = 2
        elif formula_decifrada == "MEDIO":
            fator = 1.5

        dano = calcular_dano(precisao, resistencia, poder, fator) # Calcula o dano
        print(f"{nome}: {dano} de dano calculado.")

        if dano >= 100:
            print(f"{nome} será destruído!")
            print()
        else:
            print(f"{nome} resistirá ao ataque.")
            print()

        nomes_alvos.append(nome)
        danos_ataques.append(dano)

    ordenar_ataques(nomes_alvos, danos_ataques) # Ordena os ataques pela lista de danos
    print("Prioridade de ataques:")
    for i in range(len(nomes_alvos)):
        print(f"{nomes_alvos[i]} - {danos_ataques[i]} de dano")