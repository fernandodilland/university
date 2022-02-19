import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class checkdemo(QWidget):
   def __init__(self, parent = None):
      super(checkdemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.b1 = QCheckBox("Rojo")
      self.b1.setChecked(True)
      self.b1.stateChanged.connect(lambda:self.btnstate(self.b1))
      layout.addWidget(self.b1)
		
      self.b2 = QCheckBox("Azul")
      self.b2.toggled.connect(lambda:self.btnstate(self.b2))

      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.setWindowTitle("Seleccion de color")

   def btnstate(self,b):
      if b.text() == "Rojo":
         if b.isChecked() == True:
            print ("El color es " + b.text())
         else:
            print ("Seleccione un color")
				
      if b.text() == "Azul":
         if b.isChecked() == True:
            print ("El color es " + b.text())
         else:
            print ("Seleccione un color")
				
def main():

   app = QApplication(sys.argv)
   ex = checkdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()