from View.Display7.Constantes import Estilos, Elementos
class Menu:
    def __init__(self, janela):
        """
        Esta classe mostra o Menu Principal
        :param janela: A janela do app
        :param titulo: O título a ser mostrado
        :param texto:  O texto a ser mostrado
        """
        self.janela = janela
        # Variável de controle
        self.on = False

        # Criando e definindo os botões
        self.criandoBotoes()
        self.definindoBotoes()
        Elementos.apagarElementoDaTela([self.botao1, self.botao2, self.botao3, self.botaoS, self.botaoD]) # Vamos rapidamente apagar os botões para que eles não apareçam


    def mostrarInstrucoes(self, titulo, texto):
        self.titulo = Elementos.criarTitulo(self.janela, self.janela.frameJogo, titulo)
        self.info = Elementos.criarTexto(self.janela, self.janela.frameJogo, texto)

        Elementos.posicionarTitulo(self.titulo)
        Elementos.posicionarTexto(self.info)




    def limparTudo(self):
        """
        Apaga toda a informação
        :return:
        """
        if self.on == True:
            Elementos.apagarElementoDaTela([self.titulo, self.info, self.botao1, self.botao2, self.botao3, self.botaoS, self.botaoD])
            self.on = False



    def reiniciar(self, titulo, texto):
        self.limparTudo()
        self.mostrarInstrucoes(titulo, texto)
        self.criandoBotoes()
        self.on = True
        self.janela.app.after(Estilos.TEMPO, lambda: self.janela.jogo.escolha(self.possibilidades, self.botoes))

    def definindoBotoes(self):
        """
        Definindo os botões a serem escolhidos
        """
        self.possibilidades = ["1", "2", "3", "s", "d"]
        self.botoes = {
            "1": self.botao1,
            "2": self.botao2,
            "3": self.botao3,
            "s": self.botaoS,
            "d": self.botaoD,

        }
    def criandoBotoes(self):

        # Criando os botões
        self.botao1 = Elementos.criarBotao(self.janela, "Investigar", self.janela.jogo.investigar, Estilos.AMARELO, Estilos.PRETO)

        self.botao2 = Elementos.criarBotao(self.janela, "Viajar", self.janela.jogo.viajar, Estilos.BRANCO, Estilos.PRETO)

        self.botao3 = Elementos.criarBotao(self.janela, "Destinos", self.janela.jogo.destinos, Estilos.AZUL, Estilos.BRANCO)

        self.botaoS = Elementos.criarBotao(self.janela, "Novo Jogo", self.janela.jogo.novoJogo, Estilos.PRETO, Estilos.BRANCO)

        self.botaoD = Elementos.criarBotao(self.janela, "Desligar", self.janela.app.destroy, Estilos.VERMELHO, Estilos.BRANCO)

        # Posicionando os botões
        Elementos.posicionarBotao(self.botao1)
        Elementos.posicionarBotao(self.botao2)
        Elementos.posicionarBotao(self.botao3)
        Elementos.posicionarBotao(self.botaoS)
        Elementos.posicionarBotao(self.botaoD)


