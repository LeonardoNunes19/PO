class Conta:
    def __init__(self,numero,agencia,c,g):
        self.numero = numero
        self.agencia = agencia
        self.c = c
        self.g = g
        self.saldo = 0
        self.c.addContas(self)
        self.g.addContas(self)

        