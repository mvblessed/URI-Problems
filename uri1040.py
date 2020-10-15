n1, n2 ,n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1*2)+(n2*3)+(n3*4)+(n4))/10
print('Media: %.1f' % media)
if media < 5:
    print('Aluno reprovado.')
elif 5 <= media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    mediaf = (media+exame)/2
    print('Nota do exame: %.1f' % exame)
    if exame < 5:
        print('Aluno reprovado.')
        print('Media final: %.1f' % mediaf)
    else:
        print('Aluno aprovado.')
        print('Media final: %.1f' % mediaf)
else:
    print('Aluno aprovado.')
