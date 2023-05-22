# Código de ejemplo otorgado por el docente: Walter Alejandro Araujo de Luna.
# Materia: Programación de aplicaciones locales, 6to semestre.
# Facultad de Contaduría Pública y Administración, Universidad Autónoma de Nuevo León.

from tkinter import ttk
from tkinter import *
import pyodbc

def Registrar(datos1):
   #DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
   # DB_PATH = "C:\Users\edith\OneDrive\Documentos\database.accdb"
   
   # Nombre del controlador.
   # Ruta completa del archivo.
   
    try:
        # Establecer la conexión.
        conn = pyodbc.connect("Driver=Microsoft Access Driver (*.mdb, *.accdb);DBQ=C:/Users/edith/OneDrive/Documentos/Database1.accdb") 
        print('conexion exitosa')
        
        # Crear cursor para ejecutar consultas.
        cursor = conn.cursor()
        
        # Agregar algunos datos.
        name = "JOSE"  # Nombre
        esp = "Cirugia plastica"  # Apellido
        ced = "123456789"  # Número de teléfono
        
        # Ejecutar la consulta.
        cursor.execute(u"INSERT INTO proveedor (nombre, especialidad, cedulaprofesional) "
                    u"VALUES (?, ?, ?)",
                    name, esp, ced)
        # Guardar los cambios.
        cursor.commit()
        
        cursor.close()
        conn.close()
    except:
        print('error al intentar conectar')
            

class Cliente:
    
    def __init__(self,root):
   
        self.wind = root
        self.wind.title("EJEMPLO CONEXION")
        self.wind.geometry("800x600")
        self.wind.config(bg="teal")
        
        nom=StringVar()
        dir=StringVar()
        mail=StringVar()
    
        # Interfaz generada para la configuracion de la Pagina o Pantalla, wind.

        frmProv = LabelFrame(self.wind, text="CLIENTE", font=("calibri", 12))
        frmProv.pack(fill="both", expand="yes", padx=20, pady=15)
        #SECCION DE CLIENTE
        lblNombre = Label(frmProv, text="Nombre", width=20)
        lblNombre.grid(row=0, column=0, padx=5, pady=3)
        entNombre = Entry(frmProv, textvariable=nom)
        entNombre.grid(row=0, column=1, padx=5, pady=3)

        lblDireccion = Label(frmProv, text="Direccion", width=20)
        lblDireccion.grid(row=0, column=2, padx=5, pady=3)
        entDomicilio = Entry(frmProv, textvariable=dir)
        entDomicilio.grid(row=0, column=3, padx=5, pady=3)

        lblCorreo = Label(frmProv, text="Correo", width=20)
        lblCorreo.grid(row=2, column=0, padx=5, pady=3)
        entCorreo = Entry(frmProv, textvariable=mail)
        entCorreo.grid(row=2, column=1, padx=5, pady=3)
        
        lblFecha = Label(frmProv, text="Fecha", width=20)
        lblFecha.grid(row=2, column=2, padx=5, pady=3)
        entFecha = Entry(frmProv, textvariable=mail)
        entFecha.grid(row=2, column=3, padx=5, pady=3)

        datos=nom.get(), dir.get(), mail.get()
        
        btnRegistrar = Button(frmProv, text="Registrar", width=12, height=2, command=lambda:Registrar(datos))
        btnRegistrar.grid(row=4, column=0, padx=10, pady=10)

        btnConsultar = Button(frmProv, text="Consultar", width=12, height=2)
        btnConsultar.grid(row=4, column=1, padx=10, pady=10)  
        
        btnCancelar = Button(frmProv, text="Cancelar", width=12, height=2, command=lambda:root.destroy())
        btnCancelar.grid(row=4, column=2, padx=10, pady=10)  

#SECCION DE PRODUCTO
        frmProd = LabelFrame(self.wind, text="PRODUCTO", font=("calibri", 12))
        frmProd.pack(fill="both", expand="yes", padx=20, pady=15)  

        lblNombProd = Label(frmProd, text="Nombre del Producto", width=20)
        lblNombProd.grid(row=0, column=0, padx=5, pady=3)
        self.entNombProd = Entry(frmProd)
        self.entNombProd.grid(row=0, column=1, padx=5, pady=3)   

        lblFechCad = Label(frmProd, text="Fecha de caducidad", width=20)
        lblFechCad.grid(row=1, column=0, padx=5, pady=3)
        self.entFechCad = Entry(frmProd)
        self.entFechCad.grid(row=1, column=1, padx=5, pady=3) 

        btnIngresar = Button(frmProd, text="Ingresar", width=12, height=2)
        btnIngresar.grid(row=3, column=0, padx=10, pady=10)

        btnBorrar = Button(frmProd, text="Borrar", width=12, height=2)
        btnBorrar.grid(row=3, column=1, padx=10, pady=10) 

#SECCION DE VENTA
        frmProd = LabelFrame(self.wind, text="VENTA", font=("calibri", 12))
        frmProd.pack(fill="both", expand="yes", padx=20, pady=15)  

 
# Proceso de arranque

if __name__ == '__main__':
    root = Tk()
    Cliente = Cliente(root)
    root.mainloop()

