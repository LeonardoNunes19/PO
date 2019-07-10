class Biblioteca:
    def __init__(self,nome,capacidade):
        self.__nome_bib = nome
        self.__capacidade_bib = capacidade
        self.__lista_bibliotecarios_bib = []
        self.__lista_prateleiras_bib = []

    def getNomeBib(self):
        return self.__nome_bib

    def getCapacidadeBib(self):
        return self.__capacidade_bib

    def getBibliotecariosBib(self):
        return self.__lista_bibliotecarios_bib

    def addPrateleiraBib(self,prateleira):
        self.__lista_prateleiras_bib.append(prateleira)

    def getLivroMaisCaroBib(self):
        dicionario = {}
        lista = []
        for x in self.__lista_prateleiras_bib:
            lista.append(x.getLivroMaisCaroPrateleira())
            dicionario[x.getLivroMaisCaroPrateleira()] = x.getTituloLivro()
        valor = max(lista)
        print(dicionario[valor])

    
    def getPrateleirasBib(self):
        return self.__lista_prateleiras_bib
    

class Bibliotecario:
    def __init__(self,nome,idade,data_admissao,salario):
        self.__nome_bibiotecario = nome
        self.__idade_bibliotecario = idade
        self.__data_admissao_bibliotecario = data_admissao
        self._salario_bibliotecario = salario

    def getNomeBibliotecario(self):
        return self.__nome_bibiotecario

    def getIdadeBibliotecario(self):
        return self.__idade_bibliotecario

    def getDataAdmissaoBibliotecario(self):
        return self.__data_admissao_bibliotecario

    def getSalarioBibliotecario(self):
        return self._salario_bibliotecario

class Prateleira:
    def __init__(self,categoria,identificador):
        self.__categoria_prateleira = categoria
        self.__identificador_prateleira = identificador
        self.__lista_livros_prateleira = []

    def getCategoriaPrateleira(self):
        return self.__categoria_prateleira

    def getIdentificadorPrateleira(self):
        return self.__identificador_prateleira

    def addLivroPrateleira(self,livro):
        if self.getCategoriaPrateleira() == livro.getCategoriaLivro():
                self.__lista_livros_prateleira.append(livro)
    
    def getListaLivrosPrateleira(self,indice):
        return self.__lista_livros_prateleira[indice].getTituloLivro()

    def getQtdeLivrosPrateleira(self):
        return len(self.__lista_livros_prateleira)

    def getNomeLivroMaisCaroPrateleira(self):
        dicionario = {}
        lista = []
        for x in self.__lista_livros_prateleira:
            lista.append(x.getPrecoVendaLivro())
            dicionario[x.getTituloLivro()] = x.getPrecoVendaLivro()
        return max(dicionario, key=dicionario.get)

    def getPrecoLivroMaisCaroPrateleira(self):
        lista = []
        for x in self.__lista_livros_prateleira:
            lista.append(x.getPrecoVendaLivro())
        valor = max(lista)
        return valor

class Livro:
    def __init__(self,ano_lancamento,nome_autor,categoria,paginas,titulo,preco_venda):
        self.__ano_lancamento_livro = ano_lancamento
        self.__nome_autor_livro = nome_autor
        self.__categoria_livro = categoria
        self.__paginas_livro = paginas
        self.__titulo_livro = titulo
        self.__preco_venda_livro = preco_venda

    def getAnoLancamentoLivro(self):
        return self.__ano_lancamento_livro

    def getNomeAutorLivro(self):
        return self.__nome_autor_livro

    def getCategoriaLivro(self):
        return self.__categoria_livro
    
    def getPaginasLivro(self):
        return self.__paginas_livro

    def getTituloLivro(self):
        return self.__titulo_livro

    def getPrecoVendaLivro(self):
        return self.__preco_venda_livro

class Cliente:
    def __init__(self,nome,endereco,idade):
        self.__nome_cliente = nome
        self.__endereco_cliente = endereco
        self.__idade_cliente = idade

    def getNomeCliente(self):
        return self.__nome_cliente
    
    def getEnderecoCliente(self):
        return self.__endereco_cliente
    
    def getIdadeCliente(self):
        return self.__idade_cliente

bib1 = Biblioteca('Biblioteca Universitaria',3)

b1 = Bibliotecario('Leonardo',19,'23/10/1999',4499)
b2 = Bibliotecario('Matheus',13,'04/01/2006',4500)
b3 = Bibliotecario('André',65,'06/06/2006',2)

c1 = Cliente('Mauro','Manhattan Street',97)
c2 = Cliente('Guilherme','Garden Street',35)
c3 = Cliente('Bruno','Avenida Paulista',17)

p1 = Prateleira('Drama',1)
p2 = Prateleira('Suspense',2)
p3 = Prateleira('Comédia',3)

l1 = Livro(1999,'Manuel Bandeira','Comédia',300,'A Droga da Obediência',30)
l2 = Livro(2005,'Dawn Brown','Drama',250,'O Código da Vinci',2)
l3 = Livro(1594,'Shakespeare','Drama',500,'The Rape of Lucrece',400)


p1.addLivroPrateleira(l3)
p1.addLivroPrateleira(l2)
# for x in range(p1.getQtdeLivrosPrateleira()):
    # print(p1.getListaLivrosPrateleira(x))
print(p1.getNomeLivroMaisCaroPrateleira())