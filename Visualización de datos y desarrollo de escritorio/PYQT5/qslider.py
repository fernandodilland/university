import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qslider(QWidget):
   #Inicializar la clase
   def __init__(self, parent = None):
      super(qslider, self).__init__()
      
      #Diseño de ventana
      layout = QVBoxLayout()
      
      #Etiqueta de texto
      self.l1 = QLabel("Volumen")
      
      #Alineación del texto
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
	  
      #Formato vertical u horizontal
      self.sl = QSlider(Qt.Horizontal)
      
      #Valor mínimo
      self.sl.setMinimum(0)
      
      #Valor máximo
      self.sl.setMaximum(100)
      
      #Valor por default del slider
      self.sl.setValue(50)
      
      #Intervalos del slider
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(5)
	
      #Hacer visible el slider
      layout.addWidget(self.sl)
      self.setLayout(layout)
      
      #Añadir nombre de la ventana
      self.setWindowTitle("Volumen multimedia")


def main():
   aplicacion = QApplication(sys.argv)
   #Inicializar ventana
   ventana = qslider()
   ventana.show()
   sys.exit(aplicacion.exec_())
	
if __name__ == '__main__':
   main()