numero_renas = int(input())

if numero_renas < 3:
    print("Meu senhor, com essa quantidade de rena vai ter que entregar os presentes a pé, viu?!")
else:
    numero_voltas = int(input())

    if numero_renas == 3:
        rena1 = input()
        rena2 = input()
        rena3 = input()
        print("Como só temos 3 renas aptas pro serviço esse ano, não adianta muito querer ficar escolhendo")
        print("As três únicas renas capazes de participar esse ano são:")
        print(f"{rena1}, {rena2} e {rena3}.")
        print("Não haverá teste de desempenho entre elas!")
    else:
        mais_atletica1 = ""
        pontuacao_total1 = 0
        mais_atletica2 = ""
        pontuacao_total2 = 0
        mais_atletica3 = ""
        pontuacao_total3 = 0

        # Avalia e pontua cada rena com base nos nomes e desempenho nas voltas
        for rena in range(1, numero_renas + 1):
            nome = input()
            nome_lower = nome.lower()
            pontuacao_inicial = 0

            # Calcula a pontuação inicial com base nas vogais do nome da rena
            for vogal in nome_lower:
                if vogal == 'a':
                    pontuacao_inicial += 8
                elif vogal == 'e':
                    pontuacao_inicial += 5
                elif vogal == 'i':
                    pontuacao_inicial += 4
                elif vogal == 'o':
                    pontuacao_inicial += 3
                elif vogal == 'u':
                    pontuacao_inicial += 2

            pontuacao_final = pontuacao_inicial
            # Calcula a pontuação final baseada no número de voltas
            for volta in range(1, numero_voltas + 1):
                resto = pontuacao_inicial % volta
                if resto == 0:
                    pontuacao_final += 2
                elif resto % 2 == 0:
                    pontuacao_final += 1

            # Define as três renas mais atléticas com base na pontuação final
            if pontuacao_final > pontuacao_total1:
                mais_atletica3, pontuacao_total3 = mais_atletica2, pontuacao_total2
                mais_atletica2, pontuacao_total2 = mais_atletica1, pontuacao_total1
                mais_atletica1, pontuacao_total1 = nome, pontuacao_final
            elif pontuacao_final > pontuacao_total2:
                mais_atletica3, pontuacao_total3 = mais_atletica2, pontuacao_total2
                mais_atletica2, pontuacao_total2 = nome, pontuacao_final
            elif pontuacao_final > pontuacao_total3:
                mais_atletica3, pontuacao_total3 = nome, pontuacao_final

        print("As três renas mais atléticas pra temporada de Natal são:")
        print(f"{mais_atletica1}, {mais_atletica2} e {mais_atletica3}.")
