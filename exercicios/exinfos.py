nome = input('Nome: ')
idade = int(input('Idade: '))
salario = float(input('Salário: '))
sexo = input('Sexo: (f) ou (m): ')
estcivil = input ('Estado Civil: (s), (c), (v) ou (d): ')
genero = input('Gênero: (c), (t) ou (n): ')
sexual = input('Sexualidade: (ht), (hm), (b) ou (p): ')

while len(nome) <= 3:
    nome = input('Seu nome deve ter mais que 3 caracteres. ')
    
while(idade <= 0) or (idade >= 150):
    idade = int(input('Sua idade deve estar entre 0 e 150. '))

while(salario < 0):
    salario = float(input('Seu salário deve sera maior que 0. '))

while(sexo != 'f') and (sexo != 'm'):
    sexo = input('Seu sexo deveria ser f ou m. ')

while(estcivil != 's') and (estcivil != 'c') and (estcivil != 'v') and (estcivil != 'd'):
    estcivil = input('Seu estado civil deve ser s, c, v ou d. ')

while(genero != 'c') and (genero != 't') and (genero != 'n') and (genero != 'a'):
    genero = input('Seu genero deve ser cis(c), trans(t), não-binário(n) ou angênero (a). ')

while(sexual != 'ht') and (sexual != 'hm') and (sexual != 'b') and (sexual != 'p'):
    sexual = input('Seu genero deve ser hetero(ht), homo(hm), bi(b) ou pan(p). ')

