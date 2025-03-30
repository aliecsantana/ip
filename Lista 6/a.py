def catalogar_aprimorar_exibir():
    cidades = {} # Inicializa um dicionário vazio para armazenar as cidades e suas informações
    numero_total_participantes = 0
    executar = True

    while executar:
        nome_cidade = input()
        if nome_cidade.upper() == "FIM":
            executar = False
        else:
            comando = input()
            if comando == "adicionar":
                dados = input().split(", ")
                lider = dados[0]
                batalha = dados[1]
                numero_revolucionarios = int(dados[2])
                # Verifica se a cidade está no dicionário
                if nome_cidade in cidades:
                    print(f"Atualizando a cidade {nome_cidade}...")
                    numero_total_participantes -= cidades[nome_cidade][2] # Subtrai o número de revolucionários antigos da cidade do total de participantes
                    cidades[nome_cidade] = (lider, batalha, numero_revolucionarios) # Atualiza os dados da cidade no dicionário
                    print(f"Dados atualizados para {nome_cidade}.")
                else:
                    cidades[nome_cidade] = (lider, batalha, numero_revolucionarios) # Se a cidade não existe, adiciona os dados ao dicionário
                    print(f"Dados adicionados para {nome_cidade}.")
                numero_total_participantes += numero_revolucionarios
            elif comando == "deletar":
                # Verifica se a cidade está no dicionário
                if nome_cidade in cidades:
                    numero_total_participantes -= cidades[nome_cidade][2] # Subtrai o número de revolucionários da cidade do total de participantes
                    cidades = {i: j for i, j in cidades.items() if i != nome_cidade} # Cria um novo dicionário que contém todas as cidades, exceto a cidade que vai ser deletada
                    print(f"Dados removidos para a cidade {nome_cidade}.")
                else:
                    print(f"Nenhum dado encontrado para a cidade {nome_cidade}.")
            else:
                print("Comando inválido! Digite 'adicionar' ou 'deletar'.")

    print("RESUMO DAS CONTRIBUIÇÕES DA REVOLUÇÃO PERNAMBUCANA")
    print("-" * 50)
    
    # Itera sobre as cidades e suas informações no dicionário
    for i, j in cidades.items():
        k, l, m = j  # k = líder, l = batalha, m = número de revolucionários
        porcentagem = (m / numero_total_participantes) * 100
        print(f"{i}: O(a) líder {k} liderou a {l} com {porcentagem:.2f}% dos revolucionários registrados.")

catalogar_aprimorar_exibir()