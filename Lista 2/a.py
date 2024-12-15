entrada = ""
boneco = 0
videogame = 0
bicicleta = 0
outros = 0
total = 0

# Loop para processar as entradas do usuário até que "FIM" seja digitado, verificando o tipo de presente e incrementando os contadores correspondentes
while True:
    entrada = input()
    if entrada == "FIM":
        break
    if entrada == "Boneco":
        print("Mais um presente saindo!")
        boneco += 1
        total += 1
    elif entrada == "Videogame":
        print("Mais um presente saindo!")
        videogame += 1
        total += 1
    elif entrada == "Bicicleta":
        print("Mais um presente saindo!")
        bicicleta += 1
        total += 1
    else:
        print("Esse presente não está sendo fabricado nesse momento")
        outros += 1
        total += 1

print("Vamos agora ao relatório dos presentes!\n")

# Calcula as porcentagens de cada tipo de presente
if total > 0:
    porcentagem_bonecos = (boneco / total) * 100
    porcentagem_videogames = (videogame / total) * 100
    porcentagem_bicicletas = (bicicleta / total) * 100
    porcentagem_outros = (outros / total) * 100
else:
    porcentagem_bonecos = porcentagem_videogames = porcentagem_bicicletas = porcentagem_outros = 0.0

# Imprime o relatório com a quantidade de unidades e a porcentagem de cada tipo de presente
print(f"Boneco - {boneco} unidades - {porcentagem_bonecos:.2f}%")
print(f"Videogame - {videogame} unidades - {porcentagem_videogames:.2f}%")
print(f"Bicicleta - {bicicleta} unidades - {porcentagem_bicicletas:.2f}%")
print(f"Outros - {outros} unidades - {porcentagem_outros:.2f}%")

# Verifica se deve-se expandir, fechar ou manter a fábrica
if outros == 0:
    print("A demanda está muito alta! Teremos que fazer mais uma fábrica!")
else:
    if porcentagem_outros > 50:
        print("Parece que o Papai Noel terá que fechar a fábrica :(")
    elif porcentagem_bonecos <= 50 and porcentagem_videogames <= 50 and porcentagem_bicicletas <= 50 and porcentagem_outros <= 50:
        print("A fábrica está cumprindo seu papel, porém não precisa ser expandida")  
    else:
        if porcentagem_bonecos > 50:
            presente = "Boneco"
            print(f"{presente} está sendo muito desejado! A fábrica terá que ser expandida!")
        elif porcentagem_videogames > 50:
            presente = "Videogame"
            print(f"{presente} está sendo muito desejado! A fábrica terá que ser expandida!")
        elif porcentagem_bicicletas > 50:
            presente = "Bicicleta"
            print(f"{presente} está sendo muito desejado! A fábrica terá que ser expandida!")