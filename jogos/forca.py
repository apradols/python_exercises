def jogo():
    print('Bem-vindo ao jogo de forca!')

    palavra = 'nana'
    letras_certas = ['_', '_', '_', '_']

    enforcou = False
    acertou = False
    erro = 0

    print(letras_certas)

    while(not enforcou and not acertou):

        chute = input('Digite uma letra:')
        chute = chute.strip()

        if(chute in palavra):
            posicao = 0
            for letra in palavra:
                if(chute.upper() == letra.upper()):
                    letras_certas[posicao] = letra
                posicao = posicao + 1

        else:
            erro = erro + 1

        enforcou = erro == 5

        print(letras_certas)    
        #print('jogando...')

    print('Fim de jogo!!!')

if(__name__ == "__main__"):
    jogo()
