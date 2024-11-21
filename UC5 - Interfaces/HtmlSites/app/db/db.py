import sqlite3

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.create_table()

    def create_table(self):
        connect_data = self.connection.cursor()
        connect_data.execute("create table if not exists userdb(Id int auto_increment primary key not null, nome varchar(50) not null, telefone varchar(40) not null, email varchar(50) not null, usuario varchar(40) not null, senha varchar(16) not null)")

    