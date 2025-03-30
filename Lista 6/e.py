"""Este código acabou ficando sem comentários, mas em algum momento eu os adiciono."""

def calcular_pontuacao(palavra_digitada, palavra_dicionario):
    pontuacao = 0
    for i in range(min(len(palavra_digitada), len(palavra_dicionario))):
        pontuacao += ord(palavra_digitada[i]) - ord(palavra_dicionario[i])
    return pontuacao

def gerar_sugestoes(texto_portugues, dicionario):
    palavras = texto_portugues.split()
    ultimas_palavras = palavras[-4:] if len(palavras) >= 4 else palavras
    pontuacoes = {}
    
    for palavra_dicionario in dicionario:
        pontuacao_total = 0
        for palavra_digitada in ultimas_palavras:
            pontuacao_total += calcular_pontuacao(palavra_digitada, palavra_dicionario)
        pontuacoes[palavra_dicionario] = pontuacao_total
    
    sugestoes_ordenadas = sorted(pontuacoes.keys(), key=lambda x: (pontuacoes[x], list(dicionario.keys()).index(x)))
    
    return sugestoes_ordenadas[:4]

def executar_programa():
    dicionario = {}
    texto_portugues = ""
    texto_traducao = ""
    executar = True
    ultima_saida = ""
    
    while executar:
        instrucao = input().strip()
        
        partes_instrucao = instrucao.split()
        processar_comando = len(partes_instrucao) > 0
        
        if processar_comando:
            tipo_instrucao = partes_instrucao[0]
            
            if tipo_instrucao == "*ADD":
                if len(partes_instrucao) == 2:
                    palavra_traducao = partes_instrucao[1]
                    if ":" in palavra_traducao:
                        palavra, traducao = palavra_traducao.split(":")
                        dicionario[palavra] = traducao
            
            elif tipo_instrucao == "*DEL":
                if len(partes_instrucao) == 2:
                    palavra = partes_instrucao[1]
                    if palavra in dicionario:
                        del dicionario[palavra]
            
            elif tipo_instrucao == "*ESC":
                if len(partes_instrucao) == 2:
                    palavra = partes_instrucao[1]
                    if palavra in dicionario:
                        texto_traducao += dicionario[palavra] + " "
                        texto_portugues += palavra + " "
                    else:
                        texto_traducao += palavra + " "
                        texto_portugues += palavra + " "
            
            elif tipo_instrucao == "*SEL":
                if len(partes_instrucao) == 2:
                    numero_sugestao = partes_instrucao[1]
                    numero_sugestao = int(numero_sugestao)
                    sugestoes = gerar_sugestoes(texto_portugues, dicionario)
                    if 1 <= numero_sugestao <= len(sugestoes):
                        palavra_selecionada = sugestoes[numero_sugestao - 1]
                        texto_portugues += palavra_selecionada + " "
                        texto_traducao += dicionario.get(palavra_selecionada, palavra_selecionada) + " "
            
            elif tipo_instrucao == "*FIM":
                executar = False
        
        if texto_portugues.strip() or texto_traducao.strip():
            sugestoes = gerar_sugestoes(texto_portugues, dicionario)
            nova_saida = f"{texto_traducao.strip()} ({','.join(sugestoes)})" if texto_traducao.strip() else texto_traducao.strip()
            
            if nova_saida != ultima_saida:
                print(nova_saida)
                print("------------------")
                ultima_saida = nova_saida
    
    print(texto_portugues.strip())
    print(texto_traducao.strip())

executar_programa()