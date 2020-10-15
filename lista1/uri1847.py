a, b, c = list(map(int, input().split()))
if a > b and (b < c or b == c):
  print(':)')
elif a < b and (b > c or b == c):
  print(':(')
elif a < b < c and (b-a > c-b):
  print(':(')
elif a < b < c and ((b - a == c - b) or (b - a < c - b)):
  print(':)')
elif a > b > c and (a - b > b - c):
  print(':)')
elif a > b > c and ((a - b == b - c) or (a - b < b - c)):
  print(':(')
elif a == b and b > c:
  print(':(')
elif a == b and b < c:
  print(':)')
elif a == b == c:
  print(':(')
