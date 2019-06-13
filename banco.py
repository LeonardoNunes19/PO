class Leilao:
    dicionario = {}
    def __init__(self,item,vmin):
        self.item = item
        self.vmin = vmin
        self.estado = 0



    def lance(self,nome,valor_lance):
        self.dicionario[nome] = valor_lance

    