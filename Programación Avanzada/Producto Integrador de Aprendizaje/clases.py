"""
Materia: Programación avanzada, Profesor: Dr. José Felipe Ramirez Ramirez.
Programa realizado por: Fernando Dilland Mireles Cisneros.
"""

# "clases.py" Programa secundario del proyecto

# Clase
class Participante():
    # Propiedades
    correo = ""
    nombre = ""
    nacimiento = ""
    momento = "" # Fecha actual
    monto = 0
    folio = 0
    # Método constructor
    def __init__(self, correo, nombre, nacimiento, momento):
        self.correo=correo
        self.nombre=nombre
        self.nacimiento=nacimiento
        self.momento=momento
    # Método que será utilizado en el programa para funcionalidad
    def __repr__(self):
        return str(self.__dict__)
