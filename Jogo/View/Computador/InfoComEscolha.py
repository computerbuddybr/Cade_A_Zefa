from View.Computador.Constantes import Estilos, Elementos
from time import sleep
import tkinter as tk
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

        # self.mostrarInstrucoes(self.titulo, self.texto)
        # self.criandoBotoes()
        #
        # self.limparTudo()



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
        Elementos.posicionarTitulo(self.titulo, 0)
        Elementos.posicionarTexto(self.info, 1)



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
            Elementos.apagarElementoDaTela([self.titulo, self.info, self.botao1, self.botao2, self.botao3, self.botaoV, self.botaoS, self.botaoD])
            self.on = False

    def mensagemRapida(self, titulo, texto):
        """
        Trocar a mensagem durante deslocamentos e dormir
        :param titulo:
        :param texto:
        :return:
        """
        self.titulo.configure(text=titulo)
        self.info.configure(text=texto)

    def trocarInfo(self, titulo, texto):
        self.limparInfo()
        self.mostrarInstrucoes(titulo, texto)

    def deslocar(self, opcao):

        if self.tipo == "investigar":
            self.localDestino = self.janela.jogo.jogo.cidadeAtual.locais[opcao].local
            self.tempoViagem = 1
            if self.testarTempo() == False:
                return
            self.trocarInfo(self.janela.jogo.jogo.cidadeAtual.locais[opcao].local, f"{self.janela.jogo.jogo.cidadeAtual.locais[opcao].personagem}: {self.janela.jogo.jogo.cidadeAtual.locais[opcao].pista}")

            # Vendo se ganhou
            if self.janela.jogo.jogo.cidadeAtual.locais[opcao].zefaEstaAqui:
                self.janela.jogo.ganhou()

        else:

            #
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
        self.botao1 = Elementos.criarBotao(self.janela, self.opcoes[0], lambda: self.deslocar(0), Estilos.AMARELO, Estilos.PRETO)

        self.botao2 = Elementos.criarBotao(self.janela, self.opcoes[1], lambda: self.deslocar(1), Estilos.BRANCO, Estilos.PRETO)

        self.botao3 = Elementos.criarBotao(self.janela, self.opcoes[2], lambda: self.deslocar(2), Estilos.AZUL, Estilos.BRANCO)

        self.botaoV = Elementos.criarBotao(self.janela, "Voltar", self.janela.jogo.voltar, Estilos.AZUL, Estilos.BRANCO)

        self.botaoS = Elementos.criarBotao(self.janela, "Novo Jogo", self.janela.jogo.novoJogo, Estilos.PRETO, Estilos.BRANCO)

        self.botaoD = Elementos.criarBotao(self.janela, "Desligar", self.janela.app.destroy, Estilos.VERMELHO, Estilos.BRANCO)

        # Posicionando os botões



        Elementos.posicionarBotao(self.botao1, 0)
        Elementos.posicionarBotao(self.botao2, 1)
        Elementos.posicionarBotao(self.botao3, 2)
        Elementos.posicionarBotao(self.botaoV, 3)
        Elementos.posicionarBotao(self.botaoS, 4)
        Elementos.posicionarBotao(self.botaoD, 5)








