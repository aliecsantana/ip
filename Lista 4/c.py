# Função que insere o nome de um personagem na lista
def adicionar_personagem(lista, personagem, n_max, numero_personagens):
    if numero_personagens < n_max:
        lista[numero_personagens] = personagem # Adiciona o personagem na posição correta da lista
        print(f"Personagem {personagem} adicionado")
        return True
    return False

# Função que remove o nome de um personagem da lista
def remover_personagem(lista, personagem, n_max):
    for i in range(n_max):
        if lista[i] == personagem: # Verifica se o personagem atual da lista é igual ao personagem a ser removido
            lista[i] = "" # Define a posição do personagem removido como uma string vazia
            print(f"Personagem {personagem} removido")
            while i < n_max - 1 and lista[i + 1] != "":
                lista[i] = lista[i + 1] # Move o personagem da próxima posição para a posição atual
                lista[i + 1] = "" # Define a próxima posição como vazia
                i += 1  # Avança para a próxima posição
            return True
    return False

# Função que verifica se todos os personagens na lista são válidos
def checar_vitoria(lista, personagens_validos):
    for i in lista:
        if i != "" and i not in personagens_validos: # Verifica se o personagem é válido
            return False
    return True

personagens_da_serie = ["Jinx", "Vi", "Heimerdinger", "Ekko", "Caitlyn", "Jayce", "Viktor", "Silco", "Claggor", "Vander", "Mylo"]

n_max = int(input())
lista_personagens = [""] * n_max # Cria uma lista vazia com o tamanho do número máximo de personagens
quantidade_personagens = 0

while quantidade_personagens < n_max:
    comando = input()
    personagem = input()

    if comando == "Adiciona":
        if adicionar_personagem(lista_personagens, personagem, n_max, quantidade_personagens): # Tenta adicionar o personagem à lista
            quantidade_personagens += 1

    elif comando == "Remove":
        if remover_personagem(lista_personagens, personagem, n_max): # Tenta remover o personagem da lista
            quantidade_personagens -= 1


print("Lista final de personagens:")
for i in lista_personagens:
    if i != "": # Verifica se a posição não está vazia
        print(i) # Imprime o nome de cada personagem válido que permanece na lista

if checar_vitoria(lista_personagens, personagens_da_serie): # Verifica se o jogador venceu (todos os personagens na lista são válidos)
    print("Parabéns!! Você conseguiu acertar todos os nomes.")
    print("UAUUU! Acho que estamos preparados para ver a segunda temporada.")
else:
    print("Infelizmente você perdeu...")
    print("Eita... Vamos precisar assistir novamente.")