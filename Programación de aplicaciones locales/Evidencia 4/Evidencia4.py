import sys
import os
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi

DB_FILE = "datos.db"

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
        self.pushButtonBorrarCliente.clicked.connect(self.borrarCliente)
    
    def agregarCliente(self):
        nombre = self.lineEditNombreCliente.text()
        direccion = self.lineEditDireccionCliente.text()
        telefono = self.lineEditTelefonoCliente.text()

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nombre TEXT, direccion TEXT, telefono TEXT)")
        cursor.execute("INSERT INTO clientes VALUES (?, ?, ?)", (nombre, direccion, telefono))
        connection.commit()
        connection.close()
        
        self.close()
    
    def borrarCliente(self):
        nombre = self.lineEditNombreCliente.text()

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM clientes WHERE nombre=?", (nombre,))
        connection.commit()
        connection.close()

        self.close()

class DialogAgregarVenta(QDialog):
    def __init__(self):
        super(DialogAgregarVenta, self).__init__()
        loadUi("DialogAgregarVenta.ui", self)
        self.pushButtonAgregarVenta.clicked.connect(self.agregarVenta)
        self.comboBoxCliente.addItems(self.obtenerClientes())
        self.comboBoxProducto.addItems(self.obtenerProductos())

    def agregarVenta(self):
        cliente = self.comboBoxCliente.currentText()
        producto = self.comboBoxProducto.currentText()
        fecha = self.dateEditFecha.date().toString("yyyy-MM-dd")
        costo_neto_total = self.lineEditCostoNetoTotal.text()

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ventas (cliente TEXT, producto TEXT, fecha TEXT, costo_neto_total TEXT)")
        cursor.execute("INSERT INTO ventas VALUES (?, ?, ?, ?)", (cliente, producto, fecha, costo_neto_total))
        connection.commit()
        connection.close()
        
        self.close()

    def obtenerClientes(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT nombre FROM clientes")
        clientes = cursor.fetchall()
        connection.close()
        return [cliente[0] for cliente in clientes]

    def obtenerProductos(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT nombre FROM productos")
        productos = cursor.fetchall()
        connection.close()
        return [producto[0] for producto in productos]

class DialogAgregarProducto(QDialog):
    def __init__(self):
        super(DialogAgregarProducto, self).__init__()
        loadUi("DialogAgregarProducto.ui", self)
        self.pushButtonAgregarProducto.clicked.connect(self.agregarProducto)
        self.pushButtonBorrarProducto.clicked.connect(self.borrarProducto)
    
    def agregarProducto(self):
        nombre = self.lineEditNombreProducto.text()
        descripcion = self.lineEditDescripcionProducto.text()
        precio = self.lineEditPrecioProducto.text()
        stock = self.lineEditStockProducto.text()

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, descripcion TEXT, precio TEXT, stock TEXT)")
        cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (nombre, descripcion, precio, stock))
        connection.commit()
        connection.close()
        
        self.close()
    
    def borrarProducto(self):
        nombre = self.lineEditNombreProducto.text()

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM productos WHERE nombre=?", (nombre,))
        connection.commit()
        connection.close()

        self.close()

if __name__ == "__main__":
    if not os.path.isfile(DB_FILE):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nombre TEXT, direccion TEXT, telefono TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS ventas (cliente TEXT, producto TEXT, fecha TEXT, costo_neto_total TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, descripcion TEXT, precio TEXT, stock TEXT)")
        connection.commit()
        connection.close()

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())