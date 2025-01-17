
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
# #     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Janela Expandida PyQt5')
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.label = QLabel('Digite algo e clique no botão:', self)
        self.text_input = QLineEdit(self)
        self.button_show = QPushButton('Mostrar Texto', self)
        self.button_clear = QPushButton('Limpar Texto', self)
        self.button_show.clicked.connect(self.mostrar_texto)
        self.button_clear.clicked.connect(self.apagar_texto)
        button_layout.addWidget(self.button_show)
        button_layout.addWidget(self.button_clear)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.text_input)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.setGeometry(100, 100, 800, 200)

    def mostrar_texto(self):
        entered_text = self.text_input.text()
        self.label.setText(f'Você digitou: {entered_text}')

    def apagar_texto(self):
        
        self.text_input.clear()
        self.label.setText('Digite algo e clique no botão:')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QKeySequence, QAction

class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard \
                | QMessageBox.StandardButton.Cancel
        )
        if answer & QMessageBox.StandardButton.Save:
            save()
            if text.document().isModified():
                # This happens when the user closes the Save As... dialog.
                # We do not want to close the window in this case because it
                # would throw away unsaved changes.
                e.ignore()
        elif answer & QMessageBox.StandardButton.Cancel:
            e.ignore()

app = QApplication([])
app.setApplicationName("Text Editor")
text = QPlainTextEdit()
window = MainWindow()
window.setCentralWidget(text)

file_path = None

menu = window.menuBar().addMenu("&File")
open_action = QAction("&Open")
def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path
open_action.triggered.connect(open_file)
open_action.setShortcut(QKeySequence.StandardKey.Open)
menu.addAction(open_action)

save_action = QAction("&Save")
def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence.StandardKey.Save)
menu.addAction(save_action)

save_as_action = QAction("Save &As...")
def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        file_path = path
        save()
save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)

close = QAction("&Close")
close.triggered.connect(window.close)
menu.addAction(close)

help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)
def show_about_dialog():
    text = "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    QMessageBox.about(window, "About Text Editor", text)
about_action.triggered.connect(show_about_dialog)

window.show()
app.exec()
