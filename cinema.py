class Cinema:
    def __init__(self,nome,endereco):
        self.__nome_cinema = nome
        self.__endereco_cinema = endereco
        self.__lista_funcionarios_cinema = []
        self.__lista_salas_cinema = []
        self.__lista_filmes_cinema = []
        self.__lista_sessoes_cinema = []

    def addSessaoCinema(self,sessao):
        self.__lista_sessoes_cinema.append(sessao)

    def getSessaoMaisCaraCinema(self):
        lista = []
        for x in self.__lista_sessoes_cinema:
            lista.append(x.getPrecoSessao())
        val = max(lista)
        return val

    def addFilmesCinema(self,filme):
        self.__lista_filmes_cinema.append(filme)

    def addSalaCinema(self,sala):
        self.__lista_salas_cinema.append(sala)

    def getQtdeFilmesCinema(self):
        return len(self.__lista_filmes_cinema)

    def getFilmesComediaCinema(self,indice):
        return self.__lista_filmes_cinema[indice].getNomeFilme()
        
    def getGeneroMaisPopularCinema(self):
        lista=[]
        dic = {}
        for x in self.__lista_sessoes_cinema:
            if x.getGeneroSessao() in dic:
                dic[x.getGeneroSessao()] += 1
            else:
                dic[x.getGeneroSessao()] = 1
        for key in dic:
            lista.append(dic[key])
        for gen in dic:
            if dic[gen] == max(lista): 
                return gen
        
    def getCapacidadeMaximaCinema(self):
        lista = []
        for x in self.__lista_salas_cinema:
            lista.append(x.getCapacidadeSala())
        valor = sum(lista)
        return valor

    def lucroMaximoCinema(self):
        valor = self.getCapacidadeMaximaCinema() * self.getSessaoMaisCaraCinema()
        return valor

class Funcionario:
    def __init__(self,idade,nome,salario,sexo):
        self.__idade_funcionario = idade
        self.__nome_funcionario = nome
        self.__salario_funcionario = salario
        self.__sexo_funcionario = sexo

class Sala:
    def __init__(self,codigo,capacidade):
        self.__codigo_sala = codigo
        self.__capacidade_sala = capacidade

    def getCapacidadeSala(self):
        return self.__capacidade_sala

class Filme:
    def __init__(self,nome_filme,data_lancamento,nome_diretor,genero,duracao):
        self.__nome_filme = nome_filme
        self.__data_lancamento_filme = data_lancamento
        self.__nome_diretor_filme = nome_diretor
        self.__genero_filme = genero
        self.__duracao_filme = duracao

    def getGeneroFilme(self):
        return self.__genero_filme

    def getNomeFilme(self):
        return self.__nome_filme

class Sessao:
    def __init__(self,data,hora,filme,sala,preco):
        self.__data_sessao = data
        self.__hora_sessao = hora
        self.__filme_sessao = filme
        self.__sala_sessao = sala
        self.__preco_bilhete_sessao = preco

    def getPrecoSessao(self):
        return self.__preco_bilhete_sessao

    def getGeneroSessao(self):
        return self.__filme_sessao.getGeneroFilme()

c1 = Cinema('Grupo Cine','Avenida Paulista')

f1 = Funcionario(35,'Fernando',1000,'Masculino')
f2 = Funcionario(37,'Carla',1500,'Feminino')

sala1 = Sala(1,300)
sala2 = Sala(2,500)
sala3 = Sala(3,500)
sala4 = Sala(4,500)


filme1 = Filme('Lagoa Azul',1999,'Alexandre Santoro','Terror',100)
filme2 = Filme('Vingadores',2018,'Castro Brothers','Aventura',180)
filme3 = Filme('Rambo',1988,'Arnold','Aventura',150)
filme4 = Filme('Frozen',2017,'Disney','Aventura',130)

sessao1 = Sessao('20/10/19','15:00',filme1,sala1,10)
sessao2 = Sessao('01/02/18','16:00',filme2,sala2,20)
sessao3 = Sessao('11/02/18','16:30',filme3,sala3,30)
sessao4 = Sessao('21/02/18','16:45',filme4,sala4,40)


c1.addSessaoCinema(sessao1)
c1.addSessaoCinema(sessao2)
c1.addSessaoCinema(sessao3)
c1.addSessaoCinema(sessao4)
# print(c1.getSessaoMaisCaraCinema())
c1.addFilmesCinema(filme1)
c1.addFilmesCinema(filme2)
c1.addFilmesCinema(filme3)
c1.addFilmesCinema(filme4)

c1.addSalaCinema(sala1)
c1.addSalaCinema(sala2)
c1.addSalaCinema(sala3)
c1.addSalaCinema(sala4)
# for x in range(c1.getQtdeFilmesCinema()):
    # print(c1.getFilmesComediaCinema(x))

print(c1.getGeneroMaisPopularCinema())
print(c1.getCapacidadeMaximaCinema())
print(c1.lucroMaximoCinema())
