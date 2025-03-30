limite_animes = int(input())

quantidade_animes = int(input())

# Lista vazia que armazenará os nomes dos animes
lista_animes = []

quantidade_animes_lista = 0

for indice_anime in range(quantidade_animes):
    entrada = input()
    
    # Divide a entrada em três partes: nome do anime, quantidade de temporadas e quem indicou
    nome_anime, temporadas, indicacao = entrada.split(" - ")
    
    # Converte a quantidade de temporadas de string para inteiro
    temporadas = int(temporadas)
    
    adicionar = True  
    
    if quantidade_animes_lista >= limite_animes:
        adicionar = False
        print(f"A lista de animes está cheia. O {nome_anime} não foi adicionado.")
    
    if adicionar:
        if indicacao == "Walter" or (indicacao == "Internet" and temporadas <= 16):
            lista_animes.append(nome_anime) # Adiciona o anime à lista de animes aceitos
            quantidade_animes_lista += 1
            print(f"O {nome_anime} foi adicionado à lista de animes para assistir.")
        else:
            print(f"O {nome_anime} é muito longo, fica pra próxima.")

print(f"Lista final para assistir:{lista_animes}")