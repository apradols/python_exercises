import random

def jogo():

    print('Bem-vindo ao jogo de adivinhação')

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print('Escolha um nível dificuldade!')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, tentativas))

        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou: ', chute)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou, o seu chute foi maior que o numero secreto')
            elif(menor):
                print('Você errou, o seu chute foi menor que o numero secreto')
            pont_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pont_perdidos


    print('Fim de jogo!!!')
    
if(__name__ == "__main__"):
    jogo()