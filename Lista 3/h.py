sequencia_gojo = input().split('-') # Separa a sequência de números com "-"
numeros_gojo = [] # Lista que armazenará os números de Gojo

for num in sequencia_gojo:
    numeros_gojo.append(int(num)) # Converte o número de string para inteiro e adiciona à lista que armazena o conjunto de números de Gojo

tamanho_sequencia_geto = int(input())
soma_sequencia_geto = int(input())

tamanho_maior_sequencia_gojo = 0
soma_maior_sequencia_gojo = 0

tamanho_sequencia_atual_gojo = 1
soma_sequencia_atual_gojo = numeros_gojo[0] # Inicializa a soma da sequência atual de Gojo com o primeiro número da lista

for indice in range(1, len(numeros_gojo)):
    if numeros_gojo[indice] == numeros_gojo[indice-1] + 1:  # Verifica se o número atual é sequencial ao anterior
        tamanho_sequencia_atual_gojo += 1
        soma_sequencia_atual_gojo += numeros_gojo[indice] # Adiciona à soma da sequência atual o número atual
    else:
        if tamanho_sequencia_atual_gojo > tamanho_maior_sequencia_gojo:
            tamanho_maior_sequencia_gojo = tamanho_sequencia_atual_gojo
            soma_maior_sequencia_gojo = soma_sequencia_atual_gojo
        elif tamanho_sequencia_atual_gojo == tamanho_maior_sequencia_gojo:
            if soma_sequencia_atual_gojo > soma_maior_sequencia_gojo:
                soma_maior_sequencia_gojo = soma_sequencia_atual_gojo
        tamanho_sequencia_atual_gojo = 1
        soma_sequencia_atual_gojo = numeros_gojo[indice] # Reinicia a soma da sequência atual com o número atual

if tamanho_sequencia_atual_gojo > tamanho_maior_sequencia_gojo:
    tamanho_maior_sequencia_gojo = tamanho_sequencia_atual_gojo
    soma_maior_sequencia_gojo = soma_sequencia_atual_gojo
elif tamanho_sequencia_atual_gojo == tamanho_maior_sequencia_gojo:
    if soma_sequencia_atual_gojo > soma_maior_sequencia_gojo:
        soma_maior_sequencia_gojo = soma_sequencia_atual_gojo

if tamanho_maior_sequencia_gojo > tamanho_sequencia_geto:
    print("Uma vitória avassaladora de Satoru Gojo. Nem mesmo o infinito pode pará-lo. Ele realmente é o melhor!")
elif tamanho_maior_sequencia_gojo < tamanho_sequencia_geto:
    print("Inesperado! Suguru Geto domina com maestria. Uma vitória indiscutível!")
else:
    if soma_maior_sequencia_gojo > soma_sequencia_geto:
        print("Gojo vence por pouco. Mesmo com toda a pressão, ele continua no topo!")
    elif soma_maior_sequencia_gojo < soma_sequencia_geto:
        print("Geto vence por pouco. Sua estratégia foi impecável nesta batalha!")
    else:
        print("Um empate absoluto! Quem diria que duas lendas podem ser tão iguais em poder?")