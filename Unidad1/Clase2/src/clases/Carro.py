#Vamos a importar la clase vehiculo, porque de ella se heredan
# atributos para las clases hijas
from clases.Vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, marca, modelo, anio, numPasajeros):
        super().__init__(marca, modelo, anio)
        self.numPasajeros = numPasajeros

    def informacionDetallada(self):
        #: ^ centro
        #: > derecha
        #: < izquierda
        print(f"-" + "-" * 61)
        print(f"|{"Carro":^61}|") 
        print(f"|" + "-" * 30 + "|" + "-" * 30 + "|")
        print(f"|{"Marca:":<30}|{self.marca:<30}|")
        print(f"|{"Modelo:":<30}|{self.modelo:<30}|")
        print(f"|{"Año:":<30}|{self.anio:<30}|")
        print(f"|{"Disponible:":<30}|{self.disponible:<30}|")
        print(f"|{"Pasajeros:":<30}|{self.numPasajeros:<30}|")
        print(f"-" + "-" * 61)

    #Encapsulamiento

    #Getters
    def getNumPasajeros(self):
        return self.numPasajeros
    
    #Setters
    def setNumPasajeros(self, numPasajeros):
        self.numPasajeros = numPasajeros
