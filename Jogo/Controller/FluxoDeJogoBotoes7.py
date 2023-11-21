from Model.Jogo import Jogo
from Controller.FluxoDeJogoComp import FluxoDeJogoComp
# import RPi.GPIO as pi
class FluxoDeJogoBotoes7(FluxoDeJogoComp):
    """
    Classe que controla o fluxo do jogo
    """

    def __init__(self, janela):
        """
        Inicia o jogo
        """
        self.definicaoBotoes() # Preciso definir os botões antes de rodar o super, pois o construtor da classe mãe roda enquanto o botão desligar não tiver sido apertado
        # self.janela = janela
        # self.jogo = Jogo()
        super().__init__(janela)

    def definicaoBotoes(self):
        # pi.setmode(pi.BOARD)  # Configurando o tipo de leitura dos Pinos. Neste caso usando os números do GPIO
        # pi.setwarnings(False) # Desabilita avisos
        # Definindo em que pino está cada um - repare como as minhas chaves são exatamente o mesmo que eu espero na Linha de Comando. Desse modo só vou precisar alterar o método de entrada. Mas não o valor da entrada em si
        self.botoes = {
            "1": 40,
            "2": 38,
            "3": 36,
            "v": 32,
            "s": 37,
            "d": 35,

        }

        # Configurando os pinos como entrada com Pull-up
        # for botao in self.botoes.values():
        #     pi.setup(botao, pi.IN, pi.PUD_UP)





    def lerBotoes(self):
        """
        Lê um botão
        :param botao: o número de pino do botão
        :return:
        """
        while True:
            # Fazendo um loop pelos botões. Uso o número do pino para ler e retorno a chave
            for botao, gpio in self.botoes.items():
                if pi.input(gpio) == 0:
                    print(f"Apertei botao {botao}")
                    return botao

    def invocandoBotao(self, botao):
        """
        Esta função vai incovar o botão desejado
        """
        botao.invoke() # vai chamar a ação do botão
    def escolha(self, possibilidades, jbotoes):
        """
        Checa se a escolha feita está dentro das possibilidades, se não continua esperando resposta
        :param: possibilidades: array com as possibilidades de botões
        :param: jbotoes: o dicionário de botões da janela
        :return:
        """
        print("Possibilidades")
        print(possibilidades)
        valido = False
        while valido != True:
            # Está é a única linha de código diferente nesta função. O método pelo qual leio a minha escolha
            # self.opcao = self.lerBotoes()
            self.opcao = self.lcTeste()
            print(f"Escolha {self.opcao}")
            valido = self.opcao in possibilidades
            if valido == False:
                print("Escolha inválida, favor escolher outra opção")
            else:
                self.invocandoBotao(jbotoes[self.opcao])

    def lcTeste(self):
        """
        Função para testes da linha de comando
        :return:
        """
        print("Digite a sua escolha:")
        return input()

