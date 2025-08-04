'''
Creando nuestro constructor
todo lo que vallamos a crear en el constructor siempre va el self
el self es una referencia a la instancia actual de la clase
se usa para acceder a las variables y métodos de la clase.
'''

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.disponible = True

    #Métodos
    def mantenimiento(self):
        self.disponible = False

    def disponibilizar(self):
        self.disponible = True

    def informacionDetallada(self):
        '''
        Formato estelizado para ver la información
        :^ el titulo irá en el centro 
        :> el titulo irá hacia la derecha 
        :< el titulo irá hacia la izquierda
        f es para darle formato a la cadena
        '''
        print(f"-" + "-" * 61)
        # "*" * 5 = "*****"
        print(f"|{"Vehiculo":^61}|")
        print(f"|" + "-" *30 + "|" + "-" * 30 + "|")
        print(f"|{"Marca":<30}|{self.marca:<30}|")
        print(f"|{"Modelo:":<30}|{self.modelo:<30}|")
        print(f"|{"Año:":<30}|{self.anio:<30}|")
        print(f"|{"Disponible:":<30}|{self.disponible:<30}|")
        print(f"-" + "-" * 61)

    #Encapsulamientos

    #Getters
    '''
    Los getters son métodos que nos permiten acceder a los atributos privados
    de las clases. Se usan para obtener el valor de un atributo privado
    '''

    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo
    
    def getAnio(self):
        return self.anio
    
    def getDisponible(self):
        return self.disponible 
    
    # Setters
    #Los setters son métodos que nos permiten modificar los atributos
    #privados de la clase.

    def setMarca(self, marca):
        self.marca = marca
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def setAnio(self, anio):
        self.anio = anio

    def setDisponible(self, disponible):
        self.disponible = disponible



