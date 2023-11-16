# Importando a classe de controlador de Jogo
from Controller.FluxoDeJogoBotoes7 import FluxoDeJogoBotoes7
# Importando a classe com os Estilos a ser usados e a classe para a criação dos elementos da janela
from View.Display7.Constantes import Estilos, Elementos
# Importamos a biblioteca tkinter para fazer as interfaces gráficas
import tkinter as tk
#Para usar temas
from tkinter import ttk
# Para usar fontes
from tkinter import font
## Importando as outras Views
from View.Display7.InfoComEscolha import InfoComEscolha
from View.Display7.InfoSemEscolha import InfoSemEscolha
from View.Display7.Info import Info
from View.Display7.Menu import Menu
from View.Display7.Inicio import Inicio
class Display7:
    """
    Classe que lida com a janela principal para o Display de 7"
    """
    def __init__(self):
        """
        Construtor que inicia a janela de jogo e todos seus elementos
        """
        # Iniciando o jogo
        self.jogo = FluxoDeJogoBotoes7(self)

        self.imagemFundo = ""
        # Criando a janela
        self.app = tk.Tk()
        # Atribuindo título a janela
        self.app.title("Cadê a Zefa, gente!")
        # Atribuindo uma cor de fundo a janela
        self.app.configure(background=Estilos.FUNDO)
        ## Descobrindo a altura e largura da janela para poder posicionar nossos elementos
        # self.larguraJanela = self.app.winfo_screenwidth()
        # self.alturaJanela = self.app.winfo_screenheight()
        self.larguraJanela = 1240
        self.alturaJanela = 600
        # Quebrando a janela em um Grid
        self.janelaColuna = self.larguraJanela / 24
        self.janelaLinha = (self.alturaJanela / 24) - 10

        # Definindo o wrap do texto
        self.wrap = self.larguraJanela - Estilos.PADX
        print(f"Largura da janela: {self.larguraJanela}")
        print(f"Altura da janela: {self.alturaJanela}")
        print(f"Altura da linha: {self.janelaLinha}")
        # Com geometry eu dou um tamanho e posiciono a janela.
        self.app.geometry(f"{self.larguraJanela}x{self.alturaJanela}+0+0")
        # Define a janela como sendo fullscreen. Como nosso interesse é fazer um emulador que em teoria teria somente este jogo, é interessante pois não vai aparecer aqueles tradicionais botões de janela do sistema operacional. Porém é meio chato na hora de programar porque ocupa tudo. Por isso o método acima para a hora da programação. E trocar no deploy
        # self.app.attributes('-fullscreen',True)
        # Definindo o ícone da janela
        self.app.iconbitmap(default="recursos/imagens/zefa.ico")

        # Criando as fontes que quero usar
        self.titulo = font.Font(weight="bold", family=Estilos.FONTE, size=32, slant="italic")
        self.tituloNormal = font.Font(weight="bold", family=Estilos.FONTE, size=24)
        self.negrito = font.Font(weight="bold", family=Estilos.FONTE, size=24)
        self.textoNormal = font.Font(family=Estilos.FONTE, size=24)

        #Aqui vou criar três frames principais de informação
        # Informação
        # Botões - Opcoes
        # Tempo De Jogo Restante
        self.frameJogo = Elementos.criarFrame(self)
        self.frameOpcoes = Elementos.criarFrame(self)
        self.frameTempo = Elementos.criarFrame(self)


        # Agora tenho que posicionar os frames
        Elementos.posicionarFrame(self.frameJogo)
        Elementos.posicionarFrame(self.frameOpcoes)
        Elementos.posicionarFrame(self.frameTempo)


        # Agora vou criar as caixas de texto para a informação de tempo de jogo
        self.tituloTempo = Elementos.criarTitulo(self, self.frameTempo, "Tempo remanescente:")
        self.tempo = Elementos.criarTitulo(self,self.frameTempo,f"{self.jogo.jogo.tempoJogado}")

        Elementos.posicionarTitulo(self.tituloTempo)
        Elementos.posicionarTitulo(self.tempo)


        # Quero simplesmente iniciar minhas janelas investigar, viajar, destinos, e info mas não mostrar ela ainda ou passar informação
        self.janelaInvestigar = InfoComEscolha(self, "investigar")
        self.janelaDestinos = InfoSemEscolha(self)
        self.janelaViajar = InfoComEscolha(self, "viajar")
        self.janelaInfo = Info(self)
        self.janelaMenu = Menu(self)
        self.janelaInicio = Inicio(self)

        # Aqui eu coloco uma função que via executar depois do mainloop

        self.jogo.iniciarJogo()  # Você passa o tempo que ele vai esperar para chamar a função e depois o callback
        # Aqui eu tenho que iniciar o loop da janela

        self.app.mainloop()




    def limparTudo(self):
        """
        Limpa todos os elemetos da tela para poder colocar os novos
        :return:
        """
        self.janelaInvestigar.limparTudo()
        self.janelaViajar.limparTudo()
        self.janelaDestinos.limparTudo()
        self.janelaInfo.limparTudo()
        self.janelaMenu.limparTudo()
        self.janelaInicio.limparTudo()

    def atualizarTempo(self, info):
        """
            Atualiza a informação de tempo
            :return:
        """
        # self.tempo.grid_forget()
        Elementos.apagarElementoDaTela([self.tempo])

        self.tempo = Elementos.criarTitulo(self, self.frameTempo,f"{info} {self.jogo.jogo.tempoJogado}")
        Elementos.posicionarTitulo(self.tempo)








