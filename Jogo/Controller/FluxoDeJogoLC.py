from Model.Jogo import Jogo
class FluxoDeJogoLC:
    """
    Classe que controla o fluxo do jogo
    """

    def __init__(self, view):
        """
        Inicia o jogo e fica rodando, com novos jogos, enquanto não desligar
        """
        # Recebe o objeto view com funções que vão  servir para mostrar minhas informações. Neste caso, todos os meus objetos view vão implementar estas funções
        self.view = view





    def jogar(self):
        """
        Começa o jogo.
        :return:
        """

        # Variável de controle para saber se devo desligar o programa
        self.desligar = False
        # Variável que recebera as opções escolhidas
        self.opcao = ""
        # Variáveis de controle do jogo
        self.reiniciarControle()
        # Loop que mantem o programa rodando até o usuário escolher desligar
        while self.desligar == False:
            self.jogoAtual()

    def jogoAtual(self):
        """
        Controla o jogo atual
        :return:
        """
        # Inicia o jogo
        self.iniciarJogo()
        # Laço que manterá o jogo acontecendo até que alguém escolha desligar ou sair.
        # Desligar para de rodar o programa
        # Sair, reinicia um jogo novo
        while self.sair != True:
            # Checa se o jogo deve continuar, se não para a função com o return, para retornar ao loop inicial
            if self.checandoStatusJogo():
                return

            # Imprime o menu
            self.view.mostraMenu()
            self.escolha()
            # Testa a opcão escolhida para escolher a ação a ser tomada
            if self.opcao == "1":
                self.investigar(self.jogo.cidadeAtual.locais)
            elif self.opcao == "2":
                self.viajar(self.jogo.cidadeAtual.cidadesDeDestino)
            elif self.opcao == "3":
                self.destinos(self.jogo.cidadeAtual.cidadesDeDestino)
            elif self.opcao == "v":
                print("Voltar")
                self.voltar = True
                continue
            elif self.opcao == "s":
                print("Sair")
                self.sair = True


    def escolha(self):
        """
        Checa se a escolha feita está dentro das possibilidades, se não continua esperando resposta
        :return:
        """
        possibilidades = ["1", "2", "3", "s", "d", "v"]
        valido = False
        while valido != True:
            self.opcao = input()
            valido = self.opcao in possibilidades
            if valido == False:
                self.view.escolhaIvalida()
    def iniciarJogo(self):
         # Apaga a variável jogo anterior dando o valor None, ou Nulo para
         #self.jogo = 0
         self.jogo = Jogo()
         # Inicia as variáveis de controle
         self.reiniciarControle()
         # Imprime a informação de um jogo novo
         self.view.mostraNovoJogo(self.jogo.cidadeInicial.caso, self.jogo.cidadeInicial.tarefaCaso, self.jogo.tempoJogado)
         self.view.mostraInfo(f"Bem vindo a {self.jogo.cidadeAtual.cidade}", self.jogo.cidadeAtual.curiosidade)


    # def imprimirTitulo(self, texto):
    #     print("\n/**********************/")
    #     print(texto)
    #     print("/**********************/\n")
    # def imprimirTexto(self, texto):
    #     print(texto)

    def reiniciarControle(self):
        """
        Reinicia as variáveis de controle depois de um loop de jogo
        :return:
        """
        self.sair = False
        self.voltar = False
        self.opcao = 0

    def investigar(self, locais):
        """
        Função que roda quando o botão investigar é escolhido
        :param locais:
        :return:
        """
        if self.checandoStatusJogo():
            return

        opcoes = []
        for local in locais:
            opcoes.append(local.local)

        self.view.mostraOpcoes("Escolha o local que deseja investigar digitando a opção de destino ou v para voltar.", opcoes)
        self.escolha()
        if self.checandoStatusJogo():
            return
        if self.opcao == "v":
            return
        if self.translado(1, locais[int(self.opcao) - 1].local):
            return

        self.view.mostraInfo(f"{locais[int(self.opcao) - 1].local}", f"{locais[int(self.opcao) - 1].pista}")
        # Checa se ganhou o jogo e toma as ações necessárias
        self.checarSeGanhou(locais[int(self.opcao)])


    def destinos(self, destinos):
        """
        Mostra os destinos para onde poderia viajar
        :param destinos:
        :return:
        """
        if self.checandoStatusJogo():
            return
        opcoes = []
        for destino in destinos:
            opcoes.append(destino.cidade)
        self.view.mostraOpcoes("Estes são os destinos para os quais você pode viajar:", opcoes)
        # self.imprimirTitulo("Estes são os destinos para os quais você pode viajar:")
        # for destino in destinos:
        #     self.imprimirTexto(destino.cidade)
    def viajar(self, destinos):
        """
        Mostra os destinos para onde poderia viajar
        :param destinos: as cidades para onde o jogador pode viajar
        :return:
        """
        if self.checandoStatusJogo():
            return
        opcoes = []
        for destino in destinos:
            opcoes.append(destino.cidade)
        self.view.mostraOpcoes("Para onde você quer viajar?\nSe precisar, digite v para voltar.", opcoes)
        self.escolha()
        if self.checandoStatusJogo():
            return
        if self.opcao == "v":
            return
        # Faz o translado, e faz todas as checagens de tempo. Caso tenha estourado o tempo de jogo retorna
        # Calcula o tempo de voo
        tempoVoo = self.jogo.cidadeAtual.calcularTempoDeVoo(destinos[int(self.opcao) - 1])
        if self.translado(tempoVoo, destinos[int(self.opcao) - 1].cidade):
            return
        self.jogo.cidadeAtual = destinos[int(self.opcao) - 1]
        self.view.mostraInfo(f"Bem vindo a {self.jogo.cidadeAtual.cidade}", self.jogo.cidadeAtual.curiosidade)

    def translado(self, tempo, destino):
        """
        Desconta tempo de translado
        :param tempo: tempo de qualquer viagem
        :param destino: para onde está se deslocando
        :return: Boolean: True caso tenha ultrapassado o tempo de jogo | False caso ainda tenha tempo de jogo
        """
        # TODO: Adicionar conta com coordenadas geograficas
        self.view.mostraInfoTranslado(tempo, destino)
        self.jogo.tempoJogado -= tempo
        self.view.mostraTempoRestante(tempo, self.jogo.tempoJogado)
        if self.checarSeTempoDeJogoAcabou():
            return True
        if self.devoDormir():
            return True
        return False

    def checarSeGanhou(self, local):
        """
        Verifica se a pessoa chegou ao local onde a zefa está e ganhou o jogo e toma as ações necessárias
        :param local: local de investigação
        :return:
        """
        if local.zefaEstaAqui:
            self.sair = True
            self.view.mostraGanhou(self.jogo.cidadeInicial.vitoriaCaso, self.jogo.tempoJogado)
            # self.imprimirTitulo(self.jogo.cidades[0].vitoriaCaso)
            # self.imprimirTitulo(f"YAY! Você venceu o jogo! Sua pontuação foi de {self.jogo.tempoJogado}!")
            return True
        return False
    def checarSeTempoDeJogoAcabou(self):
        """
        Checa se já acabou o tempo de jogo
        :return: Booleno True se acabou o tempo | False se ainda tem tempo
        """
        if self.jogo.tempoJogado <= 0:
            self.view.mostraPerdeu()
            # self.imprimirTitulo("Que pena. Acabou o tempo que você tinha para achar a Zefa! Mas não desista! Na próxima você acha ela!")
            self.sair = True
            return True
        else:
            return False

    def devoDormir(self):
        """
        Checa se o jogador deve dormir, se sim desconta as horas e verifica se ainda tem tempo de jogo ou não.
        :return: Boolean True se não tem mais tempo de Jogo | False se tem
        """
        if (self.jogo.acordouEm - self.jogo.tempoJogado) >= 16:
            # self.imprimirTitulo("Está na hora de dormir. Bons sonhos!")
            # for x in range(5):
            #     self.imprimirTexto("ZZZZZ...")
            self.view.mostraDormir(self.jogo.tempoJogado)
            # self.imprimirTexto(f"Bom dia. Você só tem {self.jogo.tempoJogado} horas para achar a Zefa. Vamos ver se ainda dá tempo?")
            self.jogo.tempoJogado -= 8
            if self.checarSeTempoDeJogoAcabou():
                return True
            self.view.temTempo(self.jogo.tempoJogado)
            # self.imprimirTexto(f"Ufa, você ainda tem {self.jogo.tempoJogado} horas. Corre lá.")
            return False

    def checarSeDeveDesligar(self):
        """
        Função que checa se deve desligar. Ela é usada sempre que temos um menu de escolha no início
        :return: True
        """
        if self.opcao == "d":
            self.desligar = True
            return True
        else:
            return False
    def checarSeDeveSair(self):
        """
        Função que checa se deve sair do jogo e iniciar um novo. Ela é usada sempre que temos um menu de escolha no início
        :return: True
        """
        if self.opcao == "s" or self.sair == True:
            self.sair = True
            return True
        else:
            return False

    def checandoStatusJogo(self):
        """
        Função que checa se o jogo deve continuar ou reiniciar ou desligar,
        Usada sempre que há um menu de escolha
        :return: Boolean
        """
        if self.checarSeDeveDesligar() or self.checarSeDeveSair():
            return True
        else:
            return False


