from nodo import Nodo

class listaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None # Esto hace que no se encicle nuestra lista
        self.tamanio = 0

    def __len__(self):
        return self.tamanio
    
    def insertar(self, valor):
        #Acá vamos a insertar siempre al final
        nuevo = Nodo(valor)
        #Que es lo que hace especial esto?
        if self.primero == None and self.ultimo == None:
            #1. Asignamos el nuevo nodo al primero de la lista
            self.primero = nuevo
            #2. asignamos el nuevo nodo al ultimo de la lista
            self.ultimo = nuevo
            #3. luego el último nodo apunta al primer nodo - asi se inserta cuando el es el primero de la lista
            self.ultimo.siguiente = self.primero
        #Si la lista no esta vacia
        else:
            #1. el siguiente del ultimo nodo apunta al nuevo nodo
            self.ultimo.siguiente = nuevo
            #2. El ultimo nodo va hacer ahora el nuevo nodo
            self.ultimo = nuevo
            #3. el siguiente del último nodo va a apuntar a primero nodo
            self. ultimo.siguiente = self.primero
        self.tamanio += 1
