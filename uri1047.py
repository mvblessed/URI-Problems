h1, m1, h2, m2 = list(map(int, input().split()))
if h1 < h2:
    horas = h2-h1
elif h1==h2 and m1 < m2:
    horas = 0
else:
    horas = 24-h1+h2
if m2 < m1:
    minutos = 60-(m1-m2)
    horas = horas-1
else:
    minutos = m2-m1
print('O JOGO DUROU',horas,'HORA(S) E',minutos,'MINUTO(S)')
