N, M = int(input().split('.'))

# Notas
nCem  = N // 100
nCinq = (N % 100) // 50
nVint = ((N % 100) % 50) // 20
nDez  = (((N % 100) % 50) % 20) // 10
nCinc = ((((N % 100) % 50) % 20 ) % 10) // 5
nDois = (((((N % 100) % 50) % 20) % 10) % 5) // 2

# Moedas
M *= 100
mUm   = N // 100
mCinq = (N % 100) // 50
mVint = ((N % 100) % 50) // 20
mDez  = (((N % 100) % 50) % 20) // 10
mCinc = ((((N % 100) % 50) % 20 ) % 10) // 5
mDois = (((((M % 100) % 50) % 20) % 10) % 5) // 2

print('NOTAS:')
print(f'{nCem} nota(s) de R$ 100,00')
print(f'{nCinq} nota(s) de R$ 50,00')
print(f'{nVint} nota(s) de R$ 20,00')
print(f'{nDez} nota(s) de R$ 10,00')
print(f'{nCinc} nota(s) de R$ 5,00')
print(f'{nDois} nota(s) de R$ 2,00')

print('MOEDAS:')
print(f'{mUm} moedas(s) de R$ 100,00')
print(f'{mCinq} moedas(s) de R$ 50,00')
print(f'{mVint} moedas(s) de R$ 20,00')
print(f'{mDez} moedas(s) de R$ 10,00')
print(f'{mCinc} moedas(s) de R$ 5,00')
print(f'{mDois} moedas(s) de R$ 2,00')

 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
