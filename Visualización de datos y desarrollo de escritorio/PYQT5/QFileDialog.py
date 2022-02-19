import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class filedialogdemo(QWidget):
    def __init__(self, parent = None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.boton = QPushButton("Seleccione un archivo")
        self.boton.clicked.connect(self.getfile)

        layout.addWidget(self.boton)
        self.le2 = QLabel("Sin imagen")

        layout.addWidget(self.le2)
        self.setLayout(layout)


    def getfile(self):
        # Importante agregar el ", _" después de "fname" y antes del "="
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 
            'c:\\',"Image files (*.jpg *.gif)")
        self.le2.setPixmap(QPixmap(fname))
        # Optional, resize window to image size
        self.resize(QPixmap(fname).width(),QPixmap(fname).height())

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")

def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()