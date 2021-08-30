def jogo():
    print('Bem-vindo ao jogo de forca!')

    palavra = 'nana'.upper()
    letras_certas = ['_', '_', '_', '_']

    enforcou = False
    acertou = False
    erro = 0

    print(letras_certas)

    while(not enforcou and not acertou):

        chute = input('Digite uma letra:')
        chute = chute.strip().upper()

        if(chute in palavra):
            posicao = 0
            for letra in palavra:
                if(chute == letra):
                    letras_certas[posicao] = letra
                posicao += 1

        else:
            erro += 1

        enforcou = erro == 5
        acertou = '_' not in letras_certas
        print(letras_certas)    
        
    if(acertou):
        print("Você ganhou")
    else:
        print('Você perdeu')
    print('Fim de jogo!!!')

if(__name__ == "__main__"):
    jogo()
