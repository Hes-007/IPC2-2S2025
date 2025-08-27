import os

from estructuras.lista_doble.nodo import Nodo

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio
    
    #IGual insersión al final de la lista
    def insertar(self, valor):
        #Creamos el nodo
        nuevo = Nodo(valor)
        #Verificamos si la lista esta vacia
        if self.primero == None and self.ultimo == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            #Si la lista no esta vacia
            #mas facil porque al tener un ultimo 
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            #ESto que quiere decir que apunta al último de la lista
            self.ultimo = nuevo
        #Aumentamos el contador del tamaño de la lista
        self.tamanio +=1

    def imprimirListaHaciaAdelante(self):
        actual = self.primero
        while actual != None:
            print(str(actual.valor))
            actual = actual.siguiente
    
    def imprimirListaHaciaAtras(self):
        actual = self.ultimo
        while actual != None:
            print(str(actual.valor))
            actual = actual.anterior

    def buscar(self, id):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                return actual.valor
            actual = actual.siguiente
        return None

    def login(self, id, password):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id and actual.valor.password == password:
                return True
            actual = actual.siguiente
        return False
    
    def graficar(self):
        codigo_dot = ''
        codigo_dot += ''' digraph G {
            rankdir=LR;
            node [shape=record, height=0.1];
        '''

        actual = self.primero
        contador_nodos = 1

        while actual != None:
            #Vamos a crear los nodos
            codigo_dot += 'nodo'+ str(contador_nodos)+'[label=\"{<f1>|'+ str(actual.valor)+'|<f2>}\"];\n'
            contador_nodos +=1
            actual = actual.siguiente
            #Realizar Enlaces
        actual = self.primero
        contador_nodos = 1
        
        while actual.siguiente != None:
            #Relación de izquierda a derecha
            codigo_dot += 'nodo'+str(contador_nodos)+':f2 -> nodo' +str(contador_nodos+1)+':f1;\n'
            #Relacion de derecha a izquierda
            codigo_dot += 'nodo'+str(contador_nodos+1)+':f1 -> nodo' +str(contador_nodos)+':f2;\n'
            contador_nodos +=1
            actual = actual.siguiente
        codigo_dot += '}'

        #Ahorita se procede hacer lo mismo
        #Crar y escribir el archivo .dot
        ruta_dot = 'reportesdot/listaDoble.dot'

        #Creo el archivo
        archivo = open(ruta_dot, 'w')
        archivo.write(codigo_dot)
        archivo.close()

        #Generamos la imagen
        ruta_imagen = 'reportes/listaDoble.svg'
        comando = 'dot -Tsvg ' + ruta_dot + ' -o ' + ruta_imagen
        os.system(comando)

        #Para que me abra desde windows
        #Convierto la ruta relativa a ruta absoluta

        ruta_abrir_imagen = os.path.abspath(ruta_imagen)

        #Despues abrimos el archivo
        os.startfile(ruta_abrir_imagen)
        print("Se generó la gráfica de la lista doble")




