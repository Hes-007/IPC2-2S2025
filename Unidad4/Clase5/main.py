#Element Tree
import xml.etree.ElementTree as ET
# Importar Tkinter para obtener la ruta de los archivos XML
from tkinter import filedialog, messagebox
#vamos a importar los siguiente

from clases.usuario import Usuario
from estructuras.lista_simple.ListaEnlazada import ListaSimple

lista_usuario = ListaSimple()


def menu():
    opcion = 0
    while True:
        print('------------LISTAS-------------')
        print('1. Carga masiva')
        print('2. Ver lista simple enlazada')
        print('3. Ver lista doblemente enlazada')
        print('4. Obtener libro')
        print('5. Obtener usuario')
        print('7. Salir')
        opcion = input('Ingrese la opción que desee: ')
        if opcion == '1':
            carga_masiva()
        elif opcion == '2':
            lista_usuario.imprimirLista()
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
        elif opcion == '6':
            pass
        elif opcion == '7':
            break
        else:
            print('Opción no válida')

def carga_masiva():
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    if root.tag == 'usuarios':
        for usuario in root:
            id = usuario.attrib['id']
            password = usuario.attrib['password']
            nombre = ''
            edad = ''
            correo = ''
            telefono = ''
            for hijo in usuario:
                if hijo.tag == 'nombre':
                    nombre = hijo.text
                elif hijo.tag == 'edad':
                    edad = hijo.text
                elif hijo.tag == 'email':
                    correo = hijo.text
                elif hijo.tag == 'telefono':
                    telefono = hijo.text
            nuevo = Usuario(id, password, nombre, edad, correo, telefono)
            lista_usuario.insertar(nuevo)
            
            
    elif root.tag == 'libros':
        for libro in root:
            id = libro.attrib['id']
            titulo = ''
            autor = ''
            precio = ''
            imagen = ''
            for hijo in libro:
                if hijo.tag == 'titulo':
                    titulo = hijo.text
                elif hijo.tag == 'autor':
                    autor = hijo.text
                elif hijo.tag == 'precio':
                    precio = hijo.text
                elif hijo.tag == 'imagen':
                    imagen = hijo.text
           

if __name__ == '__main__':
    menu()