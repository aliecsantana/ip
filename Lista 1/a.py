nome_jogador1 = input() 
pontuacao1 = int(input())

nome_jogador2 = input()
pontuacao2 = int(input())

nome_jogador3 = input()
pontuacao3 = int(input())

# Verifica se algum jogador é Lucas Lima
if nome_jogador1 == 'Lucas Lima' or nome_jogador2 == 'Lucas Lima' or nome_jogador3 == 'Lucas Lima':
    print('Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!')
# Determina o jogador com maior pontuação
else:
    if pontuacao1 > pontuacao2 and pontuacao1 > pontuacao3:
        ganhador_final = nome_jogador1
    elif pontuacao2 > pontuacao1 and pontuacao2 > pontuacao3:
        ganhador_final = nome_jogador2
    else:
        ganhador_final = nome_jogador3
    print(f'{ganhador_final} é eleito o bola de ouro!')