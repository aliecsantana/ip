# Inicializa as variáveis das votações com 0 votos em cada uma
votos_rodri = 0
votos_vini_jr = 0

voto_jurado1 = input()
pais_jurado1 = input()

voto_jurado2 = input()
pais_jurado2 = input()

# Se o voto do 1º jurado é válido
if voto_jurado1 == 'rodri' and pais_jurado1 != 'Espanha':
    votos_rodri += 1
    print("Voto registrado!")
elif voto_jurado1 == 'vinijr' and pais_jurado1 != 'Brasil':
    votos_vini_jr += 1
    print("Voto registrado!")
# Se o voto do 1º jurado é inválido
else:
    print("Voto inválido! Não é permitido votar em jogadores do mesmo país.")

# Se o voto do 2º jurado é válido
if voto_jurado2 == 'rodri' and pais_jurado2 != 'Espanha':
    votos_rodri += 1
    print("Voto registrado!")
elif voto_jurado2 == 'vinijr' and pais_jurado2 != 'Brasil':
    votos_vini_jr += 1
    print("Voto registrado!")
# Se o voto do 2º jurado é inválido
else:
    print("Voto inválido! Não é permitido votar em jogadores do mesmo país.")

print(f"Votos válidos para rodri: {votos_rodri}") 
print(f"Votos válidos para vinijr: {votos_vini_jr}")  