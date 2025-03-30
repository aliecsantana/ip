# Listas para armazenar objetos e armas, divididos por classificações
objetos = [[], [], [], [], []] 
armas = [[], [], [], [], []]

tipo_item = input()

while tipo_item != "Catalogação encerrada!":
    descricao_item = input()
    nome_item, classificacao = descricao_item.split(" - ") # Separa o nome do item e sua classificação com " - "
    classificacao = int(classificacao) # Converte a classificação para um número inteiro
    
    if tipo_item == "objeto":
        objetos[classificacao].append(nome_item) # Adiciona à lista de objetos na classificação correspondente
        print(f"O objeto {nome_item} foi catalogado com sucesso!")
    elif tipo_item == "arma":
        armas[classificacao].append(nome_item) # Adiciona à lista de armas na classificação correspondente
        print(f"A arma {nome_item} foi catalogada com sucesso!")
    
    tipo_item = input()

print("Processando lista de itens…")

print("\nITENS AMALDIÇOADOS DA TOKYO JUJUTSU HIGH\n")

# Define a lista com os nomes das classificações
classificacoes = ["Categoria Especial", "Nível 1", "Nível 2", "Nível 3", "Nível 4"]

print("Objetos")
for indice_classificacoes in range(5):
    # Verifica se há objetos na classificação atual
    if objetos[indice_classificacoes]:
        print(f"{classificacoes[indice_classificacoes]}: {', '.join(objetos[indice_classificacoes])}") # Exibe o nome da classificação e a lista de objetos, separados por vírgula

# Separa a listagem de objetos da de armas com uma linha em branco
print()

print("Armas")
for indice_classificacoes in range(5):
    # Verifica se há armas na classificação atual
    if armas[indice_classificacoes]:
        print(f"{classificacoes[indice_classificacoes]}: {", ".join(armas[indice_classificacoes])}") # Exibe o nome da classificação e a lista de armas, separados por vírgula