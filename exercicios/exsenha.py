usuario = input('Digite o nome de usuário: ')
senha = input('Digite uma senha: ')


while(usuario == senha):
    senha = input('A senha deve ser diferente do nome de usuario. Digite outra senha: ')
print('Senha valida!')
