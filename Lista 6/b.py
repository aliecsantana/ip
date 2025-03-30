def calcular_pontuacao(aprovacao, orcamento, categoria):
    pontos = 0

    if aprovacao == "APROVA":
        pontos += 5
    elif aprovacao == "TANTO FAZ":
        pontos += 2
    elif aprovacao == "DESAPROVA":
        pontos += 0

    if orcamento > 1000000:
        pontos += 3
    elif 500000 <= orcamento <= 1000000:
        pontos += 4
    elif orcamento < 500000:
        pontos += 5

    if categoria == "Defesa":
        pontos += 5
    elif categoria == "Ciencia":
        pontos += 4
    elif categoria == "Lazer":
        pontos += 3
    elif categoria != "Defesa" and categoria != "Ciencia" and categoria != "Lazer":
        pontos += 0
    
    return pontos

def ordenar_estabelecimentos(estabelecimentos):
    n = len(estabelecimentos)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Verifica se a pontuação do estabelecimento na posição "j" é menor que a do estabelecimento na posição "j + 1"
            if estabelecimentos[j]['pontuacao'] < estabelecimentos[j + 1]['pontuacao']:
                estabelecimentos[j], estabelecimentos[j + 1] = estabelecimentos[j + 1], estabelecimentos[j] # Troca os estabelecimentos de posição, colocando o de maior pontuação à frente
            # Se a pontuação do estabelecimento na posição "j" for igual à do estabelecimento na posição "j + 1"
            elif estabelecimentos[j]['pontuacao'] == estabelecimentos[j + 1]['pontuacao']:
            # Verifica se o orçamento do estabelecimento na posição "j" é maior que o do estabelecimento na posição "j + 1"
                if estabelecimentos[j]['orcamento'] > estabelecimentos[j + 1]['orcamento']:
                    estabelecimentos[j], estabelecimentos[j + 1] = estabelecimentos[j + 1], estabelecimentos[j] # Troca os estabelecimentos de posição, colocando o de menor orçamento à frente

def determinar_ordem_construcao():
    estabelecimentos = []

    for i in range(3):
        nome_estabelecimento = input()
        aprovacao = input()
        orcamento = int(input())
        categoria = input()

        pontuacao = calcular_pontuacao(aprovacao, orcamento, categoria)

        # Cria um dicionário com os dados do estabelecimento
        estabelecimento = {'nome': nome_estabelecimento, 'aprovacao': aprovacao, 'orcamento': orcamento, 'categoria': categoria, 'pontuacao': pontuacao}

        estabelecimentos.append(estabelecimento)

    ordenar_estabelecimentos(estabelecimentos)

    print()
    print(f"O primeiro estabelecimento construído deve ser {estabelecimentos[0]['nome']}, com um orçamento de {estabelecimentos[0]['orcamento']} e com a funcionalidade de {estabelecimentos[0]['categoria']}.") # Exibe o primeiro dicionário da lista "estabelecimentos", acessando as chaves 'nome', 'orcamento' e 'categoria'
    print(f"O segundo estabelecimento construído deve ser {estabelecimentos[1]['nome']}, com um orçamento de {estabelecimentos[1]['orcamento']} e com a funcionalidade de {estabelecimentos[1]['categoria']}.") # Exibe o segundo dicionário da lista "estabelecimentos", acessando as chaves 'nome', 'orcamento' e 'categoria'
    print(f"O terceiro estabelecimento construído deve ser {estabelecimentos[2]['nome']}, com um orçamento de {estabelecimentos[2]['orcamento']} e com a funcionalidade de {estabelecimentos[2]['categoria']}.") # Exibe o terceiro dicionário da lista "estabelecimentos", acessando as chaves 'nome', 'orcamento' e 'categoria'

    # Itera sobre cada dicionário na lista "estabelecimentos"
    for estabelecimento in estabelecimentos:
        if estabelecimento['categoria'] == "Defesa":
            print("Oba, agora a cidade estará mais segura.")
        elif estabelecimento['categoria'] == "Ciencia":
            print("Agora sim vou poder ter uma vida intelectual.")
        elif estabelecimento['categoria'] == "Lazer":
            print("Vamooo, agora posso curtir meu final de semana descansando na bela cidade do Recife.")

determinar_ordem_construcao()