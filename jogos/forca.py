import random

def jogo():

    print_inicio()
    palavra = palavra_secreta_random()
    letras_certas = ['_' for letra in palavra]
    print(letras_certas)

    enforcou = False
    acertou = False
    erro = 0

    while(not enforcou and not acertou):

        chute = pedir_chute()

        if(chute in palavra):
            posicao = 0
            for letra in palavra:
                if(chute == letra):
                    letras_certas[posicao] = letra
                posicao += 1
        else:
            erro += 1
            desenha_forca(erro)

        enforcou = erro == 7
        acertou = '_' not in letras_certas
        print(letras_certas)

    if(acertou):
        print_acerto()
    else:
        print_perdeu(palavra)
        
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

def pedir_chute():
    chute = input('Digite uma letra:')
    chute = chute.strip().upper()
    return chute

def print_acerto():
    print("Você ganhou")

def print_perdeu(palavra):
    print('Você perdeu')
    print('A palavra secreta era:', palavra)
    print('Fim de jogo!!!')
        
def desenha_forca(erro):
    print("  _______     ")
    print(" |/      |    ")

    if(erro == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erro == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erro == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erro == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erro == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erro == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erro == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogo()

#43:57