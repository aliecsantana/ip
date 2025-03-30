qtd_monitores = int(input())

# Listas para armazenar os nomes dos monitores e as mudanças observadas
nomes = []
mudancas = []

# Listas para armazenar os monitores de cada categoria
aprimoradores = []
emissores = []
transmutadores = []
manipuladores = []
conjuradores = []
especialistas = []

for indice in range(qtd_monitores):
    nome = input()
    mudanca = input()

    if nome in nomes:
        idx = nomes.index(nome) # Encontra o índice do nome do monitor na lista
        nomes.pop(idx) # Remove o nome do monitor
        mudancas.pop(idx) # Remove a mudança anterior associada ao monitor
    
    nomes.append(nome)  # Adiciona o nome do monitor na lista
    mudancas.append(mudanca)  # Adiciona a mudança na lista

for indice in range(len(nomes)):
    nome = nomes[indice] # Obtém o nome do monitor
    mudanca = mudancas[indice] # Obtém a mudança correspondente

    if mudanca == "O volume da água foi alterado.":
        aprimoradores.append(nome) # Adiciona o nome do monitor à categoria de aprimoradores
    elif mudanca == "A cor da água foi alterada.":
        emissores.append(nome) # Adiciona o nome do monitor à categoria de emissores
    elif mudanca == "O gosto da água foi alterado.":
        transmutadores.append(nome) # Adiciona o nome do monitor à categoria de transmutadores
    elif mudanca == "A folha se moveu.":
        manipuladores.append(nome) # Adiciona o nome do monitor à categoria de manipuladores
    elif mudanca == "Impurezas apareceram na água.":
        conjuradores.append(nome) # Adiciona o nome do monitor à categoria de conjuradores
    else:
        especialistas.append(nome) # Adiciona o nome do monitor à categoria de especialistas

if len(aprimoradores) > 0:
    print(f"Temos um total de {len(aprimoradores)} aprimoradores entre os monitores! Eles são: {', '.join(aprimoradores)}")

if len(emissores) > 0:
    print(f"Temos um total de {len(emissores)} emissores entre os monitores! Eles são: {', '.join(emissores)}")

if len(transmutadores) > 0:
    print(f"Temos um total de {len(transmutadores)} transmutadores entre os monitores! Eles são: {', '.join(transmutadores)}")

if len(manipuladores) > 0:
    print(f"Temos um total de {len(manipuladores)} manipuladores entre os monitores! Eles são: {', '.join(manipuladores)}")

if len(conjuradores) > 0:
    print(f"Temos um total de {len(conjuradores)} conjuradores entre os monitores! Eles são: {', '.join(conjuradores)}")

if len(especialistas) > 0:
    print(f"Temos um total de {len(especialistas)} especialistas entre os monitores! Eles são: {', '.join(especialistas)}")