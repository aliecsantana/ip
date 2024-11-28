nome_jogador1 = input()
pontuacao_jogador1 = int(input())
nome_jogador2 = input()
pontuacao_jogador2 = int(input())
nome_jogador3 = input()
pontuacao_jogador3 = int(input())

if nome_jogador1 == "Rodri":
    melhor_jogador = nome_jogador1
    pontuacao = pontuacao_jogador1
elif nome_jogador2 == "Rodri":
    melhor_jogador = nome_jogador2
    pontuacao = pontuacao_jogador2
elif nome_jogador3 == "Rodri":
    melhor_jogador = nome_jogador3
    pontuacao = pontuacao_jogador3
else:
    if pontuacao_jogador1 > pontuacao_jogador2 and pontuacao_jogador1 > pontuacao_jogador3:
        melhor_jogador = nome_jogador1
        pontuacao = pontuacao_jogador1
    elif pontuacao_jogador2 > pontuacao_jogador1 and pontuacao_jogador2 > pontuacao_jogador3:
        melhor_jogador = nome_jogador2
        pontuacao = pontuacao_jogador2
    else:
        melhor_jogador = nome_jogador3
        pontuacao = pontuacao_jogador3


print(f"O melhor jogador do mundo é {melhor_jogador}, com {pontuacao} ponto(s).")


if melhor_jogador == "Rodri":
    print("Os europeus, como sempre, roubaram o nosso ouro!")
elif melhor_jogador == "Vini Jr.":
    print("Os brasileiros amaram o resultado! BAILA VINI!")
else:
    print("Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!")