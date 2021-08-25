
qntnome = int(input('digite um numero de 2 a 10: '))

nomes = []


#pra pegar varias variaveis de uma vez
for _ in range(qntnome):
    nome = input("Digite os nomes: ")
    nomes.append(nome)

lista_nome = nomes

lista = sorted(lista_nome, key=len )

print(lista)
