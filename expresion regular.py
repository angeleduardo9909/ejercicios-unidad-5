import re
import os
def pedirNumeroEntero():
     
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    print()
    print("------------seleccione una opcion---------------")
    print ("1. Sentencia de asignación. Ejemplo: suma = 0, factorial = 1, vidas = cont, etc. ")
    print ("2. Operaciones aritméticas básicas. Ejemplo: etc")
    print ("3. Expresiones booleanas básicas. Ejemplo: edad >= 5, suma != 0, etc.)")
    print ("4. Formulas más complejas del tipo c = a op ( b op d)")
    print ("5. El encabezado de estructura de control. if, while, for, etc.")
    print ("6. salir")
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        
        print ("las sentencias de asignacion encontradas son: ")
        f = open("ejemplo.txt").read()
        ExpReg = r'([a-z0-9]+\s*[=]+\s*[a-z0-9+]+)'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp) 
        
    elif opcion == 2:
        
        print ("Operaciones aritmeticas basicas encontradas: ")
        f = open("ejemplo.txt").read()
        ExpReg = r'([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp) 
        
    elif opcion == 3:
        
        print("Las expreciones boleanas basicas encontradas son: ")
        f = open("ejemplo.txt").read()
        ExpReg = r'([A-Za-z0-9]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9])'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp) 
        
        
    elif opcion == 4:
        print("las formulas mas complejas del tipo C encontradas son : ")
        f = open("ejemplo.txt").read()
        ExpReg = r'([A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)])'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp) 
        
        
    elif opcion == 5:
        print("El encabezado de estructura de control. if, while, for, etc")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpRegIf = r'(if+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
        ExpRegWhile = r'(while+\s*[A-Za-z0-9-]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-]+\s*:)'
        ExpRegFor = r'(for+\s*[A-Za-z0-9-]+\s*[in]+\s*[A-Za-z0-9-]+\s*:)' 
        ExpRegTry=r'(try:+\s*[A-Za-z0-9-_]+\s*except+\s*[A-Za-z0-9-_]+\s*:)'
        expIf = re.findall(ExpRegIf, f, flags=re.MULTILINE)
        expWhile = re.findall(ExpRegWhile , f, flags=re.MULTILINE)
        expFor = re.findall(ExpRegFor, f, flags=re.MULTILINE)
        expTry = re.findall(ExpRegTry, f, flags=re.MULTILINE)
        print (expWhile)
        print ()
        print (expIf)
        print ()
        print (expTry)
        print ()
        print (expFor)
    elif opcion == 6:
            salir = True
    else:
        print ("Introduce un numero entre 1 y 5")