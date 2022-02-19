import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class qdialog(QDialog):
    def __init__(self, parent = None):
      super(qdialog, self).__init__()

    def mostrardialogo():
        dlg = QDialog()
        b1 = QLabel("Archivo guardado exitosamente.",dlg)
        b1.setAlignment(Qt.AlignCenter)
        b2 = QPushButton("Close", dlg)
        b2.move(300,200)
        b2.clicked.connect(QCoreApplication.instance().quit) #Esto hace la magia de cerrar la ventana
        
        dlg.setWindowTitle("Dialog") #9. PyQt5 — QDialog Class
        dlg.setWindowModality(Qt.ApplicationModal)
        dlg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    btn = QPushButton(w)
    btn.setText("Guardar archivo")
    btn.move(300,200)
    btn.clicked.connect(qdialog.mostrardialogo)
    w.setWindowTitle("PyQt Dialog demo")
    w.show()
    sys.exit(app.exec_())