import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)
        self.pushButtonAgregarClienteDialog.clicked.connect(self.abrirCuadroDialogoAgregarCliente)
        self.pushButtonAgregarVentaDialog.clicked.connect(self.abrirCuadroDialogoAgregarVenta)
        self.pushButtonAgregarProductoDialog.clicked.connect(self.abrirCuadroDialogoAgregarProducto)
    
    def abrirCuadroDialogoAgregarCliente(self):
        dialog = DialogAgregarCliente()
        dialog.exec_()
    
    def abrirCuadroDialogoAgregarVenta(self):
        dialog = DialogAgregarVenta()
        dialog.exec_()
    
    def abrirCuadroDialogoAgregarProducto(self):
        dialog = DialogAgregarProducto()
        dialog.exec_()

class DialogAgregarCliente(QDialog):
    def __init__(self):
        super(DialogAgregarCliente, self).__init__()
        loadUi("DialogAgregarCliente.ui", self)
        self.pushButtonAgregarCliente.clicked.connect(self.agregarCliente)
    
    def agregarCliente(self):
        nombre = self.lineEditNombreCliente.text()
        direccion = self.lineEditDireccionCliente.text()
        telefono = self.lineEditTelefonoCliente.text()
        # Aquí puedes escribir el código para agregar el cliente a la base de datos
        
        self.close()

class DialogAgregarVenta(QDialog):
    def __init__(self):
        super(DialogAgregarVenta, self).__init__()
        loadUi("DialogAgregarVenta.ui", self)
        self.pushButtonAgregarVenta.clicked.connect(self.agregarVenta)
    
    def agregarVenta(self):
        cliente = self.comboBoxCliente.currentText()
        producto = self.comboBoxProducto.currentText()
        fecha = self.dateEditFecha.date().toString("yyyy-MM-dd")
        costo_neto_total = self.lineEditCostoNetoTotal.text()
        # Aquí puedes escribir el código para agregar la venta a la base de datos
        
        self.close()

class DialogAgregarProducto(QDialog):
    def __init__(self):
        super(DialogAgregarProducto, self).__init__()
        loadUi("DialogAgregarProducto.ui", self)
        self.pushButtonAgregarProducto.clicked.connect(self.agregarProducto)
    
    def agregarProducto(self):
        nombre = self.lineEditNombreProducto.text()
        descripcion = self.lineEditDescripcionProducto.text()
        precio = self.lineEditPrecioProducto.text()
        stock = self.lineEditStockProducto.text()
        # Aquí puedes escribir el código para agregar el producto a la base de datos
        
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
