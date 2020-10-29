numArr = []

for i in range(20):
  numArr.append(int(input()))

for index, num in enumerate(numArr[ : :-1]):
  print(f'N[{index}] = {num}')