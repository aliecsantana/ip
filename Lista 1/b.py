plateia1 = str(input())
plateia2 = str(input())
vencedor = str(input())

# Se o vencedor for Palé
if vencedor == "Palé":
    print("Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!")
# Se Gavião Bonito e Ronaldinho Paulista estiverem na plateia
elif (plateia1 == "Gavião Bonito" and plateia2 == "Ronaldinho Paulista") or (plateia1 == "Ronaldinho Paulista" and plateia2 == "Gavião Bonito"):
    print("Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!")
# Se o vencedor for Mãodona
elif vencedor == "Mãodona":
  # Se apenas Gavião Bonito estiver na plateia
    if plateia1 == "Gavião Bonito" or plateia2 == "Gavião Bonito":
        if plateia1 != "Ronaldinho Paulista" and plateia2 != "Ronaldinho Paulista":
            print("Gavião soltou seu grito, mas não foi o suficiente para dar o troféu ao rei do fut. Triste dia para o futebol mundial…")
    # Se apenas Ronaldinho Paulista estiver na plateia
    elif plateia1 == "Ronaldinho Paulista" or plateia2 == "Ronaldinho Paulista":
        print("Paulista subiu no palco sozinho e ninguém sabe o porquê. Mais um momento aleatório e mais um dia triste para o brasileiro…")
    # Se nenhum dos amigos de Palé estiver na plateia
    else:
        print("PERDEMOS! O futebol foi roubado e não há mais chance de volta por enquanto.")
# Se o vencedor não for nem Palé nem Mãodona
else:
    print("Não foi dessa vez, mas pelo menos não perdemos a nossa dignidade.")