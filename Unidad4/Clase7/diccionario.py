# MANEJO DE DICCIONARIOS

#Primero vamos a ver como se cra un diccionario

#1. CREACIÓN DE UN DICCIONARIO
#DICCIONARIO VACIO
#Python no es tan exigente con esto
diccionario_nuevo = {}
print(diccionario_nuevo)

#DICCIONARIO CON DATOS INICIALES
mi_diccionario = {
    'nombre': 'Juan',
    'username': 'juancho',
    'edad': 23,
    'pais': 'Guatemala'
}
print(mi_diccionario)

#Eso es lo bonito de python porque estos pueden interpretar este tipo de datos
#Ustedes crear objetos por medio de diccionarios osea practicamente es un json

# 2. ACCESO A LOS ELEMENTOS DE UN DICCIONARIO
nombre = mi_diccionario['username']
print(nombre)

# 3. MODIFICAR LOS VALORES
mi_diccionario['nombre'] = 'Carlos'
print(mi_diccionario)

# 4. AÑADIR UN NUEVO CLAVE-VALOR
#Cuando quieren hacer de forma dinámica 
print('------AÑADIENDO ELEMENTOS AL DICCIONARIO------')
mi_diccionario['apellido'] = 'Lopez'
mi_diccionario['carrera'] = 'Ingenieria en Ciencias y Sistemas'
print(mi_diccionario)

#Aca no es estricto el dicionario como por ejemplo
#Python es muy accesible cuando se trata de agreagar valores a un diccionario
#Podemos meter variables y no hay problema, no generará erroress
clave = 'semestre'
valor = 4
mi_diccionario[clave] = valor
print(mi_diccionario)

clave = 'cursos'
valor = [
    {
       'curso': 'IPC1'
    },
    {
       'curso': 'IPC2'
    }
]
mi_diccionario[clave] = valor
print(mi_diccionario)

# 5. ELIMINAR UN CLAVE-VALOR
#La clave es como un id que nos ayuda a identificar el valor que deseamos ya sea eliminar, modificar o accedr.
# Practicamente es sobreescribir el diccionario.
print('------ELIMINANDO ELEMENTOS DEL DICCIONARIO------')
del mi_diccionario['cursos']
print(mi_diccionario)

# 6. ITERAR SOBRE UN DICCIONARIO
#Esto significa recorrerlo
print('------ITERANDO SOBRE UN DICCIONARIO------')
for clave in mi_diccionario:
    print(clave + ' : ' + str(mi_diccionario[clave]))

# 7. ITERAR SOBRE LOS VALORES
# Solo quieren imprimir los valroes
print('------ITERANDO SOBRE LOS VALORES DE UN DICCIONARIO------')
for valor in mi_diccionario.values():
    print(valor)

print('------ITERANDO SOBRE LAS CLAVES DE UN DICCIONARIO------')
for clave, valor in mi_diccionario.items():
    print(clave, str(valor))

# 8. COMPROBAR SI EXISTE UNA CLAVE
#Recorre todo el diccionario y busca esta coincidencia

print('------COMPROBAR SI EXISTE UNA CLAVE EN EL DICCIONARIO------')
if 'edad' in mi_diccionario:
    print("la clave cursos existe")
else:
    print("La clave cursos no existe")

# 9. GET
# ESTO ES PARA OBTENER EL VALOR DEL NOMBRE

print('------OBTENER UN VALOR DE UNA CLAVE------')
nombre = mi_diccionario.get('nombre')
print(nombre)
# Para excepcitones
# ESta es como un try catch
cursos = mi_diccionario.get('edad', 'No existe esta clave')
print(cursos)

# 10 OBTENER TODAS LAS CLAVES
#Retorna un objeto de tipo keys
print('------OBTENER TODAS LAS CLAVES DE UN DICCIONARIO------')
claves = mi_diccionario.keys()
print(claves)

# 11. Obtener todos los valroes
print('------OBTENER TODOS LOS VALORES------')
valores = mi_diccionario.values()
print(valores)

# 12. OBtener todos los items
# Se obtiene un arreglo de tuplas
print('------OBTENER TODOS LOS ITEMS------')
items = mi_diccionario.items()
print(items)

#Si queremos limpiar el dicconario
# 13. LIMPIAR EL DICCIONARIO
mi_diccionario.clear()
print(mi_diccionario)





