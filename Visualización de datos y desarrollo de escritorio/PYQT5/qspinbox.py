import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class spindemo(QWidget):
   def __init__(self, parent = None):
      super(spindemo, self).__init__(parent)
      
      #Establecer el diseño
      diseño = QVBoxLayout()
      
      #Generar una etiqueta
      self.l1 = QLabel("El nivel de brillo actual es de: ")
      
      #Alinear la etiqueta centralizada
      self.l1.setAlignment(Qt.AlignCenter)
      
      #Añade la etiqueta a la ventana
      diseño.addWidget(self.l1)
      
      #Crea un spinbox
      self.sp = QSpinBox()
      
      #Definir el rango del spinbox
      self.sp.setRange(0,100)
      
      #Agregar el spinbox a la ventana
      diseño.addWidget(self.sp)
      
      #Cambia el valor del spinbox con base en los clicks
      self.sp.valueChanged.connect(self.cambiodevalor)
      
      #Elige el diseño
      self.setLayout(diseño)
      
      #Establece el nombre de la ventana
      self.setWindowTitle("Brillo")
		
   def cambiodevalor(self):
      # Muestra cuando cambia el nivel de brillo en el spinbox
      self.l1.setText("El nivel de brillo actual es de: "+str(self.sp.value()))

def main():
   app = QApplication(sys.argv)
   ex = spindemo()
   ex.move(500,500)
   ex.resize(500,200)
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()