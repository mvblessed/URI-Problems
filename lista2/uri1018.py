N = int(input())

cem  = N // 100
cinq = (N % 100) // 50
vint = ((N % 100) % 50) // 20
dez  = (((N % 100) % 50) % 20) // 10
cinc = ((((N % 100) % 50) % 20 ) % 10) // 5
dois = (((((N % 100) % 50) % 20) % 10) % 5) // 2
um   = ((((((N % 100) % 50) % 20) % 10) % 5) % 2) // 1

print(N)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinq} nota(s) de R$ 50,00')
print(f'{vint} nota(s) de R$ 20,00')
print(f'{cinc} nota(s) de R$ 10,00')
print(f'{dois} nota(s) de R$ 5,00')
print(f'{um} nota(s) de R$ 1,00')

