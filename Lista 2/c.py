velocidade_renas = 80
tempo_total = 0
quantidade_presentes = 0

print("Boa noite, Papai Noel! Feliz Natal!")

# Loop para processar as entregas de presentes
entrada = ""
while entrada != "Já está amanhecendo, preciso voltar ao Polo Norte! HO HO HO!":
    entrada = input()
    if entrada == "Já está amanhecendo, preciso voltar ao Polo Norte! HO HO HO!":
        print(f"Querido Papai Noel, a noite de natal foi um sucesso! Você levou apenas {tempo_total:.2f} horas para entregar todos os {quantidade_presentes} presentes")
    elif entrada == "As renas ainda estão cheias de energia para entregar presentes para mais crianças!":
        crianca = input()
        distancia = float(input())
        unidade_medida_distancia = input()

        # Converte a distância de metros para quilômetros
        if unidade_medida_distancia == "metros":
            distancia = distancia / 1000

        # Calcula o tempo necessário para chegar até a casa da criança
        tempo = distancia / velocidade_renas
        tempo_total += tempo
        quantidade_presentes += 1

        # Determina a mensagem a ser exibida com base no tempo de viagem
        if tempo >= 1:
            print(f"Querido Papai Noel, você levará {int(tempo)} horas para chegar até a casa de {crianca}!")
        elif tempo >= 1 / 60:
            print(f"Querido Papai Noel, você levará {int(tempo * 60)} minutos para chegar até a casa de {crianca}!")
        else:
            print(f"Querido Papai Noel, você chegará em breve na casa de {crianca}!")