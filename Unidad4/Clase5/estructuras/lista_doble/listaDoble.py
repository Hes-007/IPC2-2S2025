from nodo import Nodo

class ListaDoble():
    def __init__(self):
         self.primero = None
         self.ultimo = None
         self.tamanio = 0

    def __len__(self):
         return self.tamanio
    
    #Vamos a realizar la inserción - Final de la lista

    def insertar(self, valor):
         #Creamos el nodo
         nuevo = Nodo(valor)
         if self.primero == None and self.ultimo == None:
              self.primero = nuevo
              self.ultimo = nuevo
         else:
              #Si la lista no esta vacia
              self.ultimo.siguiente = nuevo
              nuevo.anterior = self.ultimo
              self.ultimo = nuevo
              
         self.tamanio +=1
         
    def imprimirListaHaciaAdelante(self):
        actual = self.primero
        while actual != None:
            print(actual.valor)
            actual = actual.siguiente
    
    def imprimirListaHaciaAtras(self):
        actual = self.ultimo
        while actual != None:
            print(actual.valor)
            actual = actual.anterior