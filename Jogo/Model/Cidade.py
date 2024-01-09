import random
import haversine as hs

from Model.Local import Local
class Cidade:
    def __init__(self, conexaoBD, id, destino):
        """
        Inicia a classe cidade
        :param: conexãoBD: o objeto de conexão à base de dados
        :param: id: o id da Cidade buscada
        :param: destino: o indíce no array cidades da cidade de destino
        """
        self.destino = destino
        self.conexaoBD = conexaoBD

        self.locais = []
        self.localAtual = ""

        sql = f"select * from cidades as c INNER JOIN paises as p ON (c.fk_id_pais = p.pk_id_pais) where c.pk_id_cidade =  :id"
        parametros = {"id": id}
        resultado = self.conexaoBD.lerDadosParam(sql, parametros)


        if len(resultado) >= 1:

            self.id = resultado[0]["pk_id_cidade"]
            self.cidade = resultado[0]["cidade"]
            self.latitude = resultado[0]["latitude"]
            self.longitude = resultado[0]["longitude"]
            self.cores_bandeira = resultado[0]["cores_bandeira"]
            self.imagem_bandeira = resultado[0]["imagem_bandeira"]

            if self.imagem_bandeira !=  None:
                # self.imagem_bandeira == False
                print("Imagem bandeira não era None")
            self.moeda = resultado[0]["moeda"]

            sql = f"select * from curiosidades_cidades where fk_id_cidade = :id"
            parametros = {"id": self.id}
            curiosidades = conexaoBD.lerDadosParam(sql, parametros)
            # print(curiosidades)
            quantidadeDeCuriosidades = len(curiosidades)

            if quantidadeDeCuriosidades > 1:
                indice = random.randint(0, quantidadeDeCuriosidades - 1)
                self.curiosidade = curiosidades[indice]["curiosidade"] # Outra opção aqui é usar a função choice da biblioteca random que retorna um elemento de uma sequência não vazia de modo aleatório. Se quiser saber mais dê uma olhada na documentação: https://docs.python.org/3/library/random.html#random.choice
            else:
                self.curiosidade = curiosidades[0]["curiosidade"]
            #Criando os locais desta cidade - as pistas serão atribuidas a estes locais na classe Jogo
            self.criarLocais()
            #Aqui estou buscando a pista da cidade para para depois atribuir onde esta cidade for destino
            self.buscarPistasCidade()

    def criarCaso(self):
        """
        Cria o caso para a cidade
        :return: informação de caso atribuida às propriedades da cidade
        """
        sql = f"select * from casos where fk_id_cidade = :id"
        parametros = {"id": self.id}
        casos = self.conexaoBD.lerDadosParam(sql, parametros)

        quantidadeDeCasos = len(casos)
        indice = 0
        if quantidadeDeCasos > 0:
            if quantidadeDeCasos > 1:
                indice = random.randint(0, quantidadeDeCasos - 1)
            self.tituloCaso = casos[indice]["titulo"]
            self.caso = casos[indice]["caso"]
            self.tarefaCaso = casos[indice]["tarefa"]
            self.vitoriaCaso = casos[indice]["mensagem_de_vitoria"]

        else:
            self.erro = "Não há um caso com esse id de cidade"

    def buscarPistasCidade(self):
        """
        Buscando as pistas que dizem respeito a esta cidade, para serem usadas quando a cidade for destino
        :return: lista de pistas da cidade
        """
        self.pistasCidade = []
        sql = f"select pista from pista_da_cidade where fk_id_cidade = :id"
        parametros = {"id": self.id}
        pistas = self.conexaoBD.lerDadosParam(sql,parametros)
        print("Pistas da base")
        print(pistas)
        for pista in pistas:
            self.pistasCidade.append(pista["pista"])
        print("As pistas da cidade são:")
        print(self.pistasCidade)
    def criarLocais(self):
        """
        Criando os locais da cidade
        :return: a atribuição dos locais a propriedade locais
        """
        sql = "select * from locais"
        locaisBase = self.conexaoBD.lerDados(sql)
        # print("Locais Base")
        # print(locaisBase)
        if len(locaisBase) > 0:
            for indice in range(0,3):
                indice = random.randint(0, len(locaisBase) - 1)
                print(f"O local que vai ser colocado")
                print(locaisBase[indice])
                self.locais.append(Local(self.conexaoBD, locaisBase[indice]["pk_id_local"],locaisBase[indice]["local"], locaisBase[indice]["bandeira"], locaisBase[indice]["pista_cidade"], locaisBase[indice]["moeda"]))
                locaisBase.pop(indice)
            print("Os locais")

            print(len(self.locais))
        else:
            self.erro = "Não há locais na base"
            print(self.erro)
        print(f"Os locais escolhidos para a cidade {self.cidade}:")
        for local in self.locais:
            print(local.local)


    def criandoAsPistas(self, destinos):
        """
        Atribuindo as pistas aos locais
        :param destinos: o array com todas as cidades do caso para poder verificar a cidade para a qual a Zefa partiu desta cidade, e a qual as pistas dirão respeito a está cidade
        :return: atribuição das pistas a propriedade pista de cada Local
        """
        #Variáveis de controle
        coresBandeiraUsada = False
        imagemBandeiraUsada = False
        pistasBandeiras = 0
        moedaUsada = False
        print(f"Criando as pistas para {self.cidade}")
        print("Locais da cidade onde pistas vão ser criadas")
        for loc in self.locais:
            print(f"{loc.local} com {loc.personagem}")
        for local in self.locais:
            print(f"Pegando pista para: {local.local} com id: {local.id} Bandeira: {local.bandeira} Moeda: {local.moeda} Personagem: {local.personagem}")
            if local.bandeira == 1:
                print(f"Imagem bandeira: {destinos[self.destino].imagem_bandeira}")
                if destinos[self.destino].imagem_bandeira !=  None:
                    print(f"Entrou na imagem bandeira")
                    if imagemBandeiraUsada == False:
                        if (random.randint(0,1) == 0 and pistasBandeiras == 0) or pistasBandeiras == 1:
                            local.criaPistaBandeira(destinos[self.destino].imagem_bandeira, True)
                            imagemBandeiraUsada = True
                            pistasBandeiras += 1
                            continue
                if coresBandeiraUsada == False:
                    local.criaPistaBandeira(destinos[self.destino].cores_bandeira, False)
                    coresBandeiraUsada = True
                    pistasBandeiras += 1
                    continue

            if local.moeda == 1 and moedaUsada == False:
                local.criarPistaMoeda(destinos[self.destino].moeda)
                moedaUsada = True
                continue

            print("Pistas antes do pop",destinos[self.destino].pistasCidade)
            local.criarPistaCidade(destinos[self.destino].pistasCidade)
            print("Pistas depois do pop",destinos[self.destino].pistasCidade)
        print("Resultado montagem locais")
        for newLocal in self.locais:
            print(f"A pista para o local: {newLocal.local} da cidade {self.cidade} é: {newLocal.pista}")


    def criarPistasCidadeFinal(self):
        """
        Caso está seja a cidade final onde a Zefa se encontra, atribuindo as pistas a propriedade pista dos locais
        :return: atribuição das pistas a propriedade pista de cada Local
        """
        localFinal = random.randint(0,2)
        print(f"Indice do local final: {localFinal}")

        for indice in range(0,3):
            print(f"Indice para pista de {self.locais[indice].local}: {indice}")
            if indice != localFinal:
                print("Criou pistas de cidade final")
                self.locais[indice].criarPistaCidadeFinal()
            else:
                print("Criou pista prender a zefa")
                self.locais[indice].criarPistaPrendeuAZefa()
        print(f"Pistas cidade final de {self.cidade}: ")
        for loc in self.locais:
            print(f"Local: {loc.local} Pista: {loc.pista}")

    def criarPistasCidadeFalsa(self):
        """
        Caso est seja uma das 3 cidades falsas. Atribuindo as pistas de cidade falsa a propriedade pista dos locais
        :return: atribuição das pistas a propriedade pista de cada Local
        """
        for local in self.locais:
            local.criarPistaFalsa()
        print(f"Pistas cidade falsa de {self.cidade}: ")
        for loc in self.locais:
            print(f"Local: {loc.local} Pista: {loc.pista}")


    def criarCidadesDestino(self, cidadesDestino):
        """
        Atribuindo as cidades para onde se pode viajar para a cidade atual
        :param cidadesDestino: array com as cidades para onde se pode viajar
        :return: atribui a lsita de cidades para a propriedade cidadesDeDestino
        """
        self.cidadesDeDestino = []
        for cidade in cidadesDestino:
            self.cidadesDeDestino.append(cidade)


    def embaralharDestinos(self):
        """
        Embaralha os destinos para que não fique previsivel a rota (de modo similar, você pode verificar o método do Python shuffle que têm o mesmo princípio)
        :return:
        """
        destinosTemp = []
        elementos = len(self.cidadesDeDestino)
        print(f"Embaralhando destinos para {self.cidade}")
        print(f"Destinos antes de embaralhar")
        for d in self.cidadesDeDestino:
            print(d.cidade)
        for i in range(elementos):
            indice = random.randint(0, (len(self.cidadesDeDestino) - 1))
            destinosTemp.append(self.cidadesDeDestino.pop(indice))

        print(f"Depois de emparalhar no temp os destinos ficaram: ")
        print(self.cidadesDeDestino)
        for destino in destinosTemp:
            self.cidadesDeDestino.append(destino)
        print(f"Depois de embaralhar os destinos ficaram")
        for dest in self.cidadesDeDestino:
            print(dest.cidade)


    def calcularTempoDeVoo(self, cidade):
        """
        Calcular o tempo de voo entre a cidade atual e a cidade de destino
        :param: cidade de destino
        :return:
        """
        velocidadeAviao = 850 # velocidade em km por hora
        origem = (float(self.latitude),float(self.longitude))
        destino = (float(cidade.latitude),float(cidade.longitude))
        distancia = hs.haversine(origem,destino) # retorna valor em km
        print(f"Distância: {distancia}")
        horas = round(distancia/velocidadeAviao) # nosso avião é miraculoso e anda sempre na mesma velocidade sem aceleração nenhuma, e as horas sempre dão um número redondinho
        print(f"Horas de vôo {cidade.cidade}: {horas}")
        return horas


