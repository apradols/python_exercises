n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if(n1 > n2 and n3):
    print('Número 1, {} é o maior número.' .format(n1))

elif(n2 > n1 and n3):
    print('Número 2, {} é o maior número.' .format(n2))

else:
    print('Número 3, {} é o maior número.' .format(n3))

