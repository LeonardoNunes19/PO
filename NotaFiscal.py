''' EXEMPLO DE COMPOSIÇÃO: O objeto parte (ItemNotaFiscal) pertece
somente ao objeto todo (NotaFiscal) e NotaFiscal não faz sentido
de existir sem ItemNotaFiscal'''

class NotaFiscal:
    def __init__(self):
        self.items = []
    def addItem(self,prod,qtde,vl):
        self.items.append(ItemNotaFiscal(prod,qtde,vl))
    def getTotal(self):
        tot = 0
        for item in self.items:
            tot += item.total
        return tot

class ItemNotaFiscal:
    def __init__(self,prod,qtde,vl):
        self.prod = prod
        self.qtde = qtde
        self.vl = vl
        self.total = qtde * vl

a = NotaFiscal()
a.addItem("11222222", 2, 1.5)
a.addItem("4324321", 3, 2)
print(a.getTotal())

''' COMPOSIÇÃO: 1. quando o objeto (todo) não pode existir sem possuir
outros objetos (partes) e vice versa

1.1 neste caso o objeto todo é responsável por criar objetos parte e um
objeto parte não pode estar presente em outro objeto todo.

EX: não faz sentido o coração do homem de ferro sem o homem de ferro
e vice e versa, senão o tony morre :/ (dnv) por 1.
assim como o coração do homem de ferro não pode ir para o do Thor, Hulk
... por 1.1'''
