orcamento_total = float(input())
numero_convidados = int(input())
local_festa = input()
cantor_convidado = input()
valor_euro = float(input())

orcamento_em_euros = orcamento_total / valor_euro

gastos_por_convidado = orcamento_em_euros / numero_convidados

# Se o orçamento em euros for menor que 1 milhão de euros
if orcamento_em_euros < 1000000:
    print(f"Acabei de receber a informação que o orçamento total da festa será {orcamento_em_euros:.2f} de euros. Poxa, com um orçamento desses vai ser difícil fazer a festa bombar! Vou divulgar essa informação pros sites de fofocas pra flopar a festa.")
# Se o orçamento em euros for igual ou maior que 1 milhão de euros
else:
    print(f"Poxa, esse cara tá podendo! Vai ser um festão, mas eu vou encontrar alguma coisa para que flope.")

# Se os gastos por convidado forem maiores ou iguais a 5000 euros
if gastos_por_convidado >= 5000:
    print("Eita, cancela o repasse da informação pros sites de fofocas! Gastando isso tudo por pessoa, vai continuar sendo um luxo.")
# Se os gastos por convidado forem menores que 5000 euros
else:
    print("Que vergonha, viu? O povo vai passar fome. Divulgue isso agora!")

# Se o local da festa for em um dos dois hotéis específicos
if local_festa == "Hotel Pera Palace" or local_festa == "Hotel Copacabana Palace":
    print("Eu conheço os donos e são meus amigos! Vou pedir pra recusarem a oferta!")
# Se o local da festa for em outro lugar
else:
    print("Poxa, não vou conseguir fazer nada!")

# Se o cantor convidado for Anitta ou Thiaguinho
if cantor_convidado == "Anitta" or cantor_convidado == "Thiaguinho":
    print(f"Duvido que aceite, Rodri fez isso pra me estressar! Claro que {cantor_convidado} não vai fazer isso comigo!")
# Se o cantor convidado for outro
else:
    print("Vou fazer uma oferta maior! Isso precisa flopar!")