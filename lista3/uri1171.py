n = int(input())
listOfNums = []
largestNum = 0

for i in range(n):
  listOfNums.append(int(input()))

for i in listOfNums:
  if i >= largestNum:
    largestNum = i
  
for i in range(largestNum + 1):
  count = 0

  for j in listOfNums:
    if j == i:
      count += 1
  if i in listOfNums:
    print(f'{i} aparece {count} vez(es)')