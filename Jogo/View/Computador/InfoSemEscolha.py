from View.Computador.Constantes import Estilos, Elementos
import tkinter as tk
class InfoSemEscolha:
    """
    Mostra a informação de opções sem escolha como Destinos
    """
    def __init__(self, janela):
        """
        Para as opções de visualização que terão somente os botões de Voltar, Novo Jogo e Desligar como por exemplo "Mostrar Destinos"
        :param janela: A janela do app
        :param titulo: O título que precisa mostrar
        :param info: O texto que precisa mostrar
        """
        self.janela = janela
        self.titulo = ""
        self.info = []

        # Variável de controle
        self.on = False


        # self.mostrarInstrucoes()
        #
        # self.criandoBotoes()



    def atualizarInfo(self, titulo, info):
        """
        Atualiza a informação das variáveis
        :param titulo:
        :param texto:
        :param locais:
        :return:
        """
        self.tituloTexto = titulo
        self.info.clear()
        for opcao in info:
            self.info.append(opcao)

    def mostrarInstrucoes(self):
        """
        Mostra as informações
        :return:
        """
        self.titulo = Elementos.criarTitulo(self.janela, self.janela.frameJogo, self.tituloTexto)
        self.info1 = Elementos.criarTexto(self.janela, self.janela.frameJogo, self.info[0])
        self.info2 = Elementos.criarTexto(self.janela, self.janela.frameJogo, self.info[1])
        self.info3 = Elementos.criarTexto(self.janela, self.janela.frameJogo, self.info[2])

        Elementos.posicionarTitulo(self.titulo)
        Elementos.posicionarTexto(self.info1)
        Elementos.posicionarTexto(self.info2)
        Elementos.posicionarTexto(self.info3)





    def limparTudo(self):
        """
        Apaga os frames com informação e botões
        :return:
        """
        if self.on == True:
            Elementos.apagarElementoDaTela([self.titulo, self.info1, self.info2, self.info3, self.botaoV, self.botaoS, self.botaoD])
            self.on = False


    def reiniciar(self, titulo, info):
        """
        Recoloca toda a informação nos seus frames
        :param titulo: título que precisa mostrar
        :param texto: texto que precisa mostrar
        :return:
        """
        self.on = True
        self.atualizarInfo(titulo, info)
        self.mostrarInstrucoes()
        self.criandoBotoes()

    def criandoBotoes(self):
        """
        Cria os botões
        :return:
        """

        # Criando os botões
        # Criando os botões

        self.botaoV = Elementos.criarBotao(self.janela, "Voltar", self.janela.jogo.voltar, Estilos.AZUL, Estilos.BRANCO)

        self.botaoS = Elementos.criarBotao(self.janela, "Novo Jogo", self.janela.jogo.novoJogo, Estilos.PRETO, Estilos.BRANCO)

        self.botaoD = Elementos.criarBotao(self.janela, "Desligar", self.janela.app.destroy, Estilos.VERMELHO, Estilos.BRANCO)

        # Posicionando os botões


        Elementos.posicionarBotao(self.botaoV)
        Elementos.posicionarBotao(self.botaoS)
        Elementos.posicionarBotao(self.botaoD)









