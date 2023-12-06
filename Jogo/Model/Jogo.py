from Model.ConexaoBD import ConexaoBD
from Model.Cidade import Cidade
import random
class Jogo:
    """
    Classe que criaa o jogo. Criação e Lógica de jogo
    """
    # Com este roteiro sabemos para que cidades podemos viajar de cada cidade. Isso porque os destinos possíveis refere-se sempre aos indices, que batem com os índices da lista self.cidades. Então, por exemplo, os destinos para onde se pode viajar desde a cidade que estiver no índice 1 do array selfcidades são as dos índices 5, 2 e 8 do mesmo array
    destinosPossiveis = [[2,4,7],[5,2,8],[3,1,0],[4,2,7],[0,3,5],[1,6,4],[0,2,5],[0,3,8],[0,1,7]]
    # Com este roteiro, buscamos a pista da cidade. Exemplo, se o detevive está na cidade do índice 0 de self.cidades então as pists mostradas devem ser as da cidade do índice 4
    roteiroZefa = [4,5,1,2,3,False, False, False, False]
    def __init__(self):
        self.conexaoBD = ConexaoBD()
        # self.tempoDeJogo = 152
        self.acordouEm = 152
        self.tempoJogado = 152
        self.criarJogo()


    def sortearCidades(self):
        sql = "select pk_id_cidade from cidades"
        resultados = self.conexaoBD.lerDados(sql)
        print(resultados)
        indicesCidades = []
        # Sorteando os indices das cidades
        if len(resultados) > 0:
            for indiceCidade in range(0,9):
                indice = random.randint(0, len(resultados) - 1)
                print(resultados[indice][0])
                indicesCidades.append(resultados[indice]["pk_id_cidade"])
                resultados.pop(indice)
            print(indicesCidades)
            return indicesCidades

        else:
            self.erro = "Não há cidades"
    def criarJogo(self):
        # Escolhendo as cidades
        indicesCidades = self.sortearCidades()
        # Criando a lista com as 9 cidades
        self.criarListaDeCidades(indicesCidades)

        # Buscando a informação de caso para a cidade no indice 0
        self.criarCaso()
        #Buscando a informação de pistas para os indices de 0 a 4
        for i in range(0,5):
            # As pistas que busco não são da cidade, mas sim da cidade para a qual se deveria viajar se eu estiver nessa cidade. Minha cidade de destino ideal. para isso eu uso o Array do Roteiro da Zefa para saber para onde a Zefa foi quando estava na cidade do índice i e recolher as pistas dessa cidade
            self.cidades[i].criandoAsPistas(self.cidades)

        # Criando a informação da cidade final do índice 5
        self.cidades[5].criarPistasCidadeFinal()

        # Criando a informação de pista para os indices de 6,7,8
        for x in range(6,9):
            self.cidades[x].criarPistasCidadeFalsa()

        # Atribuindo destinos às cidades
        self.criandoDestinosPossiveis()

        # Embaralhando cidades
        self.embaralharCidades()

        # Embaralhando os destinos
        for cidade in self.cidades:
            cidade.embaralharDestinos()



    def criandoDestinosPossiveis(self):
        """
        Atribui as cidades de destino de viagem para cada cidade da lista de cidades
        :return:
        """
        index = 0
        for cid in self.cidades:
            arrayTemp= []
            print("Indice destinos possiveis")
            print(self.destinosPossiveis[index])
            for destinos in self.destinosPossiveis[index]:
                arrayTemp.append(self.cidades[destinos])
            cid.criarCidadesDestino(arrayTemp)
            for destino in cid.cidadesDeDestino:
                print(f"Destino da cidade {cid.cidade} é {destino.cidade}")
            index += 1

    def criarListaDeCidades(self, indicesCidades):
        """
        Com os índices das cidades escolhidos, ele monta a lista com os objetos Cidade.
        Faz isto em duas etapas para não desperdiçar memória pegando toda a informação de cidades e países antes de definir quais cidades serão as do jogo. Dessa maneira pegando a informação só das cidades necessárias
        :param indicesCidades: o índice das cidades criado criarJogo
        :return:
        """
        self.cidades = []
        # Buscando informação de cada cidade
        for indice in range(0,9):
            self.cidades.append(Cidade(self.conexaoBD, indicesCidades[indice], self.roteiroZefa[indice]))


        # Definindo a cidade em que o jogo se encontra, no caso a primeira que é sempre a de indice 0
        self.cidadeAtual = self.cidades[0]
        self.cidadeInicial = self.cidades[0]

    def criarCaso(self):
        """
        Cria o caso para a cidade do índice 0
        :return:
        """
        self.cidades[0].criarCaso()

    def embaralharCidades(self):
        """
        Embaralha as cidades para que não fique previsivel a rota, (de modo similar, você pode verificar o método do Python shuffle que têm o mesmo princípio)
        :return:
        """
        cidadesTemp = []
        elementos = len(self.cidades)
        print(f"Antes de embaralhar as cidades ficaram")
        for c in self.cidades:
            print(c.cidade)
        for i in range(elementos):
            indice = random.randint(0, (len(self.cidades) - 1))
            cidadesTemp.append(self.cidades.pop(indice))

        print(f"Depois de emparalhar no temp as cidades ficaram: ")
        print(self.cidades)
        for cidade in cidadesTemp:
            self.cidades.append(cidade)
        print(f"Depois de embaralhar as cidades ficaram")
        for cid in self.cidades:
            print(cid.cidade)







