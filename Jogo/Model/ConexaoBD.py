import sqlite3 # import da biblioteca para lidar com SQLite
import traceback # é uma boa biblioteca para fazer debugging

class ConexaoBD:
    """
    Está classe faz a conexão com a base de dados
    Atributos:
    ConexaoSQLite: conexão com o SQLite
    cursor: cursor para executar as buscas (queries)
    conectad: booleano que indica se há uma conexão
    """
    erro = ""
    def __init__(self):
        self.conectado = self.conectar()

    def conectar(self):
        """
        Faz a conexão com a base de dados
        :return: Booleano de sucesso (True) ou erro (False)
        """
        try:
            self.conexao = sqlite3.connect('db/zefa.sqlite')
            self.conexao.row_factory = sqlite3.Row
            self.cursor = self.conexao.cursor()
            print("A conexão com a base de dados foi um sucesso")
            return True

        except sqlite3.Error as erro:
            self.erro = erro
            print("Erro ao conectar ao sqlite", self.erro)
            return False



    def lerDados(self, sql):
        """
        Usada para ler dados quando o sql não usar variáveis
        """
        if(self.conectado):
            try:
                self.cursor.execute(sql)
                self.registros = self.cursor.fetchall()
                print("Os dados da base são: ")
                for registro in self.registros:
                    for chave in registro.keys():
                        print(f"Coluna: {chave} | Valor: {registro[chave]}")
                return self.registros
            except sqlite3.Error as erro:
                self.erro = erro
                print("Erro ao conectar ao sqlite", self.erro)
                return self.erro
        else:
            print(f"A conexão não existe: {self.erro}")
            return False


    def lerDadosParam(self, sqlParametrizado, parametros):
        """
        Com os atributos cursor faremos a busca (query) na base de dados

        :param: sqlParametrizado: sql já com os placeholders para os paramêtros. Ex: "select * from tabela where id = :id"
        :param: parametros: dict com os parâmetros, sendo as chaves os nomes dos paramêtros. Exemplo: {"id": 2}
        Mais informação: https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders
        :return: resultados ou erro
        """
        if(self.conectado):
            try:
                self.cursor.execute(sqlParametrizado, parametros)
                self.registros = self.cursor.fetchall()
                print("Os dados da base são: ")
                for registro in self.registros:
                    for chave in registro.keys():
                        print(f"Coluna: {chave} | Valor: {registro[chave]}")
                return self.registros
            except sqlite3.Error as erro:
                self.erro = erro
                print("Erro ao conectar ao sqlite", self.erro)
                return self.erro
        else:
            print(f"A conexão não existe: {self.erro}")
            return False

