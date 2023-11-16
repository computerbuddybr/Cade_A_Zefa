import random
class Local:
    """
    @param tipoPista = 1 - pista real, 2 - pista local falso, 3 - pista local final
    """
    def __init__(self, conexaoBD, id, local, bandeira, pistaCidade, moeda):
        self.zefaEstaAqui = False
        self.conexaoBD = conexaoBD
        self.id = id
        self.local = local
        self.bandeira = bandeira
        self.pistaCidade = pistaCidade
        self.moeda = moeda
        self.personagem = ""
        self.criarPersonagem()






    def criarPersonagem(self):
        sql = f"select * from personagens as p INNER JOIN local_personagem as lp on (p.pk_id_personagem = lp.fk_id_personagem) where fk_id_local = {self.id}"
        personagens = self.conexaoBD.lerDados(sql)
        # print(curiosidades)
        quantidadeDePersonagens = len(personagens)
        indice = 0
        if quantidadeDePersonagens > 0:
            if quantidadeDePersonagens > 1:
                indice = random.randint(0, quantidadeDePersonagens - 1)
                # print("Pra saber o indice")
                # print(personagens[indice])
            self.personagem = personagens[indice][1]
        else:
            self.personagem = "Não há um personagem com esse id"


    def criaPistaBandeira(self, bandeira, imagem):
        if self.local == "Aeroporto":
            veiculo = "O avião que ela embarcou tinha"
        elif self.local == "Estação de ônibus":
            veiculo = "Ela pegou um ônibus com"
        else:
            veiculos = ["Ela foi embora em um carro com", "Ela partiu disparada em uma moto com"]
            veiculo = veiculos[random.randint(0,1)]
        if imagem == True:
            self.pista = f"{veiculo} uma bandeira com {bandeira}"
        else:
            self.pista = f"{veiculo} uma bandeira {bandeira}"

        print(f"A pista da bandeira para {self.local} é: {self.pista}")

    def criarPistaMoeda(self, moeda):
        self.pista = f"Só sei que ela comprou {moeda}"
        print(f"A pista da moeda para {self.local} é: {self.pista}")

    def criarPistaCidade(self, destino):
        print("Chamou o criar Pista Cidade")
        print(f"O id de destino no criar pista cidade é: {destino.cidade}")
        print("Pistas da cidade de destino")
        print(destino.pistasCidade)
        quantidadeDePistas = len(destino.pistasCidade)
        if(quantidadeDePistas > 0):
            indice = random.randint(0, quantidadeDePistas - 1)
            print(f"Random int pista cidade: {indice}")
            self.pista = destino.pistasCidade[indice]
        else:
            self.pista = "Não há pistas para esta cidade"

        print(f"A pista da cidade para {self.local} é: {self.pista}")




    def criarPistaFalsa(self):
        naoVi = ["Nunca vi alguém assim.", "Nunca vi essa pessoa.", "Não conheço não.", "Você tem certeza que ela esteve aqui?", "Acho que você se enganou, não passou ninguém assim por aqui.", "Quem?", "Tô sabendo de nada não.", "Acho que você está na pista errada."]
        self.pista = f"{self.personagem}:  {naoVi[random.randint(0, len(naoVi) - 1)]}"
        print(f"A pista da falsa para {self.local} é: {self.pista}")

    def criarPistaCidadeFinal(self):
        cuidado = ["Se eu fosse você eu tomava cuidado.", "A Zefa já está sabendo que você está atrás dela e não está feliz.", "Tem uma recompensa pela sua cabeça.", "Você está cutucando vespeiro", "Não me envolve nisso, não quero rolo pro meu lado.", "Se eu fosse você fugia.", "Some daqui, não quero saber de problemas."]
        self.pista = f"{cuidado[random.randint(0, len(cuidado) - 1)]}"
        print(f"A pista da cidade final para {self.local} é: {self.pista}")

    def criarPistaPrendeuAZefa(self):
        self.pista = "Parabéns! Você capturou a Zefa!"
        self.zefaEstaAqui = True
        self.localFinal = True
        print(f"A pista de prendeu a Zefa para {self.local} é: {self.pista}")

