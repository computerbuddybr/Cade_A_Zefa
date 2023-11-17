from View.Display7.Constantes import Estilos, Elementos
class InfoComEscolha:
    """
    Mostra as informações de opções com escolhas como Investigar e Viajar e o principal
    """
    def __init__(self, janela, tipo):
        """
        Mostra as informações que terão uma escolha
        :param janela: A janela do app
        :param titulo: O título que precisa colocar
        :param tipo: "investigar" ou "viajar". A decisão do tipo serve para saber quanto descontar do tempo de viagem
        """
        self.janela = janela
        self.tipo = tipo
        # Aqui iniciamos a variável com valores padrões que depois serão trocados simplesmente para não causar bugs de inicialização
        if self.tipo == "investigar":
            self.tempoViagem = 1
        else:
            self.tempoViagem = 10
        self.opcoes = []

        # Variável de controle
        self.on = False



    def atualizarInfo(self, opcoes):
        """
        Atualiza a informação das variáveis
        :param titulo:
        :param texto:
        :param locais:
        :return:
        """

        self.opcoes.clear()
        for opcao in opcoes:
            self.opcoes.append(opcao)

    def mostrarInstrucoes(self, titulo, texto):
        # Para apagar o texto que tinha antes
        self.titulo = Elementos.criarTitulo(self.janela, self.janela.frameJogo, titulo)
        self.info = Elementos.criarTexto(self.janela, self.janela.frameJogo, texto)
        Elementos.posicionarTitulo(self.titulo)
        Elementos.posicionarTexto(self.info)



    def limparInfo(self):
        Elementos.apagarElementoDaTela([self.titulo, self.info])

    def limparTudo(self):
        """
        Apaga toda a informação
        :return:
        """
        if self.on == True:
            Elementos.apagarElementoDaTela([self.titulo, self.info, self.botao1, self.botao2, self.botao3, self.botaoV, self.botaoS, self.botaoD])
            self.on = False

    def trocarInfo(self, titulo, texto):
        self.limparInfo()
        self.mostrarInstrucoes(titulo, texto)

    def deslocar(self, op):
        # Como eu recebo um string iniciando em um, preciso transformar em um int e subtrair 1 para ter a posição de índice correto
        opcao = int(op) - 1


        if self.tipo == "investigar":
            self.tempoViagem = 1
            self.localDestino = self.janela.jogo.jogo.cidadeAtual.locais[opcao].local
            if self.testarTempo() == False:
                return
            self.trocarInfo(self.janela.jogo.jogo.cidadeAtual.locais[opcao].local, f"{self.janela.jogo.jogo.cidadeAtual.locais[opcao].personagem}: {self.janela.jogo.jogo.cidadeAtual.locais[opcao].pista}")

            # Vendo se ganhou
            if self.janela.jogo.jogo.cidadeAtual.locais[opcao].zefaEstaAqui:
                self.janela.jogo.ganhou()

        else:


            self.localDestino = self.janela.jogo.jogo.cidadeAtual.cidadesDeDestino[opcao].cidade
            self.tempoViagem = self.janela.jogo.jogo.cidadeAtual.calcularTempoDeVoo(self.janela.jogo.jogo.cidadeAtual.cidadesDeDestino[opcao])

            if self.testarTempo() == False:
                return

            # self.janela.atualizarTempo()
            self.janela.jogo.novaCidade(self.janela.jogo.jogo.cidadeAtual.cidadesDeDestino[opcao])



    def testarTempo(self):
        """
        Testa o tempo para ver se finalizou o jogo, e se precisa dormir
        :return: True - pode continuar o jogo | False: acabou o tempo de jogo
        """
        if self.janela.jogo.deslocar(self.tempoViagem, self.localDestino) == False:
            self.janela.jogo.acabouJogo()
            return False

        dormiu = self.janela.jogo.dormir()
        if dormiu > 0:
            print("Entrou em tem que dormir")
            if dormiu == 1:
                self.janela.jogo.acabouJogo()
                return False
        return True
    def reiniciar(self, titulo, texto, opcoes):
        # self.limparTudo()
        self.atualizarInfo(opcoes)
        self.mostrarInstrucoes(titulo, texto)
        self.criandoBotoes()
        self.on = True
    def criandoBotoes(self):

        # Criando os botões
        self.botao1 = Elementos.criarBotao(self.janela, self.opcoes[0], Estilos.AMARELO, Estilos.PRETO)

        self.botao2 = Elementos.criarBotao(self.janela, self.opcoes[1], Estilos.BRANCO, Estilos.PRETO)

        self.botao3 = Elementos.criarBotao(self.janela, self.opcoes[2], Estilos.AZUL, Estilos.BRANCO)

        self.botaoV = Elementos.criarBotao(self.janela, "Voltar", Estilos.AZUL, Estilos.BRANCO)

        self.botaoS = Elementos.criarBotao(self.janela, "Novo Jogo", Estilos.PRETO, Estilos.BRANCO)

        self.botaoD = Elementos.criarBotao(self.janela, "Desligar", Estilos.VERMELHO, Estilos.BRANCO)

        # Posicionando os botões



        Elementos.posicionarBotao(self.botao1)
        Elementos.posicionarBotao(self.botao2)
        Elementos.posicionarBotao(self.botao3)
        Elementos.posicionarBotao(self.botaoV)
        Elementos.posicionarBotao(self.botaoS)
        Elementos.posicionarBotao(self.botaoD)








