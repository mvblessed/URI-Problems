coord1 = input().split(' ')
coord2 = input().split(' ')

x1 = float(coord1[0])
y1 = float(coord1[1])
x2 = float(coord2[0])
y2 = float(coord2[1])

d = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

print(f'{d:.4f}')
