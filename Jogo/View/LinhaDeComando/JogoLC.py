from Controller.FluxoDeJogoLC import FluxoDeJogoLC
class JogoLC:
    """
    Esta classe que cuida de como será feita a visualização do jogo na Linha de comando
    """
    def __init__(self):
        self.jogo = FluxoDeJogoLC(self)
        self.jogo.jogar()



    def mostraNovoJogo(self, caso, tarefa, tempo):
        """
        Imprime a informação de um novo jogo
        :param caso:
        :param tarefa:
        :param tempo:
        :return:
        """
        print("\n/**********************/")
        print("Cadê a Zefa?")
        print("/**********************/\n")
        print("A notória ladra internacional de origem brasileira, Zefa da Silva, está foragida desde 1983 quando ajudou seu pai a roubar a taça Jules Rimet com a tenra idade de 10 anos. Desde então ela tem aplicado roubos cada vez mais ousados pelo Brasil e o mundo e a nossa dedicada PF nunca deixou de persegui-la décadas afora. Será você a pessoa que finalmente irá aprender está elusiva ladra? Boa sorte!")
        print("/**********************/\n")
        print(caso)
        print(tarefa)
        print(f"Você tem {tempo} horas para apreender a Zefa! Boa sorte!")
        print("/**********************/\n")
    def mostraInfo(self, infoTitulo, info):
        print("\n/**********************/")
        print(infoTitulo)
        print("/**********************/\n")
        print(info)

    def mostraOpcoes(self, titulo, opcoes):
        """
        Imprimime as opcões que podem ser escolhidas
        :return:
        """
        print("\n/**********************/")
        print(titulo)
        print("/**********************/\n")
        contador = 1
        for opcao in opcoes:
            print(f"{contador} - {opcao}")
            contador += 1

    def mostraGanhou(self, vitoria, pontuacao):
        """
        Imprime o texto de vitória e a pontuação
        :param vitoria:
        :param pontuacao:
        :return:
        """
        print("\n/**********************/")
        print(vitoria)
        print("\n/**********************/")
        print(f"YAY! Você ganhou! Parabéns! Sua pontuação foi de {pontuacao} pontos")
        print("/**********************/\n")

    def mostraPerdeu(self):
        print("\n/**********************/")
        print("Ah, que pena. Você extrapolou o tempo de jogo. Mas não se preocupe, você pode tentar novamente com outro caso!")
        print("\n/**********************/")

    def mostraMenu(self):
        """
        Imprime as opções principais
        :return:
        """
        print("\n/**********************/")
        print("Digite a opção:\n1 - Investigar\n2 - Viajar\n3 - Ver Destinos\nE a qualquer momento digite: \ns - Novo Jogo\nd - Desligar")
        print("\n/**********************/")

    def mostraInfoTranslado(self, tempo, destino):
        if tempo == 1:
            texto = "hora"
        else:
            texto = "horas"
        print(f"Você vai levar {tempo} {texto} para chegar a {destino}")
    def mostraTempoRestante(self, tempo, tempoJogo):
        if tempo == 1:
            texto = "hora"
        else:
            texto = "horas"
        print(f"Você acaba de viajar {tempo} {texto}. Você só tem {tempoJogo} horas para achar a Zefa")

    def mostraDormir(self, tempoJogado):
        print("Está na hora de dormir. Bons sonhos!")
        for x in range(5):
            print("ZZZZZ...")
        if tempoJogado == 1:
            texto = "hora"
        else:
            texto = "horas"
        print(f"Bom dia. Você só tem {tempoJogado} {texto} para achar a Zefa. Vamos ver se ainda dá tempo?")

    def temTempo(self, tempoJogado):
        if tempoJogado == 1:
            texto = "hora"
        else:
            texto = "horas"
        print(f"Ufa, você ainda tem {tempoJogado} {texto}. Corre lá.")

    def escolhaIvalida(self):
        print("Essa escolha não é válida. Favor entrar um dos valores válidos.")


