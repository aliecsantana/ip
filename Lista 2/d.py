qtd_folhas = int(input())
populacao = int(input())
altura_arvore = int(input())

if altura_arvore < 2:
    print("Isso não é uma árvore, é um arbusto!")
else:
    qtd_folhas_necessarias = altura_arvore * (altura_arvore + 1)
    # Verifica se é possível criar pelo menos uma árvore
    if qtd_folhas_necessarias > qtd_folhas:
        print("Infelizmente não poderemos comemorar o Natal esse ano, não conseguimos fazer uma única árvore!")
    # Exibe a árvore
    else:
        for camada in range(altura_arvore + 1):
            print("\u2800" * (altura_arvore - camada), end="")
            # Imprime a estrela
            if camada == 0:
                print("\u2800", end="")
                print("*")
            # Imprime as folhas
            else:
                print("\u2800", end="")
                print("+" * camada, end="")
                print("\u2800", end="")
                print("+" * camada)
        # Verifica se há folhas suficientes para fazer árvores para toda a população
        qtd_folhas_necessarias_populacao = qtd_folhas_necessarias * populacao
        if qtd_folhas_necessarias_populacao <= qtd_folhas:
            print("O Grinch não conseguiu estragar o Natal dessa vez!")
        else:
            print("Essa árvore está muito grande, dessa forma não conseguiremos entregar para a cidade toda")