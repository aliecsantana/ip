# Função que calcula a taxa de distribuição de recursos com base na situação econômica de Zaun
def calcular_taxa(situacao_zaun):
    if situacao_zaun == "desastre":
        return 0.9
    elif situacao_zaun == "crise":
        return 0.8
    elif situacao_zaun == "critica":
        return 0.7
    elif situacao_zaun == "normal":
        return 0.6
    elif situacao_zaun == "tranquilo":
        return 0.5
    else:
        return None # A taxa não é especificada

# Função que distribui os recursos entre Piltover e Zaun com base nas populações de ambas as cidades e a taxa, se calculada
def distribuir_recursos(total_recursos, populacao_piltover, populacao_zaun, taxa):
    if taxa is None: # Se a taxa não foi especificada, a quantidade de recursos distribuidos é proporcional a população de cada cidade
        total_populacao = populacao_piltover + populacao_zaun
        recursos_piltover = (populacao_piltover / total_populacao) * total_recursos
        recursos_zaun = (populacao_zaun / total_populacao) * total_recursos
    else:
        recursos_zaun = taxa * total_recursos
        recursos_piltover = total_recursos - recursos_zaun
    return recursos_piltover, recursos_zaun

# Função que imprime uma mensagem informativa sobre a distribuição de recursos
def mensagem(recursos_piltover, recursos_zaun):
    razao = recursos_zaun / recursos_piltover if recursos_piltover > 0 else float('inf') # Calcula a razão entre os recursos de Zaun e Piltover
    
    if razao >= 0.9:
        print("Zaun receberá uma bolada!!!")
    elif 0.8 <= razao < 0.9:
        print("Quase que Piltover ficava sem nada, pobrezinhos...")
    elif 0.7 <= razao < 0.8:
        print("O negócio vai ficar bom para Zaun hein.")
    elif 0.6 <= razao < 0.7:
        print("Parece que Zaun ainda precisa de ajuda.")
    elif 0.5 <= razao < 0.6:
        print("As coisas estão meio apertadas para Zaun.")
    else:
        print("A situação não está muito favorável para Zaun...")

total_recursos = int(input())
populacao_piltover = int(input())
populacao_zaun = int(input())
situacao_zaun = input()

# Cálculos da taxa e distribuição dos recursos
taxa = calcular_taxa(situacao_zaun)
recursos_piltover, recursos_zaun = distribuir_recursos(total_recursos, populacao_piltover, populacao_zaun, taxa)

print(f"Foi decidido que será {recursos_piltover:.1f} para Piltover e {recursos_zaun:.1f} para Zaun!")
mensagem(recursos_piltover, recursos_zaun)