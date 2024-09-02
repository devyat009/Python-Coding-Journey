import mysql.connector
from mysql.connector import Error

class MySQLConnection():
    def __init__(self):
        try: 
            self.connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='cadastro')
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
            else:
                print('Não foi possível conectar')
        except Error as e:
            print(f'Erro ao conectar ao MySQL: {e}')
        except Exception as e:
            print(f"Um erro ocorreu: {e}")

    def add_item(self, data1, data2):
        # Query
        query = f'INSERT INTO vendas (produto, preco) values ("{data1}", "{data2}")'
        self.cursor.execute(query)

    def read_table(self):
        try:
            # Print
            command = f'SELECT * FROM VENDAS'
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            if result:
                for i in result: # Laço para imprimir linha por linha
                    print(i)
            else:
                print('Nada foi encontrado na tabela...')
        except Error as e:
            print(f'Erro ao ler dados do MySQL: {e}')
        except Exception as e:
            print(f'Erro ao ler tabela: {e}')

    def update_table(self, target, value):
        command = f'UPDATE VENDAS SET preco = "{value}" WHERE PRODUTO = "{target}"'
        self.cursor.execute(command)

    def delete_item(self, target):
        command = f'DELETE FROM VENDAS WHERE idVendas = "{target}"'
        self.cursor.execute(command)

    def commit_changes(self):
        self.connection.commit()

    def close_database(self):
        # Fecha a conexão
        self.cursor.close()
        self.connection.close()