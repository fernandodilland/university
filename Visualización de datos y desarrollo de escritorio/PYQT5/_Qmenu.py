import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class menudemo(QMainWindow):
    
    def __init__(self, parent = None):
        super(menudemo, self).__init__(parent)
		
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("Archivo")
        file.addAction("Nuevo")
            
        save = QAction("Guardar",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
            
        edit = file.addMenu("Editar")
        edit.addAction("copiar")
        edit.addAction("pegar")
            
        quit = QAction("Salir",self) 
        file.addAction(quit)
        file.triggered[QAction].connect(self.processtrigger)
        self.setLayout(layout)
        self.setWindowTitle("Menu Demo")
		
    def processtrigger(self,q):
        print (q.text() + " se activa")
		
def main():
    app = QApplication(sys.argv)
    ex = menudemo()
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()