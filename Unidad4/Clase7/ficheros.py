#Acá vamos a comenzar a manejar ficheros

#MANEJO DE FICHEROS

# 1. MÉTODO DE LECTURA DE FICHEROS

#Si solo vamos a querer leer

#Tenemos todo el contenido, el encoding jala todas las tildes tal y como es en xml

print('-------------LECTURA DE FICHEROS-------------')
with open('entrada.txt', 'r', encoding='utf-8') as archivo:
    #Para leerlo
    contenido = archivo.read()
    print(contenido)

# 2 Escrirua de archivo
#Método sobreescribe
#Podemos crar cualquier archivo, e inclusive archivos html, si piden reportes html y el archivo. w esto lo pueden aplicar 
# en los reportes del segundo proyecto
print('-------------ESCRITURA DE FICHEROS-------------')
with open('escritura.py', 'w') as archivo:
    contenido = "print('Hola Mundo!!!!!')\nprint('Si funciona :D')"
    archivo.write(contenido)
    print('Archivo creado con éxito')

#3. MÉTODO PARA AÑADIR TEXTO A UN FICHERO

print('-------------AÑADIR TEXTO A UN FICHERO-------------')
with open('entrada.txt', 'a') as archivo:
    #Se le coloca salto de línea porque recuerden que es también es un caracter los espacios en blanco.
    contenido = '\n Acabo de agreagar mas texto a mi archivo desde python'
    archivo.write(contenido)
    print('Texto añadido con éxito')

#4. MÉTODO PARA UN FICHERO EN MODO LECTURA Y ESCRITURA
# Si ustedes quieren leer y escribir un archivo
print('-------------LECTURA Y ESCRITURA DE UN FICHERO-------------')
with open('entrada.txt', 'r+', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print('Antes de que añada texto: ' + contenido)
    extra = '\nAcabo de concatenar texto con mi contenido actual'
    #Añado lo que leí mas el texto que voy a agregar
    salida = contenido + extra
    print('Mi salida ahora va ser: ' + salida)
    archivo.write(salida)
    print('Texto añadido con éxito')
  
# 5. LEER EN UN PUNTO EN ESPECÍFICO DEL FICHERO
print('-------------LECTURA EN UN PUNTO ESPECÍFOCO DE FICHERO-------------')
with open('entrada.txt', 'a+', encoding='utf-8') as archivo:
    #ubicamos donde quiero escribir
    archivo.write('prueba ')
    archivo.seek(5)
    contenido = archivo.read()
    print(contenido)
    print('Texto añadido con éxito')

# 6. ESCRIBIR EN UN PUNTO ESPECÍFICO DEL FICHERO
print('-------------ESCRIBIR EN UN PUNTO ESPECÍFOCO DE FICHERO-------------')
with open('entrada.txt', 'r+', encoding='utf-8') as archivo:
    archivo.seek(5)
    archivo.write('prueba ')
    print("Texto añadido con éxito")

#Por último si quieren leer un archivo linea por linea
#7. LEER UN FICHERO LINEA POR LINEA
print('-------------LECTURA LINEA POR LINEA DE UN FICHERO-------------')
with open('entrada.txt', 'r', encoding='utf-8') as archivo:
    contador = 0
    for linea in archivo:
        contador += 1
    print('El archivo tiene ' + str(contador) + ' lineas')

#Python es mas cariñoso al momento de implementar lo de ficheros, a comparación de otros lenguajes.
