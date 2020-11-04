count1 = 0
count2 = 0

gameNum = 1

while True:
	p = []
	
	n = int(input())
	if n == 0:
		break

	name1 = input()
	name2 = input()

	for i in range(n):
		p.append(input().split(' '))
		p[i] = [int(x) for x in p[i]]
	
	print(f'Teste {gameNum}')
	gameNum += 1

	for i in range(len(p)):
		if (p[i][0] + p[i][1]) % 2 == 0:
			print(name1)
		else:
			print(name2)

	print()		