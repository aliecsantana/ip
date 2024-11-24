d = int(input().strip())

if d <= 10:
    p = "Arthur"
elif d <= 30:
    p = "Luiz"
elif d <= 100:
    p = "Pedro"
else:
    p = "Nenhum"
    
print(p)