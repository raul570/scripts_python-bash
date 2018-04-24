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

"""def suma("a,b"):
    suma= a+b
    print (suma)
def resta("a,b"):
    resta= a-b
    print= a-b
def division("a,b"):
    division= a+b
    print= a/b
