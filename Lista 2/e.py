nome_musica1 = ""
quantidade_streams1 = 0
nome_musica2 = ""
quantidade_streams2 = 0
nome_musica3 = ""
quantidade_streams3 = 0

# Lê os dados das 3 músicas e seus respectivos números de streams
for posicao in range(1, 4):
    nome_musica = input()
    quantidade_streams = int(input())
    
    # Armazena o nome e quantidade de streams de acordo com a posição
    if posicao == 1:
        nome_musica1 = nome_musica
        quantidade_streams1 = quantidade_streams
    elif posicao == 2:
        nome_musica2 = nome_musica
        quantidade_streams2 = quantidade_streams
    else:
        nome_musica3 = nome_musica
        quantidade_streams3 = quantidade_streams

# Ordena as músicas com base na quantidade de streams
if quantidade_streams1 > quantidade_streams2:
    if quantidade_streams1 > quantidade_streams3:
        # Se a primeira música tem mais streams que as outras duas
        nome_1_lugar = nome_musica1
        streams_1_lugar = quantidade_streams1
        if quantidade_streams2 > quantidade_streams3:
            nome_2_lugar = nome_musica2
            streams_2_lugar = quantidade_streams2
            nome_3_lugar = nome_musica3
            streams_3_lugar = quantidade_streams3
        else:
            nome_2_lugar = nome_musica3
            streams_2_lugar = quantidade_streams3
            nome_3_lugar = nome_musica2
            streams_3_lugar = quantidade_streams2
    else:
        # Se a terceira música tem mais streams que a primeira
        nome_1_lugar = nome_musica3
        streams_1_lugar = quantidade_streams3
        nome_2_lugar = nome_musica1
        streams_2_lugar = quantidade_streams1
        nome_3_lugar = nome_musica2
        streams_3_lugar = quantidade_streams2
else:
    if quantidade_streams2 > quantidade_streams3:
        # Se a segunda música tem mais streams que a terceira
        nome_1_lugar = nome_musica2
        streams_1_lugar = quantidade_streams2
        if quantidade_streams1 > quantidade_streams3:
            nome_2_lugar = nome_musica1
            streams_2_lugar = quantidade_streams1
            nome_3_lugar = nome_musica3
            streams_3_lugar = quantidade_streams3
        else:
            nome_2_lugar = nome_musica3
            streams_2_lugar = quantidade_streams3
            nome_3_lugar = nome_musica1
            streams_3_lugar = quantidade_streams1
    else:
        # Se a terceira música tem mais streams que a segunda
        nome_1_lugar = nome_musica3
        streams_1_lugar = quantidade_streams3
        nome_2_lugar = nome_musica2
        streams_2_lugar = quantidade_streams2
        nome_3_lugar = nome_musica1
        streams_3_lugar = quantidade_streams1

print(f"1º: {nome_1_lugar} teve {streams_1_lugar} de streams e foi a música mais ouvida de Simone!")
print(f"2º: {nome_2_lugar} teve {streams_2_lugar} de streams e foi a segunda música mais ouvida de Simone!")
print(f"3º: {nome_3_lugar} teve {streams_3_lugar} de streams e completou o top 3 das músicas mais ouvidas da artista!")

# Verifica se alguma das músicas possui mais de 10 milhões de streams
if streams_1_lugar > 10000000:
    print(f"Uau! {nome_1_lugar} foi um hit certeiro da rainha do Natal!")
if streams_2_lugar > 10000000:
    print(f"Uau! {nome_2_lugar} foi um hit certeiro da rainha do Natal!")
if streams_3_lugar > 10000000:
    print(f"Uau! {nome_3_lugar} foi um hit certeiro da rainha do Natal!")

# Verifica se alguma das músicas possui menos de 1 milhão de streams
if streams_1_lugar < 1000000:
    print(f"Bom… a música {nome_1_lugar} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")
if streams_2_lugar < 1000000:
    print(f"Bom… a música {nome_2_lugar} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")
if streams_3_lugar < 1000000:
    print(f"Bom… a música {nome_3_lugar} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")

# Verifica a diferença de streams entre a música mais ouvida e a segunda mais ouvida
if streams_1_lugar - streams_2_lugar > 5000000:
    print(f"{nome_1_lugar} foi disparada a mais ouvida neste ano! Nenhuma outra música natalina chega aos pés dela!")
elif streams_1_lugar - streams_2_lugar < 1000000:
    print(f"{nome_1_lugar} foi a mais ouvida, mas não podemos esquecer da música {nome_2_lugar}! Fez bonito nesse feriado!")