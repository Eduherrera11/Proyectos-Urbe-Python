class Cuenta:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        while True:
            if monto > 0:
                self.saldo += monto
                format(self.saldo, ".2f")
                print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.saldo}.")
                break
            else:
                print("Solo puedes ingresar valores numericos positivos.")


    def retirar(self, monto):
        if monto > 0:
            if self.saldo >= monto:
                self.saldo -= monto
                format(self.saldo, ".2f")
                print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self.saldo}.")
            else: 
                print("Fondos insuficientes.")
        else:
            print("Solo puedes ingresar valores numericos positivos.")
