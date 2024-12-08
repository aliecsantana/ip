projecao_desempenho = input()
projecao_participacao_gols = int(input())
desempenho_final = input()

pontuacao_final = 0
nivel_projecao = 0
nivel_final = 0
participacao_gols_final = 37
pontuacao_rodri = 1170
nivel_rodri = 3

print("Está aberta a revisão da premiação!")

# Analisa a projeção de desempenho
if projecao_desempenho == "Decepção":
    print("Parece que não estão colocando muitas expectativas para a temporada do nosso Vini Jr., não... Sempre subestimado!")
    nivel_projecao = 1
    pontuacao_final += 100
elif projecao_desempenho == "Oscilação":
    print("Os jornalistas acreditam que Vini Jr. terá atuações irregulares nesta temporada, mas quem sabe ele não supera as projeções?")
    nivel_projecao = 2
    pontuacao_final += 200
elif projecao_desempenho == "Importante":
    print("Em um elenco tão forte como o do Real Madrid, é normal as atenções serem divididas mesmo. O que importa é que ele não vai se esconder!")
    nivel_projecao = 3
    pontuacao_final += 300
elif projecao_desempenho == "Estrela":
    print("Vini Jr. será o craque do Real Madrid na temporada de 2023/2024! Será que ele consegue a tão sonhada Bola de Ouro?")
    nivel_projecao = 4
    pontuacao_final += 400

pontuacao_final += int((projecao_participacao_gols * 2) + (pontuacao_final / 2))

# Analisa o desempenho final
if desempenho_final == "Decepção":
    print("Vini Jr. decepcionou os torcedores em 2024, não era o ano dele.")
    nivel_final = 1
    pontuacao_final += 150
elif desempenho_final == "Oscilação":
    print("A temporada não foi das melhores, mas Vini Jr. conseguiu mostrar, em alguns momentos, que ele de fato é craque.")
    nivel_final = 2
    pontuacao_final += 250
elif desempenho_final == "Importante":
    print("Vini Jr. mostrou que é crucial para o elenco do Real Madrid e da Seleção.")
    nivel_final = 3
    pontuacao_final += 350
elif desempenho_final == "Estrela":
    print("Ele é demais! Herói do título da Champions, ele conseguiu mostrar ao mundo que é uma estrela do futebol!")
    nivel_final = 4
    pontuacao_final += 500

# Compara o desempenho final e a projeção
if nivel_final > nivel_projecao:
    print("Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!")
    pontuacao_final += 300
elif nivel_final == nivel_projecao:
    print("A mídia estava certa! Vini Jr. se manteve dentro das projeções dos jornalistas, mas será que é suficiente para vencer o Rodri?")
    pontuacao_final += 100
else:
    print("É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.")

# Compara a projeção de participação de gols e a participação de gols final
if participacao_gols_final > projecao_participacao_gols:
    print("Vini Jr. foi muito decisivo para sua equipe este ano, superando sua previsão de participações em gols!")
else:
    print("É, Vini Jr. não conseguiu provar que estavam errados, mas ainda assim ele segue vivo para a premiação.")

# Determina o resultado final
if pontuacao_final > pontuacao_rodri:
    print(f"O mundo estava certo! Com {pontuacao_final} pontos, Vini Malvadeza é o verdadeiro melhor do mundo! Chega dessa injustiça!")
elif pontuacao_final < pontuacao_rodri:
    print("Infelizmente, teremos que nos contentar com o Rodri sendo o melhor do mundo mesmo.")
else:
    print("Empate! Vamos ao critério de desempate.")
    if desempenho_final == "Estrela":
        print("Foi uma premiação apertada, mas a justiça foi feita! Vini Jr. é, sim, o melhor do mundo.")
    else:
        print("Bom, é isso. Ainda tivemos esperanças, mas o Rodri é, mesmo, o Bola de Ouro.")