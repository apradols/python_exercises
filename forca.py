def jogo():
    print('Bem-vindo ao jogo de forca!')

    palavra = 'nana'

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input('Digite uma letra:')
        
        posicao = 0
        for letra in palavra:
            if(chute == letra):
                print('Letra {} na posição {}' .format(letra, posicao))
            posicao = posicao + 1
            
        print('jogando...')

    print('Fim de jogo!!!')

if(__name__ == "__main__"):
    jogo()