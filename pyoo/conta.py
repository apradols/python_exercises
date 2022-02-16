

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}" .format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__cod_banco = "001"

    def extrato(self):
        print("O seu saldo é de {}" .format(self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor
        print("O valor {} foi depositado com sucesso!" .format(valor))

    def __pode_sacar(self, valor_saque):
        valor_disp = self.__saldo + self.__limite
        return valor_saque <= valor_disp 

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("O valor {} foi sacado com sucesso!" .format(valor))
        else:
            print("O valor {} passou do limite." .format(valor))
        
    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def cod_banco(self):
        return self.__cod_banco
