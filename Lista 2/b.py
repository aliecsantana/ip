playlist = ""
tentativas_viloes = 0
ultima_musica = ""
qtd_musicas = 0

print("PLAYLIST DO PAPAI NOEL")

while True:
    musica = input()
    # Verifica se a entrada é "FIM"
    if musica == "FIM":
        if qtd_musicas > 0:
            print(f"Ufa! Conseguimos criar a playlist perfeita, tomara que o Papai Noel goste das {qtd_musicas} músicas.")
        else:
            print("Infelizmente não conseguimos encontrar nenhuma música para a playlist do Papai Noel...")
        break
    # Verifica se a música é composta apenas por números
    if musica.isnumeric():
        tentativas_viloes += 1
        if tentativas_viloes == 3:
            print("NAAÃO! Já está na hora do Papai Noel sair e não conseguimos construir sua playlist perfeita.")
            break
        else:
            print("ABORTAR! OS VILÕES OBTIVERAM ACESSO, TEREMOS QUE RECOMEÇAR.")
            print("PLAYLIST DO PAPAI NOEL")
            playlist = ""
            ultima_musica = ""
            qtd_musicas = 0
        continue
    # Verifica se a música é composta apenas por letras e espaços e tem pelo menos 15 caracteres
    if len(musica.replace(" ", "")) >= 15 and all(caracter.isalpha() or caracter.isspace() for caracter in musica):
        print(f"{musica} foi adicionada à playlist!")
        playlist += musica + "\n"
        ultima_musica = musica
        qtd_musicas += 1
    else:
        if qtd_musicas > 0:
            print(f"{musica} não pôde ser adicionada à playlist! A última música adicionada foi {ultima_musica}.")
        else:
            print(f"{musica} não pôde ser adicionada e a playlist continua vazia. Papai Noel precisa da sua ajuda!")