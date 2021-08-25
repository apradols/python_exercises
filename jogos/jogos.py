import forca
import adivinhacao

def escolhe_jogo():
    print('Escolha um dos jogos!')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual o jogo? '))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogo()
    elif(jogo == 2):
        print('Jogando adivinhação')
        adivinhacao.jogo()

if(__name__ == "__main__"):
    escolhe_jogo()

