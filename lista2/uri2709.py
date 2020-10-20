while True:
	try: 
		M = int(input())

		coins = []
		total = 0
		div   = 0
		
		# Get input and append to a list
		for i in range(M):
			coins.append(int(input()))
		
		N = int(input())
			
		# Add coin values with the given step		
		for i in range(0, len(coins), N):
			total += coins[len(coins) - 1 - i]
		
		# Check if total is a prime number
		for i in range(2, int(total ** 0.5) + 1):
			if total % i == 0:
				div += 1

		if div == 0 and total != 1:
			print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
		else: 
			print('Bad boy! I’ll hit you.')
			
	except EOFError:
		break
