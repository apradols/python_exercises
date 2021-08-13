n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = float(n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10
print('Média: ', media)

if(media >= 7.0):
    print('Aluno aprovado.')

elif(media >= 5.0 < 6.9):
    print('Aluno em exame.')

else:
    print('Aluno reprovado')

