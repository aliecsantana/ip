# Cria uma lista para armazenar os nomes dos vilões
lista_viloes = []

entrada = ""

while entrada != "Já temos nossa lista de vilões":
    
    entrada = input()
    
    if entrada == "Novo vilão - Muito Perigoso":
        nome_vilao = input()
        lista_viloes.insert(0, nome_vilao) # Insere o vilão no início da lista
    
    elif entrada == "Novo vilão - Meio perigoso":
        nome_vilao = input()
        lista_viloes.append(nome_vilao) # Adiciona o vilão ao final da lista
    
    elif entrada == "O que ele está fazendo aqui?":
        nome_vilao = input()
        lista_viloes.remove(nome_vilao) # Remove o vilão da lista
    
    elif entrada == "Vilão mais perigoso do que pensávamos":
        indice_atual = int(input())
        novo_indice = int(input())
        lista_viloes[indice_atual], lista_viloes[novo_indice] = lista_viloes[novo_indice], lista_viloes[indice_atual] # Troca as posições dos vilões de acordo com o as entradas de "indice_atual" e "novo_indice"
    
    elif entrada == "Que estranho, esses dois vilões… troque-os de lugar":
        nome_1 = input()
        nome_2 = input()
        # Encontra os índices dos vilões na lista
        idx_1 = lista_viloes.index(nome_1)  
        idx_2 = lista_viloes.index(nome_2)
        lista_viloes[idx_1], lista_viloes[idx_2] = lista_viloes[idx_2], lista_viloes[idx_1] # Troca as posições dos vilões
    
    elif entrada == "Essa posição não está de acordo, ele nem odeia carecas":
        nome_vilao = input()
        lista_viloes.remove(nome_vilao) # Remove o vilão da lista
        lista_viloes.append(nome_vilao) # Adiciona o vilão ao final da lista
    
    elif entrada == "Como a lista está ficando?":
        print(", ".join(lista_viloes)) # Imprime os vilões da lista, separados por vírgula e espaço

if entrada == "Já temos nossa lista de vilões":
    print("O resultado final ficou assim:")
    print(", ".join(lista_viloes)) # Imprime todos os vilões da lista, separados por vírgula e espaço