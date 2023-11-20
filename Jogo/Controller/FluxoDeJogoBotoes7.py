from Model.Jogo import Jogo
# import RPi.GPIO as pi # Biblioteca de Raspberry Pi para leitura do GPIo (https://pypi.org/project/RPi.GPIO/)
espera = 100
class FluxoDeJogoBotoes7():
    """
    Classe filha da classe FluxoDeJogo com alterações necerrárias para receber a entrada dos botões  físicos e não do teclado usando a biblioteca Rpi.GPIO
    """
    def __init__(self, janela):
        self.definicaoBotoes() # Preciso definir os botões antes de rodar o super, pois o construtor da classe mãe roda enquanto o botão desligar não tiver sido apertado
        self.jogo = Jogo()
        self.opcao = ""
        self.janela = janela




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
    def escolha(self, tipoMenu, menu):
        """
        Checa se a escolha feita está dentro das possibilidades, se não continua esperando resposta
        :return:
        """
        print("Na função escolha:")
        print("Tipo menu: ", tipoMenu)
        print("função de menu: ", menu)
        if tipoMenu == "simples":
            possibilidades = ["v", "s", "d"]
        elif tipoMenu == "final":
            possibilidades = ["s", "d"]
        elif tipoMenu == "menu":
            possibilidades = ["1", "2", "3", "s", "d"]
        else:
            possibilidades = ["1", "2", "3", "s", "d", "v"]
        print("Possibilidades")
        print(possibilidades)
        # possibilidades = ["1", "2", "3", "s", "d", "v"]
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
                menu(self.opcao)

    def lcTeste(self):
        """
        Função para testes da linha de comando
        :return:
        """
        print("Digite a sua escolha:")
        return input()





    def iniciarJogo(self):
        """
        Inicia o jogo
        :return:
        """
        # Começa a janela inicial de jogo
        self.janela.janelaInicio.reiniciar()
        self.janela.app.after(espera, lambda: self.escolha("simples", self.menuInicio))


    def menuInicio(self, escolha):
        print("Menu inicio")
        print("Escolhas: v,s,d")
        if escolha == "v":
            print("Começar jogo")
            self.jogar()
            return
        if escolha == "s":
            print("Novo Jogo")
            self.novoJogo()
            return
        if escolha == "d":
            print("Desligar")
            self.janela.app.destroy()
            return

    def menuJogo(self, escolha):
        print("Menu Jogo")
        print("Escolhas: 1,2,3 ,s,d")
        if escolha == "1":
            print("Investigar")
            self.investigar()
            return
        if escolha == "2":
            print("Viajar")
            self.viajar()
            return
        if escolha == "3":
            print("Destinos")
            self.destinos()
            return
        if escolha == "v":
            print("Voltar")
            self.voltar()
            return
        if escolha == "s":
            print("Novo Jogo")
            self.novoJogo()
            return
        if escolha == "d":
            print("Desligar")
            self.janela.app.destroy()
            return

    def menuInvestigar(self, escolha):
        print("Menu Investigar")
        print("Escolhas: 1,2,3 v,s,d")
        if escolha == "1":
            print("Deslocar para 0")
            self.investigando(0)
            return
        if escolha == "2":
            print("Deslocar para 1")
            self.investigando(1)
            return
        if escolha == "3":
            print("Deslocar para 2")
            self.investigando(2)
            return
        if escolha == "v":
            print("Voltar")
            self.voltar()
            return
        if escolha == "s":
            print("Novo Jogo")
            self.novoJogo()
            return
        if escolha == "d":
            print("Desligar")
            self.janela.app.destroy()
            return

    def investigando(self, escolha):
        """
        Chamado pelo menu investigar. Faz o deslocamento e chama a alteração para informação de pista e lógica de descolcamento e no final traz o menu Investigar
        :param escolha:
        :return:
        """
        self.janela.janelaInvestigar.deslocar(escolha)
        self.janela.app.after(espera, lambda: self.escolha("opcoes", self.menuInvestigar))




    def menuViajar(self, escolha):
        print("Menu Viajar")
        print("Escolhas: 1,2,3 v,s,d")
        if escolha == "1":
            print("Viajar para 0")
            self.viajando(0)
            return
        if escolha == "2":
            print("Viajar para 1")
            self.viajando(1)
            return
        if escolha == "3":
            print("Viajar para 2")
            self.viajando(2)
            return
        if escolha == "v":
            print("Voltar")
            self.voltar()
            return
        if escolha == "s":
            print("Novo Jogo")
            self.novoJogo()
            return
        if escolha == "d":
            print("Desligar")
            self.janela.app.destroy()
            return
    def viajando(self, escolha):
        """
        Chamado pelo menu viajar. Faz o deslocamento e chama a alteração para informação de pista e lógica de descolcamento e no final traz o menu Investigar
        :param escolha:
        :return:
        """
        self.janela.janelaViajar.deslocar(escolha)

    def menuDestinos(self, escolha):
        print("Menu Destinos")
        print("Escolhas: 1,2,3 v,s,d")
        if escolha == "v":
            print("Começar jogo")
            self.voltar()
            return
        if escolha == "s":
            print("Novo Jogo")
            self.novoJogo()
            return
        if escolha == "d":
            print("Desligar")
            self.janela.app.destroy()
            return
    def menuFinal(self, escolha):
        print("Menu Final")
        print("Escolhas: s,d")
        if escolha == "s":
            print("Novo Jogo")
            self.novoJogo()
            return
        if escolha == "d":
            print("Desligar")
            self.janela.app.destroy()
            return

    def jogar(self):
        self.janela.limparTudo()
        self.janela.janelaMenu.reiniciar(f"Bem vindo a {self.jogo.cidadeAtual.cidade}", self.jogo.cidadeInicial.curiosidade)
        self.janela.app.after(espera, lambda: self.escolha("menu", self.menuJogo))

    def investigar(self):
        self.janela.limparTudo()
        opcoes = []
        for opcao in self.jogo.cidadeAtual.locais:
            opcoes.append(opcao.local)
        self.janela.janelaInvestigar.reiniciar(f"Clique em uma das opções abaixo para começar a investigar na cidade de {self.jogo.cidadeAtual.cidade}", "Não se esqueça, deslocamentos dentro da cidade levam 1 hora!", opcoes)
        # self.escolha("opcoes", self.menuInvestigarOuViajar)
        self.janela.app.after(espera, lambda: self.escolha("opcoes", self.menuInvestigar))
    def viajar(self):
        print("Viajar")
        self.janela.limparTudo()
        opcoes = []
        tempoDeVoo = ""

        for opcao in self.jogo.cidadeAtual.cidadesDeDestino:
            tempoDeVoo += f"\n{opcao.cidade}: {self.jogo.cidadeAtual.calcularTempoDeVoo(opcao)} horas de voo."

            opcoes.append(opcao.cidade)
        # self.janela.janelaViajar.reiniciar("Para onde quer viajar? ", "Seu tempo de viagem será de 10 horas.", opcoes)
        self.janela.janelaViajar.reiniciar("Para onde quer viajar? ", tempoDeVoo, opcoes)
        print("Destinos")
        # self.escolha("opcoes", self.menuInvestigarOuViajar)
        self.janela.app.after(espera, lambda: self.escolha("opcoes", self.menuViajar))
    def destinos(self):
        self.janela.limparTudo()
        opcoes = []
        for opcao in self.jogo.cidadeAtual.cidadesDeDestino:
            opcoes.append(opcao.cidade)
        self.janela.janelaDestinos.reiniciar("Você pode viajar para: ", opcoes)
        print("Destinos")
        # self.escolha("simples", self.menuDestinos)
        self.janela.app.after(espera, lambda: self.escolha("simples", self.menuDestinos))

    def voltar(self):
        print("Voltar")
        self.janela.limparTudo()
        self.janela.janelaMenu.reiniciar(self.jogo.cidadeAtual.cidade, "Qual seu próximo passo? Clique em um dos botões abaixo para escolher.")
        # self.escolha("opcoes", self.menuJogo)
        self.janela.app.after(espera, lambda: self.escolha("menu", self.menuJogo))

    def novaCidade(self, cidade):
        self.jogo.cidadeAtual = cidade
        print("Nova cidade")
        self.janela.limparTudo()
        self.janela.janelaMenu.reiniciar(self.jogo.cidadeAtual.cidade, self.jogo.cidadeAtual.curiosidade)
        # self.escolha("opcoes", self.menuJogo)
        self.janela.app.after(espera, lambda: self.escolha("menu", self.menuJogo))

    def acabouJogo(self):
        print("Acabou o jogo")
        self.janela.limparTudo()
        self.janela.janelaInfo.reiniciar("Que pena! Acabou seu tempo!", "Mas não desanime, você ainda terá outras oportunidades de capturar a Zefa!")
        # self.escolha("final", self.menuFinal())
        self.janela.app.after(espera, lambda: self.escolha("final", self.menuFinal))
    def ganhou(self):
        print("Ganhou")
        self.janela.limparTudo()
        self.janela.janelaInfo.reiniciar("Eba! Você capturou a Zefa com sucesso!", self.jogo.cidadeInicial.vitoriaCaso)
        self.escolha("final", self.menuFinal)
        self.janela.app.after(espera, lambda: self.escolha("final", self.menuFinal))
    def novoJogo(self):
        self.janela.limparTudo()
        self.jogo = Jogo()
        self.janela.atualizarTempo("")
        self.iniciarJogo()

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
            print("Hora de dormir")
            self.jogo.tempoJogado -= 8
            self.jogo.acordouEm = self.jogo.tempoJogado
            self.janela.atualizarTempo(f"{self.infoTempo}:")
            if self.jogo.tempoJogado <= 0:
                return 1
            return 2
        return 0
