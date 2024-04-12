''' while True:
            monto = input("Ingresa el monto a depositar: ")
            if type(monto) in [int, float]:
                if monto > 0:
                    self.saldo += monto
                    break
                else:
                    print("Solo puedes ingresar valores numericos positivos")
            else:
                print("Solo puedes ingresar valores numericos positivos")

     while True:
            monto = input("Ingresa el monto a depositar: ")
            if type(monto) in [int, float]:
                if (monto > 0) and (self.saldo >= monto):
                    self.saldo -= monto
                    break
                else:
                    print("Solo puedes ingresar valores numericos positivos")
            else:
                print("Solo puedes ingresar valores numericos positivos")

                
                    def __depositar_en_sesion(self, monto):
        if self.sesion and self.sesion.cuentas:
            self.sesion.cuentas[0].depositar(monto)
        else:
            print("No hay sesión activa o el usuario no tiene cuentas.")

    def __retirar_en_sesion(self, monto):
        if self.sesion and self.sesion.cuentas:
            self.sesion.cuentas[0].retirar(monto)
        else:
            print("No hay sesión activa o el usuario no tiene cuentas.")
                '''