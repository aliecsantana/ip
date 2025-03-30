# Recebe os nomes dos alunos na fila e os separa usando o hífen
alunos_fila = input().split('-')

# Cria uma cópia da fila inicial para manipulação sem alterar a lista original
fila_atual = alunos_fila.copy()

# Inicializa a lista de contagem de teleportes para cada aluno
contagem_teleportes = [0] * len(alunos_fila)

realizar_troca = True

while realizar_troca:
    # Recebe a entrada de troca de nomes
    entrada_troca = input()
    
    if entrada_troca == "Acabou!":
        realizar_troca = False
    else:
        nomes_dupla = entrada_troca.split("-") # Separa os nomes da troca
        
        # Verifica se pelo menos um dos nomes não está na fila
        if nomes_dupla[0] not in alunos_fila or nomes_dupla[1] not in alunos_fila:
            print("Essa dupla não esta na lista!")
        else:
            # Encontra os índices dos alunos a serem trocados de lugar
            idx1 = fila_atual.index(nomes_dupla[0])
            idx2 = fila_atual.index(nomes_dupla[1])
            
            # Realiza a troca de posições na fila
            fila_atual[idx1], fila_atual[idx2] = fila_atual[idx2], fila_atual[idx1]
            
            # Atualiza a contagem de teleportes dos alunos
            contagem_teleportes[alunos_fila.index(nomes_dupla[0])] += 1
            contagem_teleportes[alunos_fila.index(nomes_dupla[1])] += 1

print("Fila do almoço:")
for aluno in fila_atual:
    # Imprime o nome do aluno e o número de teleportes
    print(f"{aluno}: {contagem_teleportes[alunos_fila.index(aluno)]} {"teleporte!" if contagem_teleportes[alunos_fila.index(aluno)] == 1 else "teleportes!"}")