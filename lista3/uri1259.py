n = int(input())

oddList  = []
evenList = []

for i in range(n):
  num = int(input())
 
  if num % 2 == 0:
    evenList.append(num)
  else:
    oddList.append(num)

evenList.sort()
oddList.sort()

evenList.extend(oddList[ : : -1])

for i in evenList:
  print(i)