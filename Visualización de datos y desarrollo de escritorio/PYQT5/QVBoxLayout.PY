import sys
from PyQt5 import QtWidgets

def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    button1 = QtWidgets.QPushButton('1')
    button2 = QtWidgets.QPushButton('2')
    button3 = QtWidgets.QPushButton('3')
    label1 = QtWidgets.QLabel('uno')
    label2 = QtWidgets.QLabel('dos')
    label3 = QtWidgets.QLabel('tres')

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(button1)
    v_box.addWidget(button2)
    v_box.addWidget(button3)
    v_box.addWidget(label1)
    v_box.addWidget(label2)
    v_box.addWidget(label3)

    windowExample.setLayout(v_box)

    windowExample.setWindowTitle('QVBoxLayout')
    windowExample.show()

    sys.exit(app.exec_())

basicWindow()