# Peaks and Valleys

landscape = []
def main():
	n = int(input())

	h = input().split(' ')
	
	if isNlogony(h):
		print(1)
	else:
		print(0)


def isNlogony(l):
	if len(l) == 2:
		return int(l[0]) != int(l[1])

	for i in range(len(l) - 2):
			if (int(l[i]) < int(l[i + 1])) and (int(l[i + 1]) < int(l[i + 2])):
					return False
			if (int(l[i]) > int(l[i + 1])) and (int(l[i + 1]) > int(l[i + 2])):
					return False
			if (int(l[i]) == int(l[i + 1])) or (int(l[i + 1]) == int(l[i + 2])):
					return False
	return True


main()