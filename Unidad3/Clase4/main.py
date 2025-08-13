#importar MiniDom
from xml.dom import minidom
from xml.dom.minidom import Document

#Importar Element Tree
import xml.etree.ElementTree as ET

#Importar Tkinter para obtner la ruta de los archivos XML
from tkinter import filedialog, messagebox


def menu_principal():
    ruta = ' '
    while True:
        print('--------- MENU PRINCIPAL ---------')
        print('- 1. Cargar XML                  -')
        print('- 2. Leer XML con miniDOM        -')
        print('- 3. Leer XML con ElementTree    -')
        print('- 4. Escribir XML con miniDOM    -')
        print('- 5. Salir                       -')
        print('----------------------------------')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 1:
                ruta = cargar_xml()
                if ruta == '':
                    messagebox.showerror('Error', 'No se seleccionó un archivo')
                else:
                    messagebox.showinfo('Exito', 'Archivo cargado al sistema exitosamente')
                print(ruta)
            case 2:
                leerConMiniDom(ruta)
            case 3:
                leerConET(ruta)
            case 4:
               escribirConMiniDOM()
            case 5:
                print('Hasta luego')
                break
            case _:
                print('Opción no válida')

def cargar_xml():
    ruta_archivo = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files', '*.*')))
    return ruta_archivo

def leerConMiniDom(ruta):
    #Primero vamos a parsear el XML
    doc = minidom.parse(ruta)
    #print(doc)
    #Obtener el elemento raíz
    root = doc.documentElement
    #print(root.nodeName)
    #Validaciones
    if root.nodeName == 'libros':
        #Esto mas que todo es para prevenir errores 
        #Vamos a obtener los nodos hijos de la raíz
        libros = root.getElementsByTagName('libro') #Me va a retornar una lista libros
        #print(libros)

        #Recorrer los nodos libro
        for libro in libros:
            id = libro.getAttribute('id')
            titulo = libro.getElementsByTagName('titulo')[0].firstChild.data 
            autor = libro.getElementsByTagName('autor')[0].firstChild.data 
            precio = libro.getElementsByTagName('precio')[0].firstChild.data 
            imagen = libro.getElementsByTagName('imagen')[0].firstChild.data 

            print('-'*20)
            print('ID:', id)
            print('Titulo:', titulo)
            print('Autor:', autor)
            print('Precio:', precio)
            print('Imagen:', imagen)

    elif root.nodeName == 'reservaciones':
         reservaciones = root.getElementsByTagName('reservacion')
         for reservacion in reservaciones:
            id = reservacion.getAttribute('id')
            descripcion = reservacion.getElementsByTagName('descripcion')[0].firstChild.data
            libro = reservacion.getElementsByTagName('libro')[0].firstChild.data
            usuario = reservacion.getElementsByTagName('usuario')[0].firstChild.data
            dia = reservacion.getElementsByTagName('dia')[0].firstChild.data
            hora = reservacion.getElementsByTagName('dia')[0].getAttribute('hora')

            print('-'*20)
            print('ID:', id)
            print('Descripción:', descripcion)
            print('Libro:', libro)
            print('Usuario:', usuario)
            print('Día:', dia)
            print("Hora:", hora)
            print("")  

def leerConET(ruta):
    #Parseamos el XML
    tree = ET.parse(ruta)
    #Obtener el elemento raiz
    root = tree.getroot()
    #Si queremos obtener etiquetas para hacer validaciones
    #print(root.tag)
    if root.tag == 'libros':
        #Si quiero obtener la cantidad de libros
        #print(len(root))

        #Recorrer todos los hijos
        for libro in root:
            id = libro.attrib['id']
            titulo = ''
            autor = ''
            precio = ''
            imagen = ''
            for hijo in libro:
                match hijo.tag:
                    case 'titulo':
                        titulo = hijo.text
                    case 'autor':
                        autor = hijo.text
                    case 'precio':
                        precio = hijo.text
                    case 'imagen':
                        imagen = hijo.text

            print('-'*20)
            print('ID:', id)
            print('Titulo:', titulo)
            print('Autor:', autor)
            print('Precio:', precio)
            print('Imagen:', imagen)
            print("")

    elif root.tag == 'reservaciones':
        for reservacion in root:
            id = reservacion.attrib['id']
            descripcion = ''
            libro = ''
            usuario = ''
            dia = ''
            hora = ''
            for hijo in reservacion:
                match hijo.tag:
                    case 'descripcion':
                        descripcion = hijo.text
                    case 'libro':
                        libro = hijo.text
                    case 'usuario':
                        usuario = hijo.text
                    case 'dia':
                        dia = hijo.text
                        hora = hijo.attrib['hora']

            print('*'*20)
            print('ID:', id)
            print('Descripción:', descripcion)
            print('Libro:', libro)
            print('Usuario:', usuario)
            print('Día:', dia)
            print("Hora:", hora)
            print("")

def escribirConMiniDOM():
    #creamos el Documento
    doc = Document()

    #creamos el elemento raiz
    root = doc.createElement('estudiantes')
    doc.appendChild(root)

    #creamos elementos hijos de root
    estudiante1 = doc.createElement('estudiante')
    #agregamos un atributo
    estudiante1.setAttribute('carnet', '201704787')
    root.appendChild(estudiante1)

    #agregamos los hijos de estudiante1
    nombre = doc.createElement('nombre')
    texto_nombre = doc.createTextNode('Estudiante 1')
    nombre.appendChild(texto_nombre)
    estudiante1.appendChild(nombre)

    edad = doc.createElement('edad')
    texto_edad = doc.createTextNode('20')
    edad.appendChild(texto_edad)
    estudiante1.appendChild(edad)

    #creamos el archivo
    #agregamos un formato de indentacion
    xml_str = doc.toprettyxml(indent='\t')

    #guardamos el archivo
    with open('salida/estudiantes.xml', 'w') as archivo:
        archivo.write(xml_str)
        archivo.close()

        
if __name__ == '__main__':
    menu_principal()
