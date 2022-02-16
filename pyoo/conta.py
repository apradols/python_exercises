

class Conta:

    #atributos
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #metodos
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

    #propriedade
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
   
    #metodos estaticos 
    @staticmethod
    def cod_banco():
        return "001"

    @staticmethod
    def cod_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}
