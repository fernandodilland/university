import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QComboBox, QLabel, QTextEdit, QListWidget, QMessageBox

class myListWidget(QListWidget):
   def Clicked(self,item):
      QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
		
def main():
   app = QApplication(sys.argv)
   listWidget = myListWidget()
	
   #Resize width and height
   listWidget.resize(300,300)
	
   listWidget.addItem("Prueba item 1"); 
   listWidget.addItem("Prueba item 2");
   listWidget.addItem("Prueba item 3");
   listWidget.addItem("Prueba item 4");
	
   listWidget.setWindowTitle('PyQT Demo de List')
   listWidget.itemClicked.connect(listWidget.Clicked)
   
   listWidget.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
   
   w.show()
   sys.exit(app.exec_())
