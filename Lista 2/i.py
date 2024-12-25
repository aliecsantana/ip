# Recebe a altura de cada triângulo da estrela
n = int(input())

# Gera o triângulo superior
for linha in range(n - 1):
    # Calcula a quantidade de espaços antes da primeira estrela
    espacos = '\u2800' * (n - linha - 1)
    # Calcula as estrelas e os espaços entre elas
    if linha == 0:
        estrelas = '*'
    else:
        estrelas = '*' + '\u2800' * (2 * linha - 1) + '*'
    print(espacos + estrelas + espacos)

# Imprime a base que une os dois triângulos
print((('*' + '\u2800') * ( n -1 )) + '*')

# Gera o triângulo inferior
for linha in range(n - 2, -1, -1):
    # Calcula a quantidade de espaços antes da primeira estrela
    espacos = '\u2800' * (n - linha - 1)
    # Calcula as estrelas e os espaços entre elas
    if linha == 0:
        estrelas = '*'
    else:
        estrelas = '*' + '\u2800' * (2 * linha - 1) + '*'
    print(espacos + estrelas + espacos)