numero = float(input('Digite uma nota entre 0 e 10: '))

while(numero < 0) or (numero > 10):
    numero = float(input('Continue digitando uma nota! '))
print('nota valida')
