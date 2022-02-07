import random

def jogo():

    print_inicio()

    palavra = palavra_secreta_random()

    letras_certas = ['_' for letra in palavra]

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

def print_inicio():
    print('Bem-vindo ao jogo de forca!')

def palavra_secreta_random():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    num = random.randrange(0, len(palavras))
    palavra = palavras[num].upper()
    return palavra
