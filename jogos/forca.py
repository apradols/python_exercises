def jogo():
    print('Bem-vindo ao jogo de forca!')

    palavra = 'nana'
    letras_certas = ['_', '_', '_', '_']

    enforcou = False
    acertou = False

    print(letras_certas)

    while(not enforcou and not acertou):

        chute = input('Digite uma letra:')
        chute = chute.strip()

        posicao = 0
        for letra in palavra:
            if(chute.upper() == letra.upper()):
               letras_certas[posicao] = letra
            posicao = posicao + 1

        print(letras_certas)    
        #print('jogando...')

    print('Fim de jogo!!!')

if(__name__ == "__main__"):
    jogo()

    #01:23