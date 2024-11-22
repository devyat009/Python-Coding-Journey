import sqlite3

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.create_table()

    def create_table(self):
        connect_data = self.connection.cursor()
        connect_data.execute("create table if not exists userdb(Id INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(50) NOT NULL, telefone varchar(40) NOT NULL, email varchar(50) NOT NULL, usuario varchar(40) NOT NULL, senha varchar(16) NOT NULL)")

    