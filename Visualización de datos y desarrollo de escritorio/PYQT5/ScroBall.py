# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # titulo
        self.setWindowTitle("PyQt5 - QScrollBar | Visualizacion de datos ")
 
        # tamaño de la ventana
        self.setGeometry(100, 100, 500, 400)
 
        # llamamos el metodo
        self.UiComponents()
 
        # mostamos los widgets
        self.show()
 
 
    # metodo del componente
    def UiComponents(self):
 
        scroll = QScrollBar(self)
 
        # establecemos el tamaño de la scroll bar
        scroll.setGeometry(100, 50, 30, 200)
 
        # color de la scroll bar
        scroll.setStyleSheet("background : lightgrey;")
 
        # creamos un label
        label = QLabel("App Scrollbar", self)
 
        # establecemos el tamaño del label
        label.setGeometry(200, 100, 300, 80)
 
        # hacemos el label multi linea
        label.setWordWrap(True)
 
        # llamamos la accion a la scroll bar
        scroll.valueChanged.connect(lambda: do_action())
 
        # creamos la accion
        def do_action():
 
            # valor por defecto de la scroll bar
            value = scroll.value()
 
            # establecemos el texto del label
            label.setText("Valor: " + str(value))
 
 
# creamos la app pyqt5
App = QApplication(sys.argv)
 
# creamos la instancia de windows
window = Window()
 
# iniciamos la app
sys.exit(App.exec())

