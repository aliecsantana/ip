nome_suspeito1 = input()
distancia_suspeito1 = int(input())
nome_suspeito2 = input()
distancia_suspeito2 = int(input())

hipotenusa = (distancia_suspeito1 ** 2 + distancia_suspeito2 ** 2) ** (1/2)

# Se a soma das distâncias for par
if hipotenusa % 2 == 0:
    print(f"{nome_suspeito1} e {nome_suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!")
# Se a soma das distâncias for ímpar
else:
    categoria_suspeito1 = input()
    categoria_suspeito2 = input()

    # Se ambos forem fãs
    if categoria_suspeito1 == "Fã" and categoria_suspeito2 == "Fã":
        if distancia_suspeito1 % 2 == 0 and distancia_suspeito2 % 3 == 0:
            print(f"{nome_suspeito1} e {nome_suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!")
        elif distancia_suspeito1 % 2 == 0:
            print(f"{nome_suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        elif distancia_suspeito2 % 3 == 0:
            print(f"{nome_suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        else:
            print(f"{nome_suspeito1} e {nome_suspeito2} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!")

    # Se ambos forem jogadores
    elif categoria_suspeito1 == "Jogador" and categoria_suspeito2 == "Jogador":
        if distancia_suspeito1 % 2 == 0 and distancia_suspeito2 % 5 == 0:
            print(f"{nome_suspeito1} e {nome_suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!")
        elif distancia_suspeito1 % 2 == 0:
            print(f"{nome_suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        elif distancia_suspeito2 % 5 == 0:
            print(f"{nome_suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        else:
            print(f"{nome_suspeito1} e {nome_suspeito2} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!")

    # Se ambos forem jornalistas
    elif categoria_suspeito1 == "Jornalista" and categoria_suspeito2 == "Jornalista":
        if distancia_suspeito1 % 3 == 0 and distancia_suspeito2 % 5 == 0:
            print(f"{nome_suspeito1} e {nome_suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!")
        elif distancia_suspeito1 % 3 == 0:
            print(f"{nome_suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        elif distancia_suspeito2 % 5 == 0:
            print(f"{nome_suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        else:
            print(f"{nome_suspeito1} e {nome_suspeito2} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!")

    # Se os dois forem de categorias diferentes
    else:
        if distancia_suspeito1 < distancia_suspeito2:
            print(f"{nome_suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        elif distancia_suspeito1 > distancia_suspeito2:
            print(f"{nome_suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        else:
            print(f"{nome_suspeito1} e {nome_suspeito2} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!")
