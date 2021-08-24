c1 = input('digite a primeira caracteristica: ')
c2 = input('digite a segunda caractristica: ')
c3 = input('digite a terceira caracteristica: ')

c1.lower(), c2.lower(), c3.lower()

if(c1 == 'vertebrado' and c2 == 'ave'):
    if(c3 == 'carnivoro'):
        print('aguia')
    elif(c3 == 'onivoro'):
        print('pomba')

elif(c1 == 'vertebrado' and c2 == 'mamifero'):
    if(c3 == 'onivoro'):
        print('homem')
    elif(c3 == 'herbivoro'):
        print('vaca')

if(c1 == 'invertebrado' and c2 == 'inseto'):
    if(c3 == 'hematofogo'):
        print('pulga')
    elif(c3 == 'herbivoro'):
        print('lagarta')

elif(c1 == 'invertebrado' and c2 == 'anelideo'):
    if(c3 == 'hematofago'):
        print('sanguessuga')
    elif(c3 == 'onivoro'):
        print('minhoca')

