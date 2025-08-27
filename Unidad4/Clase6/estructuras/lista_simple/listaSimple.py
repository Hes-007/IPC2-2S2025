import os
#Es para acceder los comandos en la terminal

## entonces vamos a obtener el nodo
from estructuras.lista_simple.nodo import Nodo


class ListaSimple:
    def __init__(self):  # no va a pedir nada, pero si va a tener atributos
        self.primero = None #Cuando primero es nulo quiere decir que la lista esta vacia, cuando primero tiene un valor
        #esto es extra, pero por buenas practicas y tener un buen control lo colocamos
        self.tamanio = 0
        #porque si primero es nulo, el tamñano va ser igual a cero

    #Sobreescribimos esta función
    #len(lista)
    def __len__(self):
        return self.tamanio
        #tenemos un nodo que apunta a otro nodo, y ese nodo apunta a otro nodo, y asi sucesivamente

    #Insertar valores a la lista - vamos a insertar al final de la lista
    def insertar(self, valor):

        #Validar que ya existe un suario
        if self.validarExiste(valor.id) == True:   #Significa que si ya existe el id no hay que hacer todo lo anterior, significa que
            #aca muere la inserción. Si ya existe un id, que no se inserte
            return

        #Crear el nodo
        nuevo = Nodo(valor)
        #Verificamos si la lista esta vacia
        if self.primero == None:
            self.primero = nuevo
        # Si la lista no esta vacia
        else:
            #Recorremos la lista hasta el último nodo
            actual = self.primero #actual obtiene el primer valor
            while actual != None:
                # Si es nulo se sale del while, si no es nulo estra al while para seguir recorriendo
                if actual.siguiente == None:
                    actual.siguiente = nuevo
                    break # Ya insertaste, entonces acaba su ejecución
                actual = actual.siguiente   #Cada ves que nosotros pasemos por el while vamos a ir al siguiente nodo
        self.tamanio += 1

    def imprimirLista(self):
        actual = self.primero
        while actual != None:
            print(str(actual.valor)) # agruego esta función por los objetos string
            actual = actual.siguiente

    # ustedes quieren buscar algo
    def obtenerUsuario(self, id):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                return actual.valor
            actual = actual.siguiente
        return None
    
    def loginUsuario(self, id, password):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id and actual.valor.password == password:
                return True
            actual = actual.siguiente
        return False
    

    #Validar si existe un usuario
    def validarExiste(self, id):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                return True
            actual = actual.siguiente
        return False

    def graficar(self):
        #Vamos a ir concatenando el texto
        #esta es unaforma genérica para cualquier lenguaje 
        codigodot = ''
        # ahora vamos a concatenar
        codigodot += ''' digraph G {
        rankdir=LR;
        node [shape=record];
        '''

        #Luego vamos a crear una variable contador de nodos 
        # Se debe de tener mucho cuidado porque cada nodo que vallamos creando será único, y por necesitamos el contador
        contador_nodos = 1 # Para evitar erroes creamos un contador
        # creamos los nodos de la lista simple
        actual = self.primero
        #Vamos hacer un recorrido
        while actual != None:
            #Vamos a concatenar cada nodo
            codigodot += 'nodo' + str(contador_nodos) + '[label=\"{' + str(actual.valor)+'|<f1>}\"];\n'
            contador_nodos +=1
            #después de esto seguimos con el siguiente nodo
            actual = actual.siguiente
        #Ahora procemos a crear los enlaces
        actual = self.primero
        contador_nodos = 1
        while actual.siguiente != None:
            #Porque vamos a crear este texto y por ejemplo se quisiera crear un 4 nodo y evitar eso se utiliza el actual.siguiente
            codigodot += 'nodo' + str(contador_nodos)+' -> nodo'+str(contador_nodos+1)+';\n'
            #Ahora este nodo apunta a siguiente
            contador_nodos += 1
            actual = actual.siguiente
        
        #Por último vamos a concatenar esto para cerrar
        codigodot += '}'

        #Definir la ruta donde se guarda el codigo dot
        ruta_dot = 'reportesdot/listaSimple.dot'
        #Luego se crea el archivo dot
        archivo = open(ruta_dot, 'w')
        #Después escribimos el archivo
        archivo.write(codigodot)
        #Cerramos el archivo
        archivo.close()

        #Geración de archivo pnd, jpg, pdf, etc

        ruta_imagen = 'reportes/listaSimple.png'
        #Defino el comando de graphviz para compilar el .dot y generar el archvio 
        comando = 'dot -Tpng ' + ruta_dot + ' -o ' + ruta_imagen

        #Para ejecutar el comando dentro del sistema
        os.system(comando)

        #Ahora vamos a abrir la imagen
        #primero convertimos la ruta relativa a una ruta absoluta
        #Ruta relativa: ./hola.txt
        #Ruta absoluta: C://users//XD/documets/hola.txt
        ruta_abrir_imagen = os.path.abspath(ruta_imagen)

        #Ahora abrimos la imagen
        os.startfile(ruta_abrir_imagen)
        print("Grafico generado éxitosamente")

    
