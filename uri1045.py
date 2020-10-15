num = input()
num = sorted(num.split(), key = float, reverse=True)
a, b, c = num
a = float(a)
b = float(b)
c = float(c)
if a>=b+c:
    print('NAO FORMA TRIANGULO')
elif (a**2)==(b**2)+(c**2):
   print('TRIANGULO RETANGULO')
elif (a**2)>(b**2)+(c**2):
   print('TRIANGULO OBTUSANGULO')
   if a==b or a==c or b==c:
       print('TRIANGULO ISOSCELES')
elif (a**2)<(b**2)+(c**2):
   print('TRIANGULO ACUTANGULO')
   if a==b==c:
       print('TRIANGULO EQUILATERO')
   elif a==b or a==c or b==c:
       print('TRIANGULO ISOSCELES')
