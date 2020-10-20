x = int(input())
y = int(input())

oddSum = 0

for i in range(y + 1, x):
	if i % 2 != 0:
		oddSum += i

print(oddSum)
