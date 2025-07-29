# Este es un comentario simple

'''
este 
es
un 
comentario
multilínea
salu2
ipc2
'''

"""
Este es otro comentario 
multilinea
saludos
"""

# Declaración de variables

hola = "Hola"
x = 10
y = 32
z = 45
a = True
b = False
c  = 9.99
d = []
e = {}
f = None

# Asignación de variables

ipc2 = "IPC2"
ipc2 = "Introducción a la Programación y computación 2"

variable = 1
variable = "1"
variable = True
variable = 4.5
variable = [1,2,3,4]

#Casteo

var1 = "1"
var2 = int(var1)
var3 = 4
var4 = str(var3)
var5 = "2.45"
var6 = float(var5)

# Expresiones aritméticas

# Suma

suma = 3+3 

#Error
#concat = 3 + "hola"

# Correcto
concat = str(3) + "hola"

# Resta
resta = 2-6

# Multiplicación
multiplicacion = 2*3

#División
division = 3/2

#Modulo
modulo = 4%2 #residuo 0

#Expresiones de incremento y decremento
#x++
x += 1 # x + 1
#x--
x +-1 # x - 1

# Expresiones relacionales
x < y
x > y
x <= y
x >= y
x == y
x != y

# Operaciones lógicas
a and b # &&
c or d #||
not e # !

x > 3 and x < 5

# Outputs

#sin salto de linea
print("Hola mundo! :D", end="")
#Con salto de linea
print("hola de nuevo")

# Inputs
#Caso tipado
#entrada  = int(input("ingresa algo: "))

# Caso no tipado
#entrada = input("Ingresa tu nombre: ")
#print("Hola, mi nombre es " + entrada)

#input("entrada porque si")

#Sentencia IF
condicional = 6
if condicional > 5:
    print("Es mayor que 5")
elif condicional == 5:
    print("Es igual a 5")
else:
    print("Es menor que 5")

# Match-case
dia = 8

match dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case _: # Es como un else
        print("no coincide con ninguno")


# Sentencia while
contador = 1
while contador <= 10:
    print(contador)
    contador +=1

#Ciclo for (mero especial)

#queremos hacer el mismo contador de 1 a 10, quiere decir hasta este número no lo imprimas eso quiere decir el fin

print("Ciclo for")
#contador de números
#Range es i = 1 hasta que i < 10
for i in range(1,10):
    print(i)

#Contador 2
#Range j = 0 hasta que j < 10, podemos decir imprimir los números digitos les serviría esto
for j in range(10):
    print(j)

#Iterar una lista: Así se recorre una lista
lista = [1,2,3]
for numero in lista:
    print(numero)

print("for lista")
#Acá hace lo mismo que el anterior se recorre el tamaño de toda la lista.
for z in range(len(lista)):
    print(lista[z])

# Funciones

# en java teniamos que escribir public static void. Puede venir parametros o no, o puede retornar algo o no

#Sin parametros y sin retornar
def funcion1():
    print("Hola ipc2!")

funcion1()

#Con parametros y sin retornar nada
def funcion2(num1, num2):
    total = num1 + num2
    print("La suma de num1 y num2 es: " + str(total))

funcion2(1,8)


#Sin parámetros y retorna 1
def funcion3():
    return "Adios!"

print(funcion3())

#Con parámetros y con retorno
def funcion4(num1, num2):
    return num1 - num2

print(funcion4(5,3))

# Función tipada
#esto por casos estrictos por que se obliga a colocar un entero
def funcion5(num1:int, num2:int) -> int:
    return num1 * num2

print(funcion5(6,2))