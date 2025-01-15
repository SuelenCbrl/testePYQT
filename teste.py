
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

# class App(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.init_ui()

#     def init_ui(self):
#         # Definindo o título da janela
#         self.setWindowTitle('teste PyQt5')

#         # Criando um layout vertical
#         layout = QVBoxLayout()

#         # Criando um rótulo de texto
#         label = QLabel('Olá, PyQt5!', self)

#         # Criando um botão
#         button = QPushButton('Clique aqui', self)

#         # Adicionando os widgets no layout
#         layout.addWidget(label)
#         layout.addWidget(button)

#         # Definindo o layout na janela
#         self.setLayout(layout)

#         # Ajustando o tamanho da janela
#         self.setGeometry(100, 100, 400, 300)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = App()
#     window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Definindo o título da janela
        self.setWindowTitle('Janela Expandida PyQt5')

        # Criando o layout principal (vertical)
        main_layout = QVBoxLayout()

        # Criando um layout para os botões (horizontal)
        button_layout = QHBoxLayout()

        # Criando um rótulo de texto
        self.label = QLabel('Digite algo e clique no botão:', self)

        # Criando um campo de entrada de texto (QLineEdit)
        self.text_input = QLineEdit(self)

        # Criando dois botões
        self.button_show = QPushButton('Mostrar Texto', self)
        self.button_clear = QPushButton('Limpar Texto', self)

        # Conectando os botões a funções
        self.button_show.clicked.connect(self.show_text)
        self.button_clear.clicked.connect(self.clear_text)

        # Adicionando widgets ao layout de botões
        button_layout.addWidget(self.button_show)
        button_layout.addWidget(self.button_clear)

        # Adicionando widgets ao layout principal
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.text_input)
        main_layout.addLayout(button_layout)

        # Definindo o layout principal da janela
        self.setLayout(main_layout)

        # Ajustando o tamanho da janela
        self.setGeometry(100, 100, 400, 200)

    def show_text(self):
        # Exibe o texto inserido no campo de entrada
        entered_text = self.text_input.text()
        self.label.setText(f'Você digitou: {entered_text}')

    def clear_text(self):
        # Limpa o campo de entrada e o rótulo
        self.text_input.clear()
        self.label.setText('Digite algo e clique no botão:')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
