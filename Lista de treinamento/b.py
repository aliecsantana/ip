import math 

hogsmeade = (34, 220)
kakariko = (0, 0)
solitude = (140, 456)

x = int(input())
z = int(input())

def distancia(x1, z1, x2, z2):
    return math.sqrt((x1 - x2) ** 2 + (z1 - z2) ** 2)

h = distancia(x, z, hogsmeade[0], hogsmeade[1])
k = distancia(x, z, kakariko[0], kakariko[1])
s = distancia(x, z, solitude[0], solitude[1])

print(f'Distancia para Hogsmeade: {h:.2f}')
print(f'Distancia para Kakariko: {k:.2f}')
print(f'Distancia para Solitude: {s:.2f}')