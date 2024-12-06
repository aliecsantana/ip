nome_jogador1 = input()
quantidade_gols_jogador1 = int(input())
quantidade_partidas_jogador1 = int(input())
velocidade_maxima_jogador1 = float(input())

nome_jogador2 = input()
quantidade_gols_jogador2 = int(input())
quantidade_partidas_jogador2 = int(input())
velocidade_maxima_jogador2 = float(input())

nome_jogador3 = input()
quantidade_gols_jogador3 = int(input())
quantidade_partidas_jogador3 = int(input())
velocidade_maxima_jogador3 = float(input())

pontuacao1 = ((quantidade_gols_jogador1 * 5) + (quantidade_partidas_jogador1 * 2) + (velocidade_maxima_jogador1 * 3)) / 10 + (len(nome_jogador1) % 3)
pontuacao2 = ((quantidade_gols_jogador2 * 5) + (quantidade_partidas_jogador2 * 2) + (velocidade_maxima_jogador2 * 3)) / 10 + (len(nome_jogador2) % 3)
pontuacao3 = ((quantidade_gols_jogador3 * 5) + (quantidade_partidas_jogador3 * 2) + (velocidade_maxima_jogador3 * 3)) / 10 + (len(nome_jogador3) % 3)

# Verifica se o jogador 1 tem a maior pontuação
if pontuacao1 > pontuacao2 and pontuacao1 > pontuacao3:
    nome_1lugar = nome_jogador1
    pontuacao_1lugar = pontuacao1
    # Se o jogador 1 é o 1º colocado, verifica quem é o 2º
    if pontuacao2 > pontuacao3:
        nome_2lugar = nome_jogador2
        pontuacao_2lugar = pontuacao2
        nome_3lugar = nome_jogador3
        pontuacao_3lugar = pontuacao3
    else:
        nome_2lugar = nome_jogador3
        pontuacao_2lugar = pontuacao3
        nome_3lugar = nome_jogador2
        pontuacao_3lugar = pontuacao2

# Verifica se o jogador 2 tem a maior pontuação
elif pontuacao2 > pontuacao1 and pontuacao2 > pontuacao3:
    nome_1lugar = nome_jogador2
    pontuacao_1lugar = pontuacao2
    # Se o jogador 2 é o 1º colocado, verifica quem é o 2º
    if pontuacao1 > pontuacao3:
        nome_2lugar = nome_jogador1
        pontuacao_2lugar = pontuacao1
        nome_3lugar = nome_jogador3
        pontuacao_3lugar = pontuacao3
    else:
        nome_2lugar = nome_jogador3
        pontuacao_2lugar = pontuacao3
        nome_3lugar = nome_jogador1
        pontuacao_3lugar = pontuacao1

# Se nem o jogador 1 nem o jogador 2 têm a maior pontuação, o jogador 3 é 1º colocado
else:
    nome_1lugar = nome_jogador3
    pontuacao_1lugar = pontuacao3
    # Se o jogador 3 é o 1º, verifica quem é o 2º
    if pontuacao1 > pontuacao2:
        nome_2lugar = nome_jogador1
        pontuacao_2lugar = pontuacao1
        nome_3lugar = nome_jogador2
        pontuacao_3lugar = pontuacao2
    else:
        nome_2lugar = nome_jogador2
        pontuacao_2lugar = pontuacao2
        nome_3lugar = nome_jogador1
        pontuacao_3lugar = pontuacao1

print(f"1 - {nome_1lugar} obteve {pontuacao_1lugar:.2f} pontos.")
print(f"2 - {nome_2lugar} obteve {pontuacao_2lugar:.2f} pontos.")
print(f"3 - {nome_3lugar} obteve {pontuacao_3lugar:.2f} pontos.")

print(f"{nome_1lugar} é o verdadeiro ganhador da Bola de Ouro com um total de {pontuacao_1lugar:.2f} pontos.")