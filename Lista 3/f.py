quantidade_feiticeiros = int(input())

# Lista para armazenar os nomes dos feiticeiros e seus níveis de energia amaldiçoada
feiticeiros = []

for indice_feiticeiro in range(quantidade_feiticeiros):
    nome = input()
    nivel = int(input())
    feiticeiros.append([nome, nivel]) # Adiciona os dados à lista que armazena os nomes e níveis de energia dos feiticeiros

rodada = 1

while len(feiticeiros) > 1:
    print(f"\n--- Rodada {rodada} ---")
    
    # Lista para armazenar os feiticeiros classificados para a próxima rodada
    classificados = []
    
    indice_duelo = 0

    while indice_duelo < len(feiticeiros):
        if indice_duelo + 1 < len(feiticeiros):
            feiticeiro_1 = feiticeiros[indice_duelo] # Encontra o primeiro participante do duelo
            feiticeiro_2 = feiticeiros[indice_duelo + 1] # Encontra o segundo participante do duelo
            print(f"Confronto: {feiticeiro_1[0]} vs {feiticeiro_2[0]}") # Exibe os participantes do duelo
            
            if feiticeiro_1[1] >= feiticeiro_2[1]: # Compara os níveis de energia amaldiçoada
                print(f"{feiticeiro_1[0]} vence!") # Anuncia o vencedor
                classificados.append(feiticeiro_1) # Adiciona o vencedor à lista de classificados para a próxima rodada
            else:
                print(f"{feiticeiro_2[0]} vence!") # Anuncia o vencedor
                classificados.append(feiticeiro_2) # Adiciona o vencedor à lista de classificados para a próxima rodada
            
            indice_duelo += 2
        else:
            print(f"{feiticeiros[indice_duelo][0]} avança automaticamente!") # Exibe a mensagem de avanço
            classificados.append(feiticeiros[indice_duelo]) # Adiciona o feiticeiro à lista de classificados para a próxima rodada
            indice_duelo += 1

    feiticeiros = classificados
    rodada += 1

campeao = feiticeiros[0] # O único feiticeiro restante é o campeão
print(f"\nO campeão do torneio é {campeao[0]} com nível de energia amaldiçoada {campeao[1]}!") # Exibe o campeão

if campeao[0] == "Itadori": # Se o campeão é Itadori
    if campeao[1] > 90: # Se o nível de energia amaldiçoada for superior a 90
        print("\n### Nas sombras da alma de Itadori, Sukuna desperta e toma o controle! ###")
        print("Uma aura de destruição toma conta, não há escapatória.")
        print("Com um riso diabólico, ele manifesta sua Expansão de Domínio: Fukuma Mizushi!")
    else:
        print("\nItadori vence com honra e bravura!")