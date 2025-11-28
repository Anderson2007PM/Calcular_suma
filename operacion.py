import threading


class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2


    def calcular_suma(self):
        suma = self.numero1 + self.numero2
        print("La suma es:", suma)

            

operacion1 = Operacion(4,5)

hilo1 = threading.Thread(target=operacion1.calcular_suma)


