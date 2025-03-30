# Função que registra as conexões do autômato
def registrar_conexoes(n):
    automato = []
    for i in range(n):
        conexoes = input().split(", ")
        conexao_zero = conexoes[0].split(" - ")[1] # Extrai o destino da transição de "0"
        conexao_um = conexoes[1].split(" - ")[1] # Extrai o destino da transição de "1"
        automato.append([conexao_zero, conexao_um]) # Adiciona as conexões ao autômato
    return automato # Retorna a lista de transições

# Função que processa uma cadeia para verificar se é aceita pelo autômato
def processar_cadeia(automato, cadeia, estado_inicial, estado_aceitacao, estados):
    caminho = [estado_inicial] # Lista que irá registrar o caminho percorrido
    estado_atual = estado_inicial
    if cadeia == "ε":
        if estado_atual == estado_aceitacao:
            print("Caramba, essa cadeia é abençoada! Nem precisei trabalhar!")
            print("{" + estado_inicial + "}") # Exibe o estado inicial como o caminho
            return True # Retorna True quando a cadeia é aceita pelo autômato
        else:
            print("Nossa, que maldição! Nem começou e já deu errado…")
            print("{" + estado_inicial + "}") # Exibe o estado inicial como o caminho
            return False # Retorna False quando a cadeia não é aceita pelo autômato, ou quando há um erro
    
    for i in cadeia:
        if i not in ["0", "1"]: # Verifica se o símbolo é válido (0 ou 1)
            print(f"Só pode estar de brincadeira comigo! Como vou lidar com {i} dentro da máquina?")  # Mensagem de erro
            print("{" + " -> ".join(caminho) + " -> ERROR}")  # Exibe o caminho até o erro
            return False # Retorna False quando a cadeia não é aceita pelo autômato, ou quando há um erro
        novo_estado = automato[estados.index(estado_atual)][int(i)] # Calcula o próximo estado com base no símbolo
        if novo_estado != estado_atual:
            caminho.append(novo_estado)
        estado_atual = novo_estado
    if estado_atual == estado_aceitacao:
        print("Beleza! Após suar muito a cadeia foi aceita, o esforço ta sendo compensado!")
        print("{" + " -> ".join(caminho) + "}") # Exibe o caminho completo
        return True # Retorna True quando a cadeia é aceita pelo autômato
    else:
        print("Que tristeza, todo esse arrudeio pra nada…")
        print("{" + " -> ".join(caminho) + "}") # Exibe o caminho completo
        return False # Retorna False quando a cadeia não é aceita pelo autômato, ou quando há um erro

# Função que imprime as conexões do autômato
def imprimir_conexoes(automato, estados):
    for i in range(len(automato)):
        print(f"{estados[i]}: {{0 -> {automato[i][0]}, 1 -> {automato[i][1]}}}") # Exibe as transições para 0 e 1

# Função que executa o programa
def executar():
    n = int(input())
    if n == 1:
        print("É… acho que não tem muito o que fazer com apenas uma dimensão, vou ter que me contentar com minha triste realidade :(")
        return # Finaliza a execução
    
    estado_aceitacao = input()
    estados = ["q" + str(i) for i in range(1, n + 1)] # Gera a lista de estados
    automato = registrar_conexoes(n) # Registra as conexões do autômato
    imprimir_conexoes(automato, estados) # Imprime as conexões
    
    m = int(input())
    cadeias_aceitas = 0
    
    for j in range(m):
        cadeia_binaria = input()
        estado_inicial = input()
        if processar_cadeia(automato, cadeia_binaria, estado_inicial, estado_aceitacao, estados): # Processa a cadeia
            cadeias_aceitas += 1
    
    precisao = (cadeias_aceitas / m) * 100
    if precisao == 100:
        print("Sensacional :)! Com certeza vamos voltar pra casa com esse autômato, até Alan Turing teria inveja!")
    elif precisao >= 75:
        print("Show de bola! Se fizermos alguns ajustes nesse autômato, temos muitas chances de voltar pra casa!")
    elif precisao >= 50:
        print("Até que esse autômato da pro gasto, mas vamos precisar de uns bons ajustes…")
    elif precisao >= 25:
        print("Nossa, que situação horrível, não faço a mínima ideia de como concertar esse autômato")
    else:
        print("Nossas expectativas já eram baixas, mas não sabia que seria tão catastrófico assim :/")

# Chama a função "executar"
executar()