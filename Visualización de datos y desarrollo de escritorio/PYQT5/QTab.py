import sys
from PyQt5.QtWidgets import *

class tabdemo(QTabWidget):
    def __init__(self, parent = None):
        super(tabdemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1,"Pestaña 1")
        self.addTab(self.tab2,"Pestaña 2")
        self.addTab(self.tab3,"Pestaña 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("tab demo")

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("Nombre",QLineEdit())
        layout.addRow("Dirección",QLineEdit())
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        Sexo = QHBoxLayout()
        Sexo.addWidget(QRadioButton("Hombre"))
        Sexo.addWidget(QRadioButton("Mujer"))
        layout.addRow(QLabel("Sexo"), Sexo)
        layout.addRow("Fecha de nacimiento", QLineEdit())
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Materias")) 
        layout.addWidget(QCheckBox("Física"))
        layout.addWidget(QCheckBox("Matemáticas"))
        self.tab3.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    ex = tabdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()