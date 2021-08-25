print('CÓDIGO----------PRODUTO------------PREÇO')
print('----------------------------------------')
print('1        Cachorro Quente         R$ 4.00')
print('2        X-Salada                R$ 4.50')
print('3        X-Bacon                 R$ 5.00')
print('4        Torranda Simples        R$ 2.00')
print('5        Refrigerante            R$ 1.50')

codigo = int(input('Digite código do produto desejado! '))
quant = int(input('Digite a quantidade do produto desejada! '))

if(codigo == 1):
    dogao = float(quant * 4.00)
    print('Total: R$ {:.2f} ' .format(dogao))

elif(codigo == 2):
    xsalada = float(quant * 4.50)
    print('Total: R$ {:.2f}' .format(xsalada))

elif(codigo == 3):
    xbacon = float(quant * 5.00)
    print('Total: R$ {:.2f}' .format(xbacon))

elif(codigo == 4):
    torrada = float(quant * 2.00)
    print('Total: R$ {:.2f}' .format(torrada))

elif(codigo == 5):
    refri = float(quant * 1.50)
    print('Total: R$ {:.2f}'. format(refri))

else:
    print('Escolha um produto!')

