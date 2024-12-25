quant_membros = int(input())

filmes_br = 0
filmes_fora = 0
n_filmes = 0
palavras_chave_1 = "natal"
palavras_chave_2 = "papai noel"
palavras_chave_3 = "magia"

print("MARATONA DE NATAL: PAVÊ, RABANADA E FILMES")

# Loop para entrada de filmes
nome_filme = ""
while nome_filme.lower() != "chega de filmes por hoje":
    nome_filme = input()
    if nome_filme.lower() != "chega de filmes por hoje":
        nacionalidade_filme = input().lower()

        # Verifica a nacionalidade e as palavras-chave
        brasileiro = (nacionalidade_filme == "br" or nacionalidade_filme == "brasil")
        natalino = (palavras_chave_1 in nome_filme.lower() or
                       palavras_chave_2 in nome_filme.lower() or
                       palavras_chave_3 in nome_filme.lower())

        if brasileiro * natalino:
            n_filmes += 1
            filmes_br += 1
            print(f"{n_filmes}º filme: {nome_filme}")

            # Recebe as notas dos membros e calcula a média
            soma_notas = 0
            quant_membros_avaliadores = 0
            while quant_membros_avaliadores < quant_membros:
                nota = int(input())
                soma_notas += nota
                quant_membros_avaliadores += 1
            media = soma_notas / quant_membros
            print(f"Média de votos para '{nome_filme}': {media:.1f}")
        elif natalino:
            filmes_fora += 1

print(f"{filmes_br} Filmes BR X {filmes_fora} Filmes FORA")

if filmes_br == 0:
    print("Infelizmente esse ano não será nem pa vê e nem pa comer, sua lista não possui um filme bom, ops… nacional")
elif filmes_br == 1:
    print("De toda sua lista, apenas UM filme de natal é nacional, melhore suas escolhas e tente novamente!")
else:
    print("A ceia está servida? Porque aqui estão os filmes brasileiros que vão dar o toque especial da sua maratona no Natal!")