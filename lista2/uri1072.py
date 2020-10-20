N = int(input())

ins = 0
out = 0

for i in range(N):
	X = int(input())
	
	if X >= 10 and X <= 20:
		ins += 1
	else: 
		out += 1
		
print(f'{ins} in\n{out} out')

