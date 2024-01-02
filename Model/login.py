import config as con

class LoginModel:

    def __init__(self):
        self.cursor = con.conexao.cursor()

    def BuscarLogin(self):
        comando = f'SELECT * FROM vendas'

        self.cursor.execute(comando)

        resultado = self.cursor.fetchall() 
        
        self.cursor.close()
        con.conexao.close()

        return resultado



