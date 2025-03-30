# Função que calcula o consumo de energia de cada máquina
def calculo_consumo_energia(tempo_horas, potencia, ineficiencia):
    energia_inicial = potencia * tempo_horas
    consumo_total = energia_inicial * (1 + ineficiencia / 100)
    return round(consumo_total, 2) # Retorna o consumo total arredondado para 2 casas decimais

# Função que calcula o dinheiro gasto por cada máquina
def calculo_dinheiro_gasto(consumo, preco):
    gasto = consumo * preco
    return round(gasto, 2) # Retorna o gasto arredondado para 2 casas decimais

# Função que realiza a análise das máquinas
def analise():
    quantidade_maquinas = int(input())
    gasto_total = 0
    gasto_maximo = 0

    for i in range(quantidade_maquinas):
        quantidade_horas_ligada = int(input())
        potencia = float(input())
        porcentagem_ineficiencia = int(input())
        preco = float(input())

        energia_total_consumida = calculo_consumo_energia(quantidade_horas_ligada, potencia, porcentagem_ineficiencia) # Calcula a energia total consumida pela máquina
        gasto_individual = calculo_dinheiro_gasto(energia_total_consumida, preco) # Calcula o gasto individual da máquina

        if energia_total_consumida == 0:
            print("Parece que essa coisa nem ao menos funciona")
        elif energia_total_consumida <= 100:
            print(f"Temos aqui uma máquina formidável, seu consumo de energia é {energia_total_consumida:.2f}")
        elif energia_total_consumida <= 300:
            print(f"Você tem certeza que essa coisa não vai explodir? seu consumo de energia é {energia_total_consumida:.2f}")
        else:
            print("Você se importaria de jogar seus explosivos em qualquer outro lugar?")

        gasto_total += gasto_individual
        if gasto_individual > gasto_maximo:
            gasto_maximo = gasto_individual

    print(f"Os gastos totais com as maquinas foi de {gasto_total:.2f}")
    print(f"A máquina mais cara gasta um total de {gasto_maximo:.2f} para os cofres de Piltover")

# Chama a função que realiza a análise das máquinas
analise()