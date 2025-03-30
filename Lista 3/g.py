# Lista de animes favoritos de César
animes_favoritos = [
    'Fullmetal Alchemist: Brotherhood',
    'Attack On Titan',
    'Death Note',
    'Naruto',
    'One Piece',
    'Demon Slayer',
    'Dragon Ball Z',
    'Jujutsu Kaisen',
    'Pokemon',
    'Bleach'
]

quantidade_amigos = int(input())
print(f"{quantidade_amigos} amigos participaram da votação!")

nomes_animes = animes_favoritos.copy() # Cria uma cópia da lista de animes favoritos de César para manipulação sem alterar a lista original
pontuacoes_animes = [0] * len(animes_favoritos) # Inicializa a pontuação de cada anime com zero

for contador_amigos in range(quantidade_amigos):
    nome_amigo = input()
    print(f"{nome_amigo} é a {contador_amigos + 1}ª pessoa à votar!")
    
    # Lista para armazenar os votos de um amigo específico
    votos_pessoais = []
    # Sistema de pontuação para 1º, 2º e 3º lugar
    pontos = [3, 2, 1]
    
    for posicao_ranking in range(3):
        anime_votado = input().title() # Recebe o nome do anime e ajusta a capitalização
        
        while anime_votado in votos_pessoais:
            print(f"{nome_amigo}, você já votou neste anime! Escolha um outro anime para ocupar a sua {posicao_ranking + 1}º posição!")
            anime_votado = input().title() # Recebe o nome do anime e ajusta a capitalização
        
        while anime_votado not in animes_favoritos:
            print(f"O anime {anime_votado} não está presente na votação!")
            anime_votado = input().title() # Recebe o nome do anime e ajusta a capitalização

        print(f"{nome_amigo} colocou {anime_votado} em {posicao_ranking + 1}º lugar do seu ranking!")
        
        votos_pessoais.append(anime_votado) # Adiciona o anime à lista de votos pessoais do amigo
        indice_anime = nomes_animes.index(anime_votado) # Encontra o índice do anime na lista de nomes de animes
        pontuacoes_animes[indice_anime] += pontos[posicao_ranking] # Adiciona a pontuação ao anime

pontuacao_maxima = max(pontuacoes_animes) # Calcula a pontuação máxima
indice_vencedor = pontuacoes_animes.index(pontuacao_maxima) # Identifica o índice do anime vencedor
anime_vencedor = nomes_animes[indice_vencedor] # Identifica o nome do anime vencedor

print(f"Com {pontuacao_maxima} pontos, {anime_vencedor} foi votado como o melhor anime!")

if anime_vencedor == "Pokemon":
    print("César - Pokémon é o melhor anime da história!!!")

print("Eita mandaram dúvida no discord, vou lá responder!")