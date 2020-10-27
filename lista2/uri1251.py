n = 0

while True:
	try:
		string = input()
		count = {}

		for s in string:
			if s in count: 
				count[s] += 1
			else:
				count[s] = 1
			
		od = sorted(count.items(), key = lambda kv:(kv[1], -ord(kv[0])))

		n += 1
		if n > 1: 
			print()

		for letter in od:
			print(f'{ord(letter[0])} {letter[1]}')
			
	except EOFError:
		break
