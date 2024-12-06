taxa_fixa_empresa_1 = float(input())
taxa_variavel_empresa_1 = float(input())
taxa_fixa_empresa_2 = float(input())
taxa_variavel_empresa_2 = float(input())

empresa_mais_barata = ""
empresa_x = ""
empresa_y = ""

# Verifica se a empresa 1 é sempre a mais barata
if taxa_variavel_empresa_1 < taxa_variavel_empresa_2 and taxa_fixa_empresa_1 < taxa_fixa_empresa_2:
    empresa_mais_barata = "Empresa 1"
    print(f"A {empresa_mais_barata} é sempre a melhor opção!")

# Se a empresa 2 é sempre a mais barata
elif taxa_variavel_empresa_2 < taxa_variavel_empresa_1 and taxa_fixa_empresa_2 < taxa_fixa_empresa_1:
    empresa_mais_barata = "Empresa 2"
    print(f"A {empresa_mais_barata} é sempre a melhor opção!")

# Se ambas as empresas possuem sempre o mesmo preço
elif taxa_fixa_empresa_1 == taxa_fixa_empresa_2 and taxa_variavel_empresa_1 == taxa_variavel_empresa_2:
    print("As duas empresas possuem o mesmo preço sempre!")

# Se existirem intervalos de distância para os quais empresas diferentes são a melhor opção
else:
    if taxa_variavel_empresa_1 < taxa_variavel_empresa_2 and taxa_fixa_empresa_1 > taxa_fixa_empresa_2:
        k = (taxa_fixa_empresa_1 - taxa_fixa_empresa_2) / (taxa_variavel_empresa_2 - taxa_variavel_empresa_1)
        empresa_x = "Empresa 2"
        empresa_y = "Empresa 1"  

    elif taxa_variavel_empresa_1 > taxa_variavel_empresa_2 and taxa_fixa_empresa_1 < taxa_fixa_empresa_2:
        k = (taxa_fixa_empresa_2 - taxa_fixa_empresa_1) / (taxa_variavel_empresa_1 - taxa_variavel_empresa_2)
        empresa_x = "Empresa 1"
        empresa_y = "Empresa 2"

    print(f"{empresa_x} é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a {empresa_y} é mais barata para distâncias maiores que {k:.2f} km.")
