a = int(input())
l = int(input())
p = int(input()) 
h = int(input())

total_a = a * h
total_l = l * h
total_p = p * h

def x(a, b):
    return (a + b + abs(a-b)) // 2

y = x(x(total_a, total_l), total_p)

print(y)