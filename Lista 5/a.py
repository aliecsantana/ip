def pertence_penguinacci(numero, a=0, b=1):
    # Se o número for igual a "a" ou "b", que são os dois primeiros números de Fibonacci, retorna True
    if numero == a or numero == b:
        return True
    # Se o número "b" for maior que o número procurado, significa que não está na sequência
    if b > numero:
        return False
    # Chama a função recursivamente com os próximos dois números da sequência de Fibonacci
    return pertence_penguinacci(numero, b, a + b)

def verifica_penguinacci():
    n = int(input())
    numeros_penguinacci = []

    for i in range(n):
        m = int(input())
        if pertence_penguinacci(m):
            numeros_penguinacci.append(m)

    print(f"Contei um total de {len(numeros_penguinacci)} números que estão na sequência de penguinacci!")

    if len(numeros_penguinacci) == n:
        print("Boa, Paulo! Todos esses números fazem parte da sequência de penguinacci.")
    elif len(numeros_penguinacci) > 0:
        numeros_penguinacci.sort() # Ordena a lista de números válidos em ordem crescente
        print("Eita, nem todos que você falou fazem parte da sequência de penguinacci. Os que fazem parte são:")
        for j in range(len(numeros_penguinacci)):
            # Se for o último número da lista, imprime sem a vírgula
            if j == len(numeros_penguinacci) - 1:
                print(numeros_penguinacci[j])
            # Caso contrário, imprime com a vírgula
            else:
                print(numeros_penguinacci[j], end=", ")
    else:
        print("Acho que é melhor revisar a teoria um pouco...")

verifica_penguinacci()