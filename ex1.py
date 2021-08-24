a = float(input('Digite um valor A: '))
b = float(input('Digite um valor B: '))
c = float(input('Digite um valor C: '))

delta = (b ** 2) - 4 * a * c

if(a == 0):
    print('O valor de A deve ser diferente de 0!')

elif(delta < 0):
    print('Impossível calcular')

else:
    x1 = (-b + delta ** (0.5)) / (2 * a)
    x2 = (-b - delta ** (0.5)) / (2 * a)
    print(' x1: {:.5f}, x2: {:.5f}' .format(x1, x2))
