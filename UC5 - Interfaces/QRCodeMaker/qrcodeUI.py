from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QLabel, QMessageBox)
from PyQt5.QtGui import QPixmap
import sys
from qrcodeback import gerador_qr_code

class qr_code_front(QWidget):
    def __init__(self):
        super().__init__()
        # Salva o qrcode para depois deletar
        self.h_layout_qrcode = None
        # Vertical?
        self.layout = QVBoxLayout()

        # Horizontal
        self.h_layout = QHBoxLayout()

        # Titulo
        self.url = QLabel("Digite a url:")
        self.h_layout.addWidget(self.url)
        # input do usuario
        self.input_usuario = QLineEdit(self)
        self.h_layout.addWidget(self.input_usuario)
        # botão para fazer a  operacao
        self.criarBotao = QPushButton("Criar", self)
        self.criarBotao.clicked.connect(self.comunicar_qrcode)
        

        self.layout.addLayout(self.h_layout) # adiciona a url e input primeiro para nao haver erro
        self.layout.addWidget(self.criarBotao)
        self.setLayout(self.layout)
        
        self.setWindowTitle("QrCode Maker")
        self.resize(200, 100)
        self.gerador = gerador_qr_code()
        

    def error_messagem(self):
        QMessageBox.critical(self, "Erro", "Por favor, insira uma url válida.")

    def comunicar_qrcode(self):
        string = self.input_usuario.text()
        
        resposta = QMessageBox.question(self, 'Confirmação', 'Você deseja continuar?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resposta == QMessageBox.Yes:
                qr = self.gerador.gerar_qrcode(string)
                if not qr:
                    self.error_messagem()
                else:
                    QMessageBox.information(self, "QR Code Criado", "O QR Code foi gerado com sucesso!")
                    self.mostrar_qrcode()
        else:
            QMessageBox.information(self, "Processo cancelado", "Ação cancelada")
            
    def mostrar_qrcode(self):
        self.deletar_qrcode()
        self.h_layout_qrcode = QHBoxLayout()
        self.label = QLabel()
        qrcode_image = QPixmap('Pyqt5_Interfaces/QRCodeMaker/qrExport.png')
        self.label.setPixmap(qrcode_image)

        # Adiciona o qrcode ao layout
        self.h_layout_qrcode.addWidget(self.label)
        self.layout.addLayout(self.h_layout_qrcode)
    def deletar_qrcode(self):
        self.layout.removeItem(self.h_layout_qrcode)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qrmaker = qr_code_front()
    qrmaker.show()
    sys.exit(app.exec_())