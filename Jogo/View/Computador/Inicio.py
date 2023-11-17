from View.Computador.Constantes import Estilos, Elementos
import tkinter as tk
class Inicio:
    """
    Mostra a informação inicial
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






    def mostrarInstrucoes(self):
        """
        Mostra as informações
        :return:
        """
        self.titulo = Elementos.criarTitulo(self.janela, self.janela.frameJogo, self.janela.jogo.jogo.cidadeInicial.tituloCaso)
        self.caso = Elementos.criarTexto(self.janela, self.janela.frameJogo, self.janela.jogo.jogo.cidadeInicial.caso)
        self.tarefa = Elementos.criarTexto(self.janela, self.janela.frameJogo,
                                           f"Sua tarefa: {self.janela.jogo.jogo.cidadeInicial.tarefaCaso}")
        Elementos.posicionarTitulo(self.titulo)
        Elementos.posicionarTexto(self.caso)
        Elementos.posicionarTexto(self.tarefa)





    def limparTudo(self):
        """
        Apaga os frames com informação e botões
        :return:
        """
        if self.on == True:
            Elementos.apagarElementoDaTela([self.titulo, self.caso, self.tarefa, self.botaoJ, self.botaoS, self.botaoD])
            # self.titulo.grid_forget()
            # self.caso.grid_forget()
            # self.tarefa.grid_forget()
            # self.botaoJ.grid_forget()
            # self.botaoS.grid_forget()
            # self.botaoD.grid_forget()
            self.on = False


    def reiniciar(self):
        """
        Recoloca toda a informação nos seus frames
        :param titulo: título que precisa mostrar
        :param texto: texto que precisa mostrar
        :return:
        """
        self.on = True
        self.mostrarInstrucoes()
        self.criandoBotoes()
    def criandoBotoes(self):
        """
        Cria os botões
        :return:
        """

        self.botaoJ = Elementos.criarBotao(self.janela, "Jogar", self.janela.jogar, Estilos.AZUL, Estilos.BRANCO)
        self.botaoS = Elementos.criarBotao(self.janela, "Novo Jogo", self.janela.jogo.novoJogo, Estilos.PRETO, Estilos.BRANCO)

        self.botaoD = Elementos.criarBotao(self.janela, "Desligar", self.janela.app.destroy, Estilos.VERMELHO, Estilos.BRANCO)

        Elementos.posicionarBotao(self.botaoJ)
        Elementos.posicionarBotao(self.botaoS)
        Elementos.posicionarBotao(self.botaoD)







