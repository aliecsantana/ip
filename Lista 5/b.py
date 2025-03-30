def explorar_tesouros(lista, energia, quantidade_moedas, quantidade_itens_raros, indice):
    if energia == 0:
        print("Ah, cansei. Vou descansar.")
        return quantidade_moedas, quantidade_itens_raros
    elif indice >= len(lista):
        return quantidade_moedas, quantidade_itens_raros

    entrada = lista[indice]

    if entrada.isnumeric():
        quantidade_moedas += int(entrada)
        energia -= 1
    elif entrada == "X":
        energia -= 1
    else:
        print(f"Oba! Encontrei um {entrada} 🐧🎉")
        quantidade_itens_raros += 1
        energia -= 1
        energia += 2
    # Chama a função recursivamente para o próximo local (índice + 1)
    return explorar_tesouros(lista, energia, quantidade_moedas, quantidade_itens_raros, indice + 1)

def resumo_exploracao(quantidade_moedas, quantidade_itens_raros):
    if quantidade_moedas == 0 and quantidade_itens_raros == 0:
        print("Essa caminhada não foi nada produtiva. É melhor ir pescar.")
    elif quantidade_moedas > 0 and quantidade_itens_raros == 0:
        print(f"Estamos ricos!! Encontrei {quantidade_moedas} moedas.")
    elif quantidade_moedas == 0 and quantidade_itens_raros > 0:
        print(f"Dinheiro? Não temos. Mas temos {quantidade_itens_raros} itens raros.")
    else:
        print(f"Quem diria!! {quantidade_moedas} moedas e {quantidade_itens_raros} itens raros. Hoje eu mereço bolo, não aqueles puffitos de sempre.")

lista = input().split(", ")

energia_inicial = 4

quantidade_moedas, quantidade_itens_raros = explorar_tesouros(lista, energia_inicial, 0, 0, 0)

resumo_exploracao(quantidade_moedas, quantidade_itens_raros)