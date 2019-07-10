from abc import ABC

class Banco:
    @staticmethod
    def transferencia(c1,c2,valor):
        if c1.getSaldo()-valor >= 0:
            c1.saque(valor)
            c2.deposito(valor)

class Conta:
    def __init__(self,numero,agencia):
        self.__nome_gerente = ''
        self.__nome_cliente = ''
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = 0

    def setNomeCliente(self,nome):
        self.__nome_cliente = nome.getNome()

    def getNomeCliente(self):
        return self.__nome_cliente

    def setNomeGerente(self,nome):
        self.__nome_gerente = nome.getNome()

    def getNomeGerente(self,nome):
        self.__nome_gerente = nome.getNome()

    def getAgencia(self):
        return self.__agencia

    def getNumero(self):
        return self.__numero

    def getSaldo(self):
        return self.__saldo

    def saque(self,valor):
        if (valor <= self.__saldo) and (valor >= 0):
            self.__saldo -= valor

    def deposito(self,valor):
        if valor >= 0:
            self.__saldo += valor

class Pessoa(ABC):
    def __init__(self, nome, ano_de_nascimento):
        self.__nome = nome
        self.__ano_de_nascimento = ano_de_nascimento
    
    def getNome(self):
        return self.__nome

    def getAnodeNascimento(self):
        return self.__ano_de_nascimento

class Cliente(Pessoa):
    def __init__(self, nome, ano_de_nascimento, uf):
        super().__init__(nome, ano_de_nascimento)
        self.__uf = uf
        self.contas = []
    
    def getUf(self):
        return self.__uf

    def addConta_cliente(self,x):
        self.contas.append(x)

    def montanteCliente(self):
        soma = 0
        for conta in self.contas:
            soma += conta.getSaldo()
        return soma

class Gerente(Pessoa):
    def __init__(self,nome,ano_de_nascimento,registro):
        super().__init__(nome,ano_de_nascimento)
        self.__registro = registro
        self.contas = []
    
    def getRegistro(self):
        return self.__registro

    def addConta_gerente(self,x):
        self.contas.append(x)

    def montanteGerente(self):
        soma = 0
        for conta in self.contas:
            soma += conta.getSaldo()
        return soma

c1 = Conta(999,9999)
c2 = Conta(888,8888)
c3 = Conta(777,7777)

p1 = Cliente('Leonardo','23/10/1999','SC')
p2 = Cliente('Thiago', '04/01/2002', 'SP')
p3 = Cliente('Matheus', '28/04/2000', 'SC')

g1 = Gerente('João Amoedo', '06/06/2022', '19102923')
g2 = Gerente('Sergio Cabral', '19/01/2000', '19156722')

g1.addConta_gerente(c1)
g2.addConta_gerente(c3)
g1.addConta_gerente(c2)

p1.addConta_cliente(c1)
p1.addConta_cliente(c3)
p2.addConta_cliente(c2)

c1.deposito(900)
c2.deposito(500)
c3.deposito(1000)
c1.saque(100)
c2.saque(200)
c3.saque(150)
c3.saque(100000)

print(p1.montanteCliente())
print(p2.montanteCliente())
print(p3.montanteCliente())

print(g1.montanteGerente())
print(g2.montanteGerente())

Banco.transferencia(c1,c2,100)
print(p1.montanteCliente())
print(p2.montanteCliente())
