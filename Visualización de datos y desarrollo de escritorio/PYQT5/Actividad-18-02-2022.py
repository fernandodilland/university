import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore # Se usará para alinear el texto de la pestaña 1
#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFontDialog
from PyQt5.QtWidgets import *


class tabdemo(QTabWidget):
   def __init__(self, parent = None):
      super(tabdemo, self).__init__(parent)
      self.tab1 = QWidget()
      self.tab2 = QWidget()

      self.addTab(self.tab1,"Tipografía")
      self.addTab(self.tab2,"Imagen")
      self.pestania1InterfazUsuario()
      self.pestania2InterfazUsuario()
      self.setWindowTitle("Actividad")

   def pestania1InterfazUsuario(self):

      #layout = QFormLayout()
      layout = QVBoxLayout()

      # Sistema para cambiar tipografía (QFontDialog)

      self.boton = QPushButton("Elegir tipografía") #Botón
      self.boton.clicked.connect(self.getfont)
      layout.addWidget(self.boton) # Muestra de texto

      self.le = QLabel("Prueba de texto usando la tipografía elegida")
      self.le.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft) # Alinea el texto

      layout.addWidget(self.le) # Muestra texto del "self.le = QLabel ...""

      self.tab1.setLayout(layout) # Mostrar texto con tipografía elegida

   def getfont(self):
      font, ok = QFontDialog.getFont()

      if ok:
         self.le.setFont(font)

      # Fin del sistema para cambiar tipografía

   def pestania2InterfazUsuario(self):
      #layout2 = QFormLayout()

      # Sistema para mostrar imagen (QFileDialog)
      layout = QVBoxLayout()
      self.boton = QPushButton("Seleccione un archivo")
      self.boton.clicked.connect(self.getfile)

      layout.addWidget(self.boton)
      self.le2 = QLabel("Sin imagen")

      layout.addWidget(self.le2)

      self.tab2.setLayout(layout) # Se agrega "tab2." antes del "setLayout" para definir que va en la pestaña 2


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

      # Fin del sistema para mostrar imagen


def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
