from View.LinhaDeComando.JogoLC import JogoLC
from Controller.FluxoDeJogoLC import FluxoDeJogoLC
class LinhaDeComando:
    """
    Classe que roda o jogo na linha de comando
    """
    def __init__(self):
        ##Criando o jogo
        self.view = JogoLC()
        self.jogo = FluxoDeJogoLC(self.view)
        self.jogo.jogar()

