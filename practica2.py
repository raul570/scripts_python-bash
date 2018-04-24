import math
#primer ejercicio con float redondeo y truncamiento,utilizar libreria math
"""a="2"
b="3"
c= 1
d= 6.49
suma = int(a) + float(b) + c + round(d, 2) # , para mostrar decimales#
e = math.trunc(suma)
print (e)"""
#""" > comentar en bloque en vez de almoadilla en cada linea

#division, multiplicacion,potencia,resto y cociente
"""albert = 5
raul = 2
multiplicacion = albert * raul
print(multiplicacion)
division = float(albert) / float(raul)
print(division)
potencia = albert ** raul
print(potencia)
resto = albert % raul
print(resto)
cociente = albert // raul
print("el resultado es:"+ str(cociente))"""

#solicitar datos por el terminal de python
"""print("Escribe tu nombre")
name = raw_input ("introduce nombre")"""
#python2 > raw_input() python3 >input()

#condicionales if("condicion"):     elif():/else if     else:       and=&& or=||
"""
a = 3
b = 5
if ( a > b ):
    print (a,"es mayor",b)
elif (b > a ):
    print (a, "es mayor que" ,b)
else:
    print ("")
"""
#calculadora
"""
print ("Bienvenido a la calculadora del Puto amo")
a = float(raw_input ("introduce el primer numero: "))
b = float(raw_input ("introduce el segundo numero: "))
op = raw_input ("operaciones: 1=suma,2=resta,3=multiplicacion,4=division: ")
if (op =="1"):
    print (a + b)
elif (op == "2"):
    print(a - b)
elif (op == "3"):
    print (a * b)
elif (op == "4"):
    print (a / b)
else:
    print("Numero u operacion no valida")
"""
#contador
"""
count = 1
while (count <= 60):
    print ('llevas ' + str(count) + ' segundos sin trabajar')
    count = count + 1
print ("TRABAJA!")
"""

#calculadora con bucle
while
print ("Bienvenido a la calculadora del Puto amo")
a = float(raw_input ("introduce el primer numero: "))
b = float(raw_input ("introduce el segundo numero: "))
op = raw_input ("operaciones: 1=suma,2=resta,3=multiplicacion,4=division")
if (op =="1"):
    print (a + b)
elif (op == "2"):
    print(a - b)
elif (op == "3"):
    print (a * b)
elif (op == "4"):
    print (a / b)
else:
    print("Numero u operacion no valida")
