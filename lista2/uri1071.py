x, y = map(int, sorted([input() for _ in range(2)], key = int))
soma = 0
for i in range(x+1, y):
    if i%2 == 0:
        pass
    else:
        soma = soma+i
    i += 1
print(soma)
