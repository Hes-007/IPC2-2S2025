
#Obtener nuestro nodo
from estructuras.lista_simple.nodo import Nodo

class ListaSimple:
    def __init__(self):
        self.primero = None
        self.tamanio = 0
       
       
    #Sobreescribir la funcion len
    def __len__(self):
        return self.tamanio
    

    # Insertar valores a la lista - Vamos a insertar el nodo al final de la lista

    def insertar(self, valor):

        #Crear el nodo
        nuevo = Nodo(valor)
        #Verificar si la lista esta vacia
        if self.primero == None:
            self.primero = nuevo
        # Si la lista no esta vacia
        else:
            actual = self.primero
            #REcoremos la lista hasta el úlitimo nodo
            while actual != None:
                #Si es nulo automaticamente va a salir del while, si no es nulo, entonces va a recorrer la lista
                if actual.siguiente == None:
                    actual.siguiente = nuevo
                    break #Si encuentra el nuevo, el break termina el recorrido
                actual = actual.siguiente
        self.tamanio +=1

    def imprimirLista(self):
        actual = self.primero
        while actual != None:
            print(actual.valor) # Acá se imprime el cual valor.
            actual = actual.siguiente

        

