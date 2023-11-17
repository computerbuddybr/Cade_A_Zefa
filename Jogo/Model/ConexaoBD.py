import sqlite3 # import da biblioteca para lidar com SQLite
import traceback # é uma boa biblioteca para fazer debugging

class ConexaoBD:
    """
    Faz a conexão com a base de dados
    Atributos:
    ConexaoSQLite: conexão com o SQLite
    cursor: cursor para executar as buscas (queries)
    """
    erro = ""
    def __init__(self):
        self.conectado = self.conectar()
        pass
    """
    Aqui abrimos a conexão com a base de dados e criamos o atributo cursor que será usado para executar as buscas (queries)
    """
    def conectar(self):
        """
        Faz a conexão com a base de dados
        :return: Booleano de sucesso (True) ou erro (False)
        """
        try:
            self.conexao = sqlite3.connect('db/zefa.sqlite')
            self.cursor = self.conexao.cursor()
            print("A conexão com a base de dados foi um sucesso")
            return True

        except sqlite3.Error as erro:
            self.erro = erro
            print("Erro ao conectar ao sqlite", self.erro)
            return False


    """
    Com os atributos cursor faremos a busca (query) na base de dados
    """
    def lerDados(self, sql):
        # if(self.conectado):
        #     with self.conexao.cursor() as cursor:
        #         cursor.execute(sql)
        #         self.registros = cursor.fetchall()
        #         print("Os dados da base são: ")
        #         print(self.registros)
        #         return self.registros
        # else:
        #     print(f"A conexão não existe: {self.erro}")
        #     return False
        try:
            self.cursor.execute(sql)
            self.registros = self.cursor.fetchall()
            print("Os dados da base são: ")
            print(self.registros)
            return self.registros
        except sqlite3.Error as erro:
            self.erro = erro
            print("Erro ao conectar ao sqlite", self.erro)
            return self.erro


    def lerDadosParam(self, sqlParametrizado, parametros):
        """
        Com os atributos cursor faremos a busca (query) na base de dados

        :param: sqlParametrizado: sql já com os placeholders para os paramêtros. Ex: "select * from tabela where id = :id"
        :param: parametros: tupla com os parâmetros. Caso haja só um parâmetro, colocar entre parênteses e uma vírgula após o elemento para o Python entender que é uma tupla
        :return: resultados ou erro
        """
        if(self.conectado):
            try:
                self.cursor.execute(sqlParametrizado, parametros)
                self.registros = self.cursor.fetchall()
                print("Os dados da base são: ")
                print(self.registros)
                return self.registros
            except sqlite3.Error as erro:
                self.erro = erro
                print("Erro ao conectar ao sqlite", self.erro)
                return self.erro
        else:
            print(f"A conexão não existe: {self.erro}")
            return False

