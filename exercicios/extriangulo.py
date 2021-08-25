a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if(a >= b+c):
    print('Nao forma triangulo')

elif(a**2 == (b**2 + c**2)):
    print('Triangulo retangulo')

elif(a**2 > (b**2 + c**2)):
    print('Triangulo obtusangulo')

elif(a**2 < (b**2 + c**2)):
    print('Triangulo acutangulo')

if(a == b and c):
    print('Triangulo equilatero')

elif(a == b or c):
    print('Triangulo isosceles')
