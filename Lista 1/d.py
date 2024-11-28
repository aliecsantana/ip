votosrodri = 0
votosvinijr = 0

votojurado1 = input()
paisjurado1 = input()
votojurado2 = input()
paisjurado2 = input()

if votojurado1 == 'rodri' and paisjurado1 != 'Espanha':
    votosrodri += 1
    print("Voto registrado!")
elif votojurado1 == 'vinijr' and paisjurado2 != 'Brasil':
    votosvinijr += 1
    print("Voto registrado!")
else:
    print("Voto inválido! Não é permitido votar em jogadores do mesmo país.")

if votojurado2 == 'rodri' and paisjurado2 != 'Espanha':
    votosrodri += 1
    print("Voto registrado!")
elif votojurado2 == 'vinijr' and paisjurado2 != 'Brasil':
    votosvinijr += 1
    print("Voto registrado!")
else:
    print("Voto inválido! Não é permitido votar em jogadores do mesmo país.")

print(f"Votos válidos para rodri: {votosrodri}")
print(f"Votos válidos para vinijr: {votosvinijr}")