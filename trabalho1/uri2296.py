minEsforco = 100000

h = []

n = int(input())

for i in range(n):
	h = input().split(' ')
	h = [int(m) for m in h]

	esforco1 = 0
	esforco2 = 0

	for j in range(1, h[0]):
		if h[j] > h[j + 1]:
			esforco1 += h[j] - h[j + 1]
		else:
			esforco2 += h[j + 1] - h[j]
	
	if esforco1 > esforco2:
		esforco1 = esforco2

	if esforco1 < minEsforco:
		minEsforco = esforco1
		melhorTrilha = i + 1

print(melhorTrilha)