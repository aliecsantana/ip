n_rodadas = int(input())

meias_duendes = 0
meias_elfos = 0
desafios_dificeis_duendes = 0
desafios_dificeis_elfos = 0

print("O Torneio de Natal começa agora! Que vençam os melhores!")

# Loop para processar cada rodada do torneio
rodada = 1
while rodada <= n_rodadas:
    print(f"RODADA {rodada}")

    equipe = input()
    desafio = input()
    dificuldade = input()

    # Inicializa a quantidade de meias a serem atribuídas na rodada
    meias_por_rodada = 0

    # Modifica a quantidade de meias de acordo com o desafio
    if desafio == "Prepararam as roupas do Papai Noel." or desafio == "Alimentaram as renas.":
        meias_por_rodada += 10
    elif desafio == "Arrumaram os estoques de doces." or desafio == "Guardaram os presentes no trenó.":
        meias_por_rodada += 20
    elif desafio == "Ajudaram a carregar os presentes." or desafio == "Embrulharam os presentes." or desafio == "Decoraram a árvore de Natal.":
        meias_por_rodada += 30
    elif desafio == "Planejaram a rota do Papai Noel.":
        meias_por_rodada += 50
    elif desafio == "Testaram os brinquedos.":
        qtd_brinquedos = int(input())
        meias_por_rodada += 2 * qtd_brinquedos

    # Modifica a quantidade de meias de acordo com a dificuldade do desafio
    if dificuldade == "Médio":
        meias_por_rodada = int(meias_por_rodada * 1.2)
    elif dificuldade == "Difícil":
        meias_por_rodada = int(meias_por_rodada * 1.5)
        # Conta o número de desafios difíceis completados por cada equipe
        if equipe == "Duendes":
            desafios_dificeis_duendes += 1
        elif equipe == "Elfos":
            desafios_dificeis_elfos += 1

    # Modifica a quantidade de meias de acordo com o evento surpresa
    evento_surpresa = input()
    if evento_surpresa == "Dia de Sorte":
        print("É um Dia de Sorte! Vocês ganharam 30 meias bônus!")
        meias_por_rodada += 30
    elif evento_surpresa == "Dia de Azar":
        print("É um Dia de Azar! Vocês perderam 30 meias!")
        meias_por_rodada -= 30
        if meias_por_rodada < 0:
            meias_por_rodada = 0
    elif evento_surpresa == "Grinch":
        print("O Grinch está sabotando o Torneio!")
        cor_meia = input()
        # Loop para definir quantas meias serão roubadas pelo Grinch
        while cor_meia != f"{equipe}, protejam as meias!":
            if cor_meia == "Amarelas":
                meias_por_rodada -= 5
            elif cor_meia == "Verdes":
                meias_por_rodada -= 10
            elif cor_meia == "Vermelhas":
                meias_por_rodada -= 20
            if meias_por_rodada < 0:
                meias_por_rodada = 0
            cor_meia = input()

    # Atualiza a total de meias de cada equipe
    if equipe == "Duendes":
        meias_duendes += meias_por_rodada
    elif equipe == "Elfos":
        meias_elfos += meias_por_rodada

    # Exibe a quantidade de meias que a equipe ganhou ou se não ganhou meias na rodada
    if meias_por_rodada > 0:
        print(f"A equipe dos {equipe} ganhou {meias_por_rodada} meias nesta rodada.")
    else:
        print(f"Infelizmente, a equipe dos {equipe} não ganhou meias nessa rodada.")

    # Avança para a próxima rodada
    rodada += 1

print("TORNEIO ENCERRADO!")
print("Segurem seus gorros que o Noel já vai entregar o Prêmio da Estrela Natalina.")

# Determina a equipe vencedora com base no total de meias e no número de desafios difíceis
if meias_duendes > meias_elfos or (meias_duendes == meias_elfos and desafios_dificeis_duendes > desafios_dificeis_elfos):
    print(f"Os Duendes venceram o Torneio de Natal com um total de {meias_duendes} meias e terão a honra de ajudar o Papai Noel na noite mais mágica do ano.")
elif meias_elfos > meias_duendes or (meias_elfos == meias_duendes and desafios_dificeis_elfos > desafios_dificeis_duendes):
    print(f"Os Elfos venceram o Torneio de Natal com um total de {meias_elfos} meias e terão a honra de ajudar o Papai Noel na noite mais mágica do ano.")