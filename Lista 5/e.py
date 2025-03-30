lugares = ["PENGUINBAR", "PRAIAGELADA", "PENGUICUPSTADIUM", "DELEGACIAPOLAR", "SUBZEROWAY", "FRIODEJANEIRO"]

direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def buscar_palavra(matriz, palavra, posicao_x, posicao_y, indice_palavra):
    if indice_palavra == len(palavra):
        return True

    # Verifica se as coordenadas são válidas ou se o caractere atual não corresponde à letra da palavra
    if posicao_x < 0 or posicao_x >= len(matriz) or posicao_y < 0 or posicao_y >= len(matriz[0]) or matriz[posicao_x][posicao_y] != palavra[indice_palavra]:
        return False

    # Salva o valor original da coordenada
    valor_original = matriz[posicao_x][posicao_y]

    # Marca a coordenada atual como verificada
    matriz[posicao_x][posicao_y] = "VERIFICADO"

    for direcao_x, direcao_y in direcoes:
        nova_posicao_x = posicao_x + direcao_x
        nova_posicao_y = posicao_y + direcao_y
        if buscar_palavra(matriz, palavra, nova_posicao_x, nova_posicao_y, indice_palavra + 1): # Chama recursivamente para a próxima letra
            return True

    # Se não encontrar a palavra, restaura o valor original da coordenada
    matriz[posicao_x][posicao_y] = valor_original
    return False

def encontrar_lugar(matriz):
    for posicao_x in range(len(matriz)):
        for posicao_y in range(len(matriz[0])):
            for lugar in lugares:
                if matriz[posicao_x][posicao_y] == lugar[0]: # Se a letra inicial do lugar corresponde à letra da matriz
                    if buscar_palavra(matriz, lugar, posicao_x, posicao_y, 0): # Chama a função de busca recursiva para encontrar a palavra completa
                        return lugar
    return None

def converter_lugar(lugar):
    if lugar == "FRIODEJANEIRO":
        return "Frio de Janeiro"
    elif lugar == "DELEGACIAPOLAR":
        return "Delegacia Polar"
    elif lugar == "SUBZEROWAY":
        return "SubzeroWay"
    elif lugar == "PENGUINBAR":
        return "Penguin Bar"
    elif lugar == "PRAIAGELADA":
        return "Praia Gelada"
    elif lugar == "PENGUICUPSTADIUM":
        return "PenguiCup Stadium"
    return lugar

def executar_busca():
    n = int(input())
    matriz = []
    
    for i in range(n):
        linha = input().split()
        matriz.append(linha)

    lugar_encontrado = encontrar_lugar(matriz)

    if lugar_encontrado:
        lugar_formatado = converter_lugar(lugar_encontrado)
        if lugar_formatado == "Delegacia Polar":
            print("Se formos até a Delegacia Polar, estaremos mexendo com um fora da lei. Vamos até lá investigar!")
        elif lugar_formatado == "Frio de Janeiro":
            print("ARRGH! Todos sabem que o melhor carnaval é no bloco Pinguim da Madrugada. Vamos buscar nossa estátua no Frio de Janeiro")
        elif lugar_formatado == "Penguin Bar" or lugar_formatado == "Praia Gelada" or lugar_formatado == "PenguiCup Stadium" or lugar_formatado == "SubzeroWay":
            print(f"Temos que correr! O Pinguim da Madrugada pode estar no(a) {lugar_formatado}. Vamos salvar nosso Carnaval de Inverno!")
    else:
        print("Nosso carnaval de inverno está perdido... NÃOOOOO")

executar_busca()