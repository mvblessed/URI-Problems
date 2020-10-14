d = int(input())

y = d // 365
m = ((d % 365) // 30)
d = ((d % 365) % 30)

print(f'{y} ano(s)\n{m} mes(es)\n{d} dia(s)')
