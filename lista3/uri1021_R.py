# solucao do Rafael

notas, moedas = map(int, input().split("."))
valores = [100, 50, 20, 10, 5, 2, 50, 25, 10, 5, 1]
print('NOTAS:')
for i in range(6):
    nota, notas = divmod(notas, valores[i])
    print('%d nota(s) de R$ %d.00' %(nota, valores[i]))
print('MOEDAS:\n',notas,' moeda(s) de R$ 1.00',sep = '')
for i in range(6, 11):
    moeda, moedas = divmod(moedas, valores[i])
    print('%d moeda(s) de R$ 0.%02d' %(moeda, valores[i]))
