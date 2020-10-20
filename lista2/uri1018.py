notas = int(input())
valores = [100, 50, 20, 10, 5, 2, 1]
print(notas)
for i in range(7):
    nota, notas = divmod(notas, valores[i])
    print('%d nota(s) de R$ %d,00' %(nota, valores[i]))
