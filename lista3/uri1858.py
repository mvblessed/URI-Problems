n = int(input())

numList = [int(num) for num in input().split(' ')]

smallest = numList[0]
index = 0

for i, j in enumerate(numList):
  if j < smallest:
    smallest = j
    index = i

print(index + 1) 
  