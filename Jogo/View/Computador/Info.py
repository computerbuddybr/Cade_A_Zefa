from View.Computador.Constantes import Estilos, Elementos
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

        # Variável de controle
        self.on = False





    def mostrarInstrucoes(self, titulo, texto):
        """
        Mostra as informações
        :return:
        """
        self.titulo = Elementos.criarTitulo(self.janela, self.janela.frameJogo, titulo)
        self.info = Elementos.criarTexto(self.janela, self.janela.frameJogo, texto)
        Elementos.posicionarTitulo(self.titulo)
        Elementos.posicionarTexto(self.info)




    def limparTudo(self):
        """
        Apaga os frames com informação e botões
        :return:
        """
        if self.on == True:
            Elementos.apagarElementoDaTela([self.titulo, self.info, self.botaoS, self.botaoD])
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
        self.botaoS = Elementos.criarBotao(self.janela, "Novo Jogo", self.janela.jogo.novoJogo, Estilos.PRETO, Estilos.BRANCO)

        self.botaoD = Elementos.criarBotao(self.janela, "Desligar", self.janela.app.destroy, Estilos.VERMELHO, Estilos.BRANCO)

        Elementos.posicionarBotao(self.botaoS)
        Elementos.posicionarBotao(self.botaoD)






