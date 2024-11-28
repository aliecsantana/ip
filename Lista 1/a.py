nome_jogador1 = input() 
pontuação1 = int(input())

nome_jogador2 = input()
pontuação2 = int(input())

nome_jogador3 = input()
pontuação3 = int(input())

if nome_jogador1 == 'Lucas Lima' or nome_jogador2 == 'Lucas Lima' or nome_jogador3 == 'Lucas Lima':
    print('Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!')
else:
    if pontuação1 > pontuação2 and pontuação1 > pontuação3:
        ganhador_final = nome_jogador1
    elif pontuação2 > pontuação1 and pontuação2 > pontuação3:
        ganhador_final = nome_jogador2
    else:
        ganhador_final = nome_jogador3
    print(f'{ganhador_final} é eleito o bola de ouro!')
