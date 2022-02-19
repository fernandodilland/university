import sys 
from PyQt5.QtWidgets import * 
                    
   
class App(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.title = 'QTableWidget'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
   
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
   
        self.createTable() 
   
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
   
        
        self.show() 
   
    
    def createTable(self): 
        self.tableWidget = QTableWidget() 
  
        
        self.tableWidget.setRowCount(4)  
  
        
        self.tableWidget.setColumnCount(2)   
  
        self.tableWidget.setItem(0,0, QTableWidgetItem("Nombre")) 
        self.tableWidget.setItem(0,1, QTableWidgetItem("Municipio")) 
        self.tableWidget.setItem(1,0, QTableWidgetItem("Andrea")) 
        self.tableWidget.setItem(1,1, QTableWidgetItem("Apodaca")) 
        self.tableWidget.setItem(2,0, QTableWidgetItem("Alan")) 
        self.tableWidget.setItem(2,1, QTableWidgetItem("Guadalupe")) 
        self.tableWidget.setItem(3,0, QTableWidgetItem("Alondra")) 
        self.tableWidget.setItem(3,1, QTableWidgetItem("San Nicolas")) 
   
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
   
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_()) 