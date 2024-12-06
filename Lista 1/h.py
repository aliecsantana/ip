nome_jogador = input()
quantidade_partidas = int(input())
quantidade_gols = int(input())
quantidade_assistencias = int(input())
quantidade_desarmes = int(input())
liga_jogador = input()

media_gols = quantidade_gols / quantidade_partidas
media_assistencias = quantidade_assistencias / quantidade_partidas
media_desarmes = quantidade_desarmes / quantidade_partidas

score = (quantidade_gols * 2) + (quantidade_assistencias * 1) + (quantidade_desarmes * 0.4)
   
# Verifica o critério 1 (se a liga é inválida)
if liga_jogador != 'Premier League' and liga_jogador != 'La Liga' and liga_jogador != 'Serie A' and liga_jogador != 'Brasileirão':
    print("A liga informada não é válida ou o jogador não pertence a nenhuma das ligas elegíveis para a premiação.")

# Se a liga é válida
else:
    # Verifica o critério 2 (média de gols insuficiente)
    if media_gols < 0.3:
        print("O jogador está fora, não possui a média de gols necessária.")
    else:
        # Verifica o critério 3 (média de assistências insuficiente)
        if media_assistencias < 0.15:
            print("Infelizmente não teve assistências o suficiente, portanto não concorre ao prêmio.") 
        else:
            # Verifica o critério 4 (média de desarmes insuficiente)
            if media_desarmes < 1.25:
                print(f"{nome_jogador} não desarmou jogadores o suficiente, portanto está fora.")
                
            else:
                # Verifica o critério 5 (número de partidas insuficiente)
                if quantidade_partidas < 50:
                    print("O atleta não jogou partidas o suficiente para concorrer à premiação.")
                # Se passou nos 5 critérios   
                else:
                    # Ajusta o score conforme a liga do jogador
                    if liga_jogador == 'Premier League':
                        score *= 1.0
                    elif liga_jogador == 'La Liga':
                        score *= 0.95
                    elif liga_jogador == 'Serie A':
                        score *= 0.9
                    elif liga_jogador == 'Brasileirão':
                        score *= 0.8
                        
                    # Se o score é alto
                    if score >= 80:
                        print(f"Promissor! {nome_jogador} é um potencial ganhador da Bola de Ouro!")
                    # Se o score é médio
                    elif 70 <= score < 80:
                        print(f"{nome_jogador} tem chances médias de ganhar o prêmio.")
                    # Se o score é baixo
                    else:
                        print(f"{nome_jogador} dificilmente ganhará a premiação, apesar de ser apto.")