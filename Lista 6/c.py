def registrar_informacoes():
    lideres = {} # Dicionário para guardar informações dos líderes
    acontecimentos = {} # Dicionário para guardar informações dos acontecimentos

    executar = True

    while executar:
        comando = input()
        
        if comando == "REGISTRAR LÍDER":
            nome = input()
            cargo_papel = input()
            cidade_origem = input()
            data_nascimento = input()
            
            # Armazena as informações do líder em um dicionário
            lideres[nome] = {'Cargo/Papel': cargo_papel, 'Cidade de Origem': cidade_origem, 'Data de Nascimento': data_nascimento}
        
        elif comando == "REGISTRAR ACONTECIMENTO":
            data = input()
            acontecimento = input()
            local = input()
            
            # Armazena as informações do acontecimento em um dicionário
            acontecimentos[data] = {'Acontecimento': acontecimento, 'Local': local}
        
        elif comando == "FIM":
            executar = False
    
    if len(lideres) > 0:
        print("Consegui encontrar os seguintes líderes da Revolução Pernambucana de 1817:")
        i = 0
        nomes_lideres = tuple(lideres.keys()) # Converte as chaves do dicionário em uma tupla
        for i in range(len(nomes_lideres)):
            nome = nomes_lideres[i] # Obtém o nome do líder atual
            informacoes = lideres[nome] # Obtém as informações do líder atual a partir do dicionário "lideres"
            print(f"{nome}:")
            print(f"- Cargo/Papel: {informacoes['Cargo/Papel']}") # Imprime o cargo/papel do líder, acessando o valor associado à chave "Cargo/Papel" do dicionário "informacoes"
            print(f"- Cidade de Origem: {informacoes['Cidade de Origem']}") # Imprime a cidade de origem do líder, acessando o valor associado à chave "Cidade de Origem" do dicionário "informacoes"
            print(f"- Data de Nascimento: {informacoes['Data de Nascimento']}") # Imprime a data de nascimento do líder, acessando o valor associado à chave "Data de Nascimento" do dicionário "informacoes"
    else:
        print("Aff, pelo jeito nessa época não tinha LinkedIn pra facilitar encontrar os tais líderes dessa tal Revolução... Desisto.")
    
    print()
    
    if len(acontecimentos) > 0:
        print("Vivenciei os seguintes acontecimentos históricos da Revolução Pernambucana de 1817:")
        j = 0
        datas_acontecimentos = tuple(acontecimentos.keys()) # Converte as chaves do dicionário em uma tupla
        for j in range(len(datas_acontecimentos)):
            data = datas_acontecimentos[j] # Obtém a data do acontecimento atual
            informacoes = acontecimentos[data] # Obtém as informações do acontecimento atual a partir do dicionário "acontecimentos"
            print(f"({data}): {informacoes['Acontecimento']}, {informacoes['Local']}") # Imprime a data, o acontecimento e o local, acessando os valores associados a variável "data" e às chaves "Acontecimento" e "Local" do dicionário "informacoes"

    else:
        print("Ter que ler todos esses jornais não é legal, e ainda não encontrei nenhum acontecimento... saudade do Pernambuco Extraordinário pra me manter informado.")
    
    if len(lideres) > 0 and len(acontecimentos) > 0:
        print()
        print("Pronto, agora CIn tô preparado pra lutar e tornar Pernambuco o melhor país em linha reta do mundo!!!")

registrar_informacoes()