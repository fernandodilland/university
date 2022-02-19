import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.widgets import Widget

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
		
        layout = QVBoxLayout()
        self.b1 = QPushButton("Registrar numero")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
        self.b1.clicked.connect(self.btnstate)
        layout.addWidget(self.b1)
		
        self.b2 = QPushButton()
        self.b2.setIcon(QIcon(QPixmap(r"C:\Users\Usuario\Desktop\TRABAJOS DE AARON DIAZ\Preparatoria 6sem\consultar.png")))
        self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.b2)

        self.setLayout(layout)
        self.b3 = QPushButton("No funciona")
        self.b3.setEnabled(False)
        layout.addWidget(self.b3)
		
        self.b4 = QPushButton("&Default")
        self.b4.setDefault(True)
        self.b4.clicked.connect(lambda:self.whichbtn(self.b4))
        layout.addWidget(self.b4)
      
        self.setWindowTitle("Botones")

    def btnstate(self):
        if self.b1.isChecked():
            print ("Ya se registro un numero")
        else:
            print ("Se registro correctamente")
			
    def whichbtn(self,b):
        print ("clicked button is "+b.text())

def main():
    app = QApplication(sys.argv)
    ex = Form()
    ex.resize(400,400)
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()