class Quarto:
    def __init__(self):
        self.moveis = []
    def addMovel(self,movel):
        self.moveis.append(movel)
    def printMoveis(self):
        for movel in self.moveis:
            print(movel.description)

class Movel:
    def __init__(self,description):
        self.description = description

a = Quarto()
m1 = Movel("Cama")
m2 = Movel("Churrasqueira Eletrica")
a.addMovel(m1)
a.addMovel(m2)
a.printMoveis()

'''AGREGAÇÃO: 2. é uma composição fraca, onde as partes podem existir
sem o todo e isso faz sentido, 2.1 além de um objeto parte poder estar
presente em vários objetos todo

EX: uma sala pode existir sem uma poltrona e vice e versa por 2.
uma poltrona pode existir tanto em uma sala quando em um quarto por 2.1'''
