import sqlite3


class Banco():
    def __init__(self):
        self.conection = sqlite3.connect('database.db')
        self.create_table()

    def create_table(self):
        connect_data = self.conection.cursor()
        connect_data.execute("create table if not exists userdb(idusuario int auto_increment primary key not null,nome varchar(60) not null,telefone varchar(40) not null,email varchar(80) not null,usuario varchar(40) not null,senha varchar(16) not null)")
        self.conection.commit()
        connect_data.close()

    