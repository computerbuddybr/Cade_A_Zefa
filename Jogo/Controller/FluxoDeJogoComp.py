from Model.Jogo import Jogo
class FluxoDeJogoComp:
    """
    Classe que controla o fluxo do jogo
    """

    def __init__(self, janela):
        """
        Inicia o jogo
        """
        self.janela = janela
        self.jogo = Jogo()



    def iniciarJogo(self):
        # Apaga a variável jogo anterior dando o valor None, ou Nulo para
        #self.jogo = 0
        self.jogo = Jogo()
        # Imprime a informação de um jogo novo
        self.janela.janelaInicio.reiniciar()




    def investigar(self):
        self.janela.limparTudo()
        opcoes = []
        for opcao in self.jogo.cidadeAtual.locais:
            opcoes.append(opcao.local)
        self.janela.janelaInvestigar.reiniciar(f"Clique em uma das opções abaixo para começar a investigar na cidade de {self.jogo.cidadeAtual.cidade}", "Não se esqueça, deslocamentos dentro da cidade levam 1 hora!", opcoes)

        print("Investigar")
    def viajar(self):
        print("Viajar")
        self.janela.limparTudo()
        opcoes = []
        tempoDeVoo = ""

        for opcao in self.jogo.cidadeAtual.cidadesDeDestino:
            tempoDeVoo += f"\n{opcao.cidade}: {self.jogo.cidadeAtual.calcularTempoDeVoo(opcao)} horas de voo."

            opcoes.append(opcao.cidade)
        self.janela.janelaViajar.reiniciar("Para onde quer viajar? ", tempoDeVoo, opcoes)
        print("Destinos")
    def destinos(self):
        self.janela.limparTudo()
        opcoes = []
        for opcao in self.jogo.cidadeAtual.cidadesDeDestino:
            opcoes.append(opcao.cidade)
        self.janela.janelaDestinos.reiniciar("Você pode viajar para: ", opcoes)
        print("Destinos")

    def voltar(self):
        print("Voltar")
        self.janela.limparTudo()
        self.janela.janelaMenu.reiniciar(self.jogo.cidadeAtual.cidade, "Qual seu próximo passo? Clique em um dos botões abaixo para escolher.")

    def novaCidade(self, cidade):
        self.jogo.cidadeAtual = cidade
        print("Nova cidade")
        self.janela.limparTudo()
        self.janela.janelaMenu.reiniciar(self.jogo.cidadeAtual.cidade, self.jogo.cidadeAtual.curiosidade)

    def acabouJogo(self):
        print("Acabou o jogo")
        self.janela.limparTudo()
        self.janela.janelaInfo.reiniciar("Que pena! Acabou seu tempo!", "Mas não desanime, você ainda terá outras oportunidades de capturar a Zefa!")
    def ganhou(self):
        print("Ganhou")
        self.janela.limparTudo()
        self.janela.janelaInfo.reiniciar("Eba! Você capturou a Zefa com sucesso!", self.jogo.cidadeInicial.vitoriaCaso)
    def novoJogo(self):
        self.janela.limparTudo()
        self.iniciarJogo()
        self.janela.atualizarTempo("")
        print("Novo jogo")


    def deslocar(self, tempoViagem, local):
        """
        Se desloca e checa se o jogo pode continuar
        :param tempoViagem: tempo gasto no deslocamento
        :return: False se acabou o tempo de jogo True se pode continuar
        """

        self.jogo.tempoJogado -= tempoViagem
        self.infoTempo = f"Tempo depois do deslocamento para {local}"
        self.janela.atualizarTempo(f"{self.infoTempo}:")
        if self.jogo.tempoJogado <= 0:
            return False
        return True
    def dormir(self):
        """
        Verifica se tem que dormir. Se sim, desconta o tempo e checa se acabou o tempo
        :return: 0 - Não precisou dormir
        :return: 1 - Precisou dormir e acabou o tempo (deve mostrar dormir e depois a mensagem de que acabou o tempo
        :return: 2 -Precisou dormir e não acabou o tempo deve mostrar a mensagem de dormir e voltar ao fluxo de jogo
        """

        if self.jogo.acordouEm - self.jogo.tempoJogado >= 16:
            self.infoTempo += " e de dormir"
            self.jogo.tempoJogado -= 8
            self.jogo.acordouEm = self.jogo.tempoJogado
            self.janela.atualizarTempo(f"{self.infoTempo}:")
            if self.jogo.tempoJogado <= 0:
                return 1
            return 2
        return 0
