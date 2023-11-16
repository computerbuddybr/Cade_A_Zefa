from View.Display7.Constantes import Estilos, Elementos
class Info:
    """
    Mostra a informação final
    """
    def __init__(self, janela):
        """
       Para as opções de visualização que terão somente os botões de Voltar, Novo Jogo e Desligar como por exemplo "Mostrar Destinos"
       :param janela: A janela do app
       :param titulo: O título que precisa mostrar
       :param info: O texto que precisa mostrar
       """
        self.janela = janela
        self.tituloTexto = ""
        self.texto = ""

        # Variável de controle
        self.on = False




    def atualizarInfo(self, titulo, texto):
        """
        Atualiza a informação das variáveis
        :param titulo:
        :param texto:
        :param locais:
        :return:
        """
        self.tituloTexto = titulo
        self.texto = texto

    def mostrarInstrucoes(self, titulo, texto):
        """
        Mostra as informações
        :return:
        """
        self.titulo = Elementos.criarTitulo(self.janela, self.janela.frameJogo, titulo)
        self.info = Elementos.criarTexto(self.janela, self.janela.frameJogo, texto)
        Elementos.posicionarTitulo(self.titulo)
        Elementos.posicionarTexto(self.info)



    def limparInfo(self):
        """
        Apaga os frames com informação
        :return:
        """
        Elementos.apagarElementoDaTela([self.titulo, self.info])
        self.titulo.grid_forget()
        self.info.grid_forget()

    def limparTudo(self):
        """
        Apaga os frames com informação e botões
        :return:
        """
        if self.on == True:
            Elementos.apagarElementoDaTela([self.titulo, self.info, self.botaoS, self.botaoD])
            # self.titulo.grid_forget()
            # self.info.grid_forget()
            # self.botaoS.grid_forget()
            # self.botaoD.grid_forget()
            self.on = False


    def reiniciar(self, titulo, texto):
        """
        Recoloca toda a informação nos seus frames
        :param titulo: título que precisa mostrar
        :param texto: texto que precisa mostrar
        :return:
        """


        self.on = True
        self.mostrarInstrucoes(titulo, texto)
        self.criandoBotoes()
    def criandoBotoes(self):
        """
        Cria os botões
        :return:
        """

        self.botaoS = Elementos.criarBotao(self.janela, "Novo Jogo", Estilos.PRETO, Estilos.BRANCO)

        self.botaoD = Elementos.criarBotao(self.janela, "Desligar", Estilos.VERMELHO, Estilos.BRANCO)

        Elementos.posicionarBotao(self.botaoS)
        Elementos.posicionarBotao(self.botaoD)






