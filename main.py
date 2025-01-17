import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

def on_click():
    print("Botão clicado!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Exemplo PyQt6')
window.setGeometry(100, 100, 280, 80)

button = QPushButton('Clique-me', window)
button.clicked.connect(on_click)
button.resize(100, 30)
button.move(90, 20)

window.show()
sys.exit(app.exec())