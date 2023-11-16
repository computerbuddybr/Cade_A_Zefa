from View.Computador.Constantes import Estilos, Elementos
import tkinter as tk
class Menu():
    def __init__(self, janela):
        """
        Mostra o Menu Principal
        :param janela: A janela do app
        :param titulo: O título a ser mostrado
        :param texto:  O texto a ser mostrado
        """
        self.janela = janela
        # Variável de controle
        self.on = False


    def mostrarInstrucoes(self, titulo, texto):
        self.titulo = Elementos.criarTitulo(self.janela, self.janela.frameJogo, titulo)
        self.info = Elementos.criarTexto(self.janela, self.janela.frameJogo, texto)

        Elementos.posicionarTitulo(self.titulo, 0)
        Elementos.posicionarTexto(self.info,1)



    def limparInfo(self):
        Elementos.apagarElementoDaTela([self.titulo, self.info])
        # self.titulo.grid_forget()
        # self.info.grid_forget()

    def limparTudo(self):
        """
        Apaga toda a informação
        :return:
        """
        if self.on == True:
            Elementos.apagarElementoDaTela([self.titulo, self.info, self.botao1, self.botao2, self.botao3, self.botaoS, self.botaoD])
            # self.titulo.grid_forget()
            # self.info.grid_forget()
            # self.botao1.grid_forget()
            # self.botao2.grid_forget()
            # self.botao3.grid_forget()
            # self.botaoV.grid_forget()
            # self.botaoS.grid_forget()
            # self.botaoD.grid_forget()
            self.on = False


    def trocarInfo(self, titulo, texto):
        self.limparInfo()
        self.mostrarInstrucoes(titulo, texto)

    def reiniciar(self, titulo, texto):
        self.limparTudo()
        self.mostrarInstrucoes(titulo, texto)
        self.criandoBotoes()
        self.on = True
    def criandoBotoes(self):

        # Criando os botões
        self.botao1 = Elementos.criarBotao(self.janela, "Investigar", self.janela.jogo.investigar, Estilos.AMARELO, Estilos.PRETO)

        self.botao2 = Elementos.criarBotao(self.janela, "Viajar", self.janela.jogo.viajar, Estilos.BRANCO, Estilos.PRETO)

        self.botao3 = Elementos.criarBotao(self.janela, "Destinos", self.janela.jogo.destinos, Estilos.AZUL, Estilos.BRANCO)

        # self.botaoV = Elementos.criarBotao(self.janela, "Voltar", self.janela.jogo.voltar, Estilos.AZUL, Estilos.BRANCO)

        self.botaoS = Elementos.criarBotao(self.janela, "Novo Jogo", self.janela.jogo.novoJogo, Estilos.PRETO, Estilos.BRANCO)

        self.botaoD = Elementos.criarBotao(self.janela, "Desligar", self.janela.app.destroy, Estilos.VERMELHO, Estilos.BRANCO)

        # Posicionando os botões



        Elementos.posicionarBotao(self.botao1, 0)
        Elementos.posicionarBotao(self.botao2, 1)
        Elementos.posicionarBotao(self.botao3, 2)
        # Elementos.posicionarBotao(self.botaoV, 3)
        Elementos.posicionarBotao(self.botaoS, 4)
        Elementos.posicionarBotao(self.botaoD, 5)


