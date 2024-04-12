from persona import Persona

class Usuario(Persona):
    def __init__(self, nombre, apellido, cedula, nombre_usuario, contraseña):
        super().__init__(nombre, apellido, cedula)
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.cuentas = []

lista = []
usuario1 = Usuario("Jhon", "Doe", "26275576", "jhondoe", "123456")
lista.append(usuario1)

"""for i in lista:
    print(i.nombre_usuario)"""

