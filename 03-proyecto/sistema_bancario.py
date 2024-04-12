from cuenta import Cuenta
from usuario import Usuario
import random as rd

class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.sesion = None

        usuario1 = Usuario("Jhon", "Doe", "26275576", "jhondoe", "123456")
        self.usuarios.append(usuario1)

        usuario2 = Usuario("Ryan", "Smith", "25645888", "ryansmith", "12345")
        self.usuarios.append(usuario2)

    def iniciar_sesion(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contraseña == contrasena:
                self.sesion = usuario  
                print("Inicio de sesión exitoso.")
                return True
        print("Usuario o contraseña incorrectos.")
        return False

    def menu(self):
        if self.sesion:
            while True:
                opciones = str(input("""
                                    1. Crear cuenta bancaria
                                    2. Depositar
                                    3. retirar
                                    4. Transferir
                                    5. Informacion
                                    6. Cerrar sesion
                                     """))
                if opciones.title() in ["1", "Crear", "Crear Cuenta Bancaria"]:
                    numero_cuenta = ""
                    if len(self.sesion.cuentas) == 0:
                        for i in range(12):
                            numero_cuenta += str(rd.randint(0, 9))
                        print(f"Tu numero de cuenta es el {numero_cuenta}")
                        while True:
                            saldo = input("Ingresa el saldo con el que deseas aperturar tu cuenta: ")
                            try:
                                saldo = float(saldo)
                                if saldo > 0:
                                    saldo = round(saldo, 2) 
                                    break
                                else:
                                    print("Solo puedes ingresar valores numericos positivos")
                            except ValueError:
                                print("Debes ingresar un número válido")
                        cuenta = Cuenta(numero_cuenta, saldo)
                        self.sesion.cuentas.append(cuenta)
                        print(f"Tu cuenta se ha creado correctamente, este es el nro de cuenta {numero_cuenta} y su saldo es de {saldo}$")
                    else:
                        print("Ya tienes una cuenta.")

                elif opciones.title() in ["2", "Depositar"]:
                    while True:
                        monto = input("Ingresa la cantidad a depositar: ")
                        if monto.isdigit() and float(monto) > 0:
                            monto = float(monto)
                            monto = round(monto, 2) 
                            break
                        else:
                            print("Solo puedes ingresar valores numericos positivos")
                    if self.sesion and self.sesion.cuentas:
                        self.sesion.cuentas[0].depositar(monto)
                        print(f"El nuevo saldo de la cuenta es de: {self.sesion.cuentas[0].saldo}")
                    else:
                        print("No existe ninguna cuenta a la cual depositar. Primero crea una cuenta")

                elif opciones.title() in ["3", "Retirar"]:
                    while True:
                        monto = input("Ingresa la cantidad a retirar: ")
                        if monto.isdigit() and float(monto) > 0:
                            monto = float(monto)
                            monto = round(monto, 2)  # Redondear saldo a dos decimales
                            break
                        else:
                            print("Solo puedes ingresar valores numericos positivos")
                    if self.sesion and self.sesion.cuentas:
                        self.sesion.cuentas[0].retirar(monto)
                        print(f"El nuevo saldo de la cuenta es de: {self.sesion.cuentas[0].saldo}")
                    else:
                        print("No existe ninguna cuenta a la cual retirar. Primero crea una cuenta")
                
                elif opciones.title() in ["4", "Transferir"]:
                    while True:
                        id = str(input("Ingresa la cedula de la persona a la que deseas traferir o (s) para salir: "))
                        if id.isdigit():
                            for usuario in self.usuarios:
                                if id == usuario.cedula:
                                    if id != self.sesion.cedula:
                                        if usuario.cuentas:
                                            print(f"La cedula {id} esta asociada a el usuario {usuario.nombre_usuario} con el nro de cuenta {usuario.cuentas[0].numero_cuenta}")
                                            cuenta_transferencia = str(input("Ingrese el nro de cuenta del usuario al que desea transferir: "))
                                            if cuenta_transferencia == usuario.cuentas[0].numero_cuenta:
                                                monto = float(input("Ingresa la cantidad a depositar: "))
                                                while True:
                                                        monto = float(monto)
                                                        if monto > 0:
                                                            monto = round(monto, 2)  # Redondear saldo a dos decimales
                                                            break
                                                            
                                                        else:
                                                            print("Solo puedes ingresar valores numericos positivos")
                                                if len(self.sesion.cuentas) > 0: 
                                                    if self.sesion.cuentas[0].saldo >= monto:
                                                        usuario.cuentas[0].depositar(monto)
                                                        self.sesion.cuentas[0].retirar(monto)
                                                        print("La transferencia se ha completado exitosamente.")
                                                        break
                                                    else:
                                                        print("Tu saldo es insuficiente para realizar esa transferencia.")
                                                        break
                                                else:
                                                    print("No puedes hacer una transferencia si no tienes cuenta.")
                                        else:
                                            print("El usuario que indicaste no se ha creado una cuenta")
                                    else:
                                            print("No puedes hacer una transferencia a tu misma cuenta.")
                                            break
                                else:
                                    print(f"La cedula {id} no existe en el registro del banco. Vuelve a intentarlo")
                        elif id.title() in ["S"]:
                            break
                        else:
                            print("Solo puedes ingresar valores numericos.")

                elif opciones.title() in ["5", "Informacion", "Info"]:
                    if self.sesion.cuentas:
                        print(f"""La sesion activa tiene las siguientes caracteristicas: 
                                Nombre: {self.sesion.nombre}
                                Apellido: {self.sesion.apellido}
                                Cedula: {self.sesion.cedula}
                                Usuario: {self.sesion.nombre_usuario}
                                Cuenta: {self.sesion.cuentas[0].numero_cuenta}
                                Saldo: {self.sesion.cuentas[0].saldo}""")
                    else:
                        print(f"""La sesion activa tiene las siguientes caracteristicas: 
                                Nombre: {self.sesion.nombre}
                                Apellido: {self.sesion.apellido}
                                Cedula: {self.sesion.cedula}
                                Usuario: {self.sesion.nombre_usuario}
                                Cuenta: None
                                Saldo: None""")

                elif opciones.title() in ["Salir", "S", "6"]:
                    print("Finalizando sesion...")
                    self.sesion == None
                    break

                else:
                    print("Selecciona una opcion valida!!")

    def main(self):
        while True:
            opciones = str(input("""
                                 1. Iniciar Sesion
                                 2. Salir
                                 """))
            if opciones.title() in ["1", "Iniciar", "Iniciar Sesion"]:
                name = str(input("Escriba el nombre de usuario: "))
                password = str(input("Ingrese su contraseña: "))
                self.iniciar_sesion(name, password)
                if self.sesion:
                    self.menu()
                else:
                    print("Vuelve a intentarlo.")
            elif opciones.title() in ["2", "Salir", "S"]:
                print("Saliendo del programa...")
                break

            else:
                print("Ingrese una opcion valida!!")
                


sistema = SistemaBancario()
sistema.__init__()
sistema.main()




            


    

            

