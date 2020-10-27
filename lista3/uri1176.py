t = int(input())

def main():
	n = int(input())
	
	print(f'Fib({n}) = {fib(n)}')
    
def fib(n):
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    a = 0
    b = 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return c

for i in range(t):
	main()