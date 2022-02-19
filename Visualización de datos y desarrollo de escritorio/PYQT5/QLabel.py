from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()

        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)
        label5=QLabel(self) 

        label1.setText('Visualización de Datos y Desarrollo de Escritorio')
        label1.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'> Bienvenido(a) </a>")
        label2.setAlignment(Qt.AlignLeft)

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('Esta es una etiqueta de imagen')
        label3.setPixmap(QPixmap(r"C:\Users\Andrea\Documents\cuarto semestre\visualización de datos y desarollo desk\imagen1.jpg"))

        label4.setText("<A href='www.w3schools.com'> Ingresa a w3schools </a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('Esta es una etiqueta de hipervínculo')

        label5.setText("W3Schools es un sitio web para aprender tecnologías web en línea. ​Contiene tutoriales de HTML, CSS, JavaScript, SQL, PHP, XML y otras tecnologías.​​Fue lanzado en 1999 por la empresa noruega Refsnes Data, y su nombre proviene de la World Wide Web.​W3Schools presenta cientos de ejemplos de código.")
        label5.setAlignment(Qt.AlignJustify)
        label5.setWordWrap(True)

        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)
        vbox.addStretch()
        vbox.addWidget(label5)
        vbox.addStretch()

        label1.setOpenExternalLinks(True)
        
        label4.setOpenExternalLinks(True)
        label4.linkActivated.connect(self.link_clicked)

        label2.linkHovered.connect(self.link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle('Qlabel')

    def link_hovered(self):
        print('Evento de activación cuando el mouse hace clic en label2')

    def link_clicked(self):
        print('Evento de activación cuando el mouse hace clic en label4')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=WindowDemo()
    win.show()
    sys.exit(app.exec_())