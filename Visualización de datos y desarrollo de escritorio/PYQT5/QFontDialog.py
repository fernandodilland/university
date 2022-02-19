import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class tipografia(QWidget):
    def __init__(self, parent = None):
        super(tipografia, self).__init__(parent)

        layout = QVBoxLayout()
        self.boton = QPushButton("Elegir tipografía")
        self.boton.clicked.connect(self.getfont)

        layout.addWidget(self.boton)
        self.le = QLabel("Prueba de texto usando la tipografía elegida")

        layout.addWidget(self.le)
        self.setLayout(layout)
        self.setWindowTitle("Tipografia")

    def getfont(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.le.setFont(font)

def main():
    app = QApplication(sys.argv)
    ex = tipografia()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()