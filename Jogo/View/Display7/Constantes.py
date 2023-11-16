import tkinter as tk
# from tkinter import ttk as tk
class Estilos:
    FUNDO = "#6e09e2"
    FRAME = "#AA7DE3"
    INFO = "#DE97FA"
    VERMELHO = "#FF0000"
    VERMELHOCL = "#FF2D00"
    AZUL = "#0000FF"
    AZULCL = "#0051FF"
    AMARELO = "#FFFF00"
    AMARELOCL = "#FFE000"
    BRANCO = "#FFFFFF"
    BRANCOCL = "#CCCCCC"
    PRETO = "#000000"
    PRETOCL = "#444444"
    BORDA = 2
    RELEVO = "sunken"
    FONTE = "Consolas"
    PADX = 2
    PADY = 2

class Elementos:
    """
    Classe com métodos para ajudar a criar os elementos com a mesma estilização
    """
    @staticmethod
    def criarBotao(janela, texto, corBotao, corTexto):
        """
        Cria elemento de botão já com o estilo correto
        :param janela: elemento de app
        :param texto: o texto do botão
        :param funcao: a função que será chamada pelo botão - sem ()
        :param argumento: argumento para funcao.
        :param corBotao: a cor do botão
        :param corTexto: a cor do texto
        :return:
        """
        return tk.Label(janela.frameOpcoes, text=texto, foreground=corTexto, background=corBotao,  padx=Estilos.PADX, pady=Estilos.PADY,font=janela.textoNormal)

    @staticmethod
    def posicionarBotao(botao):
        """
        Posicionar o botão
        :param botao: o botão criado
        :param pos: posição do botão
        :return:
        """

        botao.pack(fill=tk.BOTH, expand=1, side=tk.LEFT, padx=Estilos.PADX, pady=Estilos.PADY)
    @staticmethod
    def criarTitulo(janela, frame, titulo):
        """
        Criar um elemento de título já com os estilos
        :param janela: elemento de app
        :param frame: o frame onde o título vai ser posicionado
        :param titulo: o título
        :return:
        """
        return tk.Label(frame, text=titulo, font=janela.titulo,bg=Estilos.FRAME, foreground=Estilos.BRANCO, wraplength=janela.wrap, anchor="center")
    @staticmethod
    def posicionarTitulo(titulo):
        """
        Posicionar título
        :param titulo: o título criado
        :param pos: posicão
        :return:
        """
        titulo.pack(fill=tk.BOTH, expand=1, padx=Estilos.PADX, pady=Estilos.PADY)

    @staticmethod
    def criarTexto(janela, frame, texto):
        """
        Criar um elemento de texto já com estilso
        :param janela: elemento de app
        :param frame: frame onde o texto será posicionado
        :param texto: texto
        :return:
        """
        return tk.Label(frame, text=texto, font=janela.textoNormal, bg=Estilos.FRAME, foreground=Estilos.BRANCO, wraplength=janela.wrap, anchor="center")

    @staticmethod
    def posicionarTexto(texto):
        """
        Posiciona o texto
        :param texto: elemento de texto
        :param pos: posição
        :return:
        """
        texto.pack(fill=tk.BOTH, expand=1, padx=Estilos.PADX, pady=Estilos.PADY)
    @staticmethod
    def criarFrame(janela):
        """
        Cria um elemento de Frame já com os estilos
        :param janela: elemento de app
        :return:
        """
        return tk.Frame(janela.app, width=janela.larguraJanela, height=(janela.janelaLinha * 8), bg=Estilos.FRAME, borderwidth=Estilos.BORDA, relief=Estilos.RELEVO, takefocus=True)
    @staticmethod
    def posicionarFrame(frame):
        """
        Posiciona o frame
        :param frame: elemento de frame
        :param pos: posição
        :return:
        """
        frame.pack(fill=tk.BOTH, expand=1, padx=Estilos.PADX, pady=Estilos.PADY)
    @staticmethod
    def apagarElementoDaTela(elementos):
        """
        "Esquece" o elemento da tela para que ele possa ser alterado. Método para facilitar a alteração de telas e para facilitar caso se queira alterar o modo de geometria do Tkinter (place, pack, grid)
        :param elemento: array com os elemento a ser esquecido
        :return:
        """
        for elemento in elementos:
            # elemento.forget_pack()
            # elemento.grid_forget()
            elemento.forget()
