"""Este código acabou ficando sem comentários, mas em algum momento eu os adiciono."""

pontuacoes_legado = {
    "Zumbi dos Palmares": 1000,
    "Frei Caneca": 900,
    "Paulo Freire": 800,
    "Clarice Lispector": 800,
    "Ariano Suassuna": 700,
    "Chico Science": 600,
    "Luiz Gonzaga": 500,
    "Eduardo Campos": 400,
    "Rivaldo": 300,
    "Lia de Itamaracá": 200
}

ordem_relevancia = {
    "Revolucionário": 1,
    "Líder comunitário": 2,
    "Cientista": 3,
    "Político": 4,
    "Escritor": 5,
    "Educador": 6,
    "Artista": 7,
    "Atleta": 8
}

def calcular_impacto(populacao, posicao):
    if posicao == 1:
        return populacao
    elif posicao == 2:
        return populacao // 2
    elif posicao == 3:
        return populacao // 3
    return 0

def desempatar(figura_1, figura_2, ramos):
    ramo_figura_1 = ramos[figura_1].strip()
    ramo_figura_2 = ramos[figura_2].strip()
    if ordem_relevancia[ramo_figura_1] < ordem_relevancia[ramo_figura_2]:
        return figura_1
    else:
        return figura_2

pontuacao_impacto = {}
for i in pontuacoes_legado:
    pontuacao_impacto[i] = 0

ramos_figuras = {}

n = int(input())

for i in range(n):
    bairro = input()
    populacao_bairro = int(input())
    for j in range(1, 4):
        figura_ramo = input().split(" - ")
        figura = figura_ramo[0]
        ramo = figura_ramo[1].strip()
        if figura not in ramos_figuras:
            ramos_figuras[figura] = ramo
        pontuacao_impacto[figura] += calcular_impacto(populacao_bairro, j)

pontuacao_total = {}
for i in pontuacoes_legado:
    pontuacao_total[i] = pontuacoes_legado[i] + pontuacao_impacto[i]

pontuacoes_figuras = []
for figura in pontuacao_total:
    pontuacoes_figuras.append((pontuacao_total[figura], figura))

n = len(pontuacoes_figuras)
for i in range(n):
    for j in range(i + 1, n):
        if pontuacoes_figuras[i][0] < pontuacoes_figuras[j][0]:
            pontuacoes_figuras[i], pontuacoes_figuras[j] = pontuacoes_figuras[j], pontuacoes_figuras[i]

ranking_pontuacoes_figuras = []
for tupla in pontuacoes_figuras:
    ranking_pontuacoes_figuras.append(tupla[1])

if pontuacao_total[ranking_pontuacoes_figuras[0]] == pontuacao_total[ranking_pontuacoes_figuras[1]]:
    figura_1 = ranking_pontuacoes_figuras[0]
    figura_2 = ranking_pontuacoes_figuras[1]
    print(f"Temos um empate entre {figura_1} e {figura_2}, vamos usar os critérios de desempate para ver quem fica com o prêmio.")
    vencedor = desempatar(figura_1, figura_2, ramos_figuras)
    print(f"Após utilizar os critérios de desempate, {vencedor} ficou com o prêmio.")
    if vencedor == figura_1:
        ranking_pontuacoes_figuras[0], ranking_pontuacoes_figuras[1] = figura_1, figura_2
    else:
        ranking_pontuacoes_figuras[0], ranking_pontuacoes_figuras[1] = figura_2, figura_1
else:
    vencedor = ranking_pontuacoes_figuras[0]

print(f"1º: {ranking_pontuacoes_figuras[0]} com {pontuacoes_legado[ranking_pontuacoes_figuras[0]]} pontos de legado, {pontuacao_impacto[ranking_pontuacoes_figuras[0]]} pontos de impacto e {pontuacao_total[ranking_pontuacoes_figuras[0]]} pontos totais")
print(f"2º: {ranking_pontuacoes_figuras[1]} com {pontuacoes_legado[ranking_pontuacoes_figuras[1]]} pontos de legado, {pontuacao_impacto[ranking_pontuacoes_figuras[1]]} pontos de impacto e {pontuacao_total[ranking_pontuacoes_figuras[1]]} pontos totais")