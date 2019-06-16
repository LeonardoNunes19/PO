class Leilao:
    lances = []
    dicionario = {}
    def __init__(self,item,vmin):
        self.item = item
        self.vmin = vmin
        self.estado = 0

    def iniciarLeilao(self):
        self.estado = 1
    
    def encerrarLeilao(self):
        self.estado = 2

    def lance(self,nome,valor_lance):
        if self.estado == 0:
            pass
        else:
            if self.estado == 1 and valor_lance >= self.vmin:
                self.dicionario[nome] = valor_lance
                self.lances.append(valor_lance)

    def getLances(self):
        print(self.lances)

    def getNomeMaiorLance(self):
        if self.estado == 0:
            pass
        else:
            print(max(self.dicionario, key=self.dicionario.get))

    def getQtdeLances(self):
        if self.estado == 0:
            pass
        else:
            print(len(self.lances))

    def getValorMaiorLance(self):
        if self.estado == 0:
            pass
        else:
            self.maior = max(self.lances)
            print(self.maior)

    def getMediaLances(self):
        if self.estado == 0:
            pass
        else:
            print((sum(self.lances)) / (len(self.lances)))


print(lances)
l1 = Leilao('carro',12200)
l1.lance('Leonardo', 1000000000)
l1.getValorMaiorLance()
# leilão ainda não inicializado
l1.iniciarLeilao()
l1.lance('Leonardo', 12200)
l1.lance('Lucas', 12201)
l1.lance('fernando',12199)
l1.encerrarLeilao()
l1.getNomeMaiorLance()
l1.getMediaLances()
l1.lance('sorocaba',10000000000000000000000000000000)
l1.getMediaLances()

l2 = Leilao("Silvio Santos's House",1000000000)
l2.iniciarLeilao()
l2.lance('Eique Batisto',100)
l2.lance('Teago Iorqui',9000000000)
l2.lance('Rei do Camarote',10000000000)
l2.lance('Chimbinha',10000500000)
l2.lance('Silvio Santos Filho', 1000000000)
l2.getLances()
l2.getQtdeLances()
