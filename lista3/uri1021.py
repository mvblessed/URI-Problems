# Essa questao tava na lista 2 tambem
# Minha resolucao

N, M = input().split('.')

N = int(N)
M = int(M)

# Notas
nCem  = N // 100
nCinq = (N % 100) // 50
nVint = ((N % 100) % 50) // 20
nDez  = (((N % 100) % 50) % 20) // 10
nCinc = ((((N % 100) % 50) % 20 ) % 10) // 5
nDois = (((((N % 100) % 50) % 20) % 10) % 5) // 2
nUm   = ((((((N % 100) % 50) % 20) % 10) % 5) % 2) // 1

# Moedas
mCinq = (M % 100) // 50
mVint = ((M % 100) % 50) // 25
mDez  = (((M % 100) % 50) % 25) // 10
mCinc = ((((M % 100) % 50) % 25 ) % 10) // 5
mUm   = (((((M % 100) % 50) % 25) % 10) % 5) // 1

print('NOTAS:')
print(f'{nCem} nota(s) de R$ 100.00')
print(f'{nCinq} nota(s) de R$ 50.00')
print(f'{nVint} nota(s) de R$ 20.00')
print(f'{nDez} nota(s) de R$ 10.00')
print(f'{nCinc} nota(s) de R$ 5.00')
print(f'{nDois} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{nUm} moeda(s) de R$ 1.00')
print(f'{mCinq} moeda(s) de R$ 0.50')
print(f'{mVint} moeda(s) de R$ 0.25')
print(f'{mDez} moeda(s) de R$ 0.10')
print(f'{mCinc} moeda(s) de R$ 0.05')
print(f'{mUm} moeda(s) de R$ 0.01')

