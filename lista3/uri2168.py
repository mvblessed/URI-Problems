# Twilight at Portland

cams = []

n = int(input())

for i in range(n + 1):
	cams.append(input().split(' '))
	cams[i] = [ int(n) for n in cams[i] ]

for i in range(n):
	for j in range(n):
		if cams[i][j] + cams[i][j + 1] + cams[i + 1][j] + cams[i + 1][j + 1] < 2:
			print('U', end='')
		else:
			print('S', end='')
	print()