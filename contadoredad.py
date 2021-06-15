#CONDICIONALES
#IF

#edad = int(input("Ingresa tu edad: "))

#if edad >= 18 :
 #   print("Eres mayor de edad...")



#print("Tu edad es: ",edad," años")



#tupla=('ardilla','arbol',8,True,'Bosque')
#print(type(tupla))
#lista=["'perro','gato',12,False],'Casa'"]
#print(type(lista))
#diccionario={dagregar contenido}

#SOLICITAR AL USUARIO UN NUMERO DEL 1 AL 17, LUEGO INDICAR EL DIA DE LA SEMANA AL CUAL CORRESPONDE
#ejemplo => 3 = miercoles

try:
    numero = int(input("ingrese un numero del 1 al 7 para decirte a que dia de la semana corresponde "))
    if numero == 1 :
        print("tu dia es Lunes")
    elif numero == 2:
        print("Tu dia es Martes")
    elif numero == 3:
        print("Tu dia es Miercoles")
    elif numero == 4:
        print("Tu dia es Jueves")
    elif numero == 5:
        print("Tu dia es Viernes")
    elif numero == 6:
        print("Tu dia es Sabado")
    elif numero == 7:
        print("Tu dia es Domingo")
    elif numero > 8:
        print("Ingresaste un numero mayor a 7")
except ValueError:
    print("Ingresaste un texto!!! debes ingresar numero digitos del 1 al 7")
