#EN ESTE EPISODIO ESTUDIAREMOS Y PRACTICAREMOS DEF FUNCIONES
#se escribe en minusculas al inicio de la sentencia def



#queremos sumar 2 numeros
# LE PEDIMOS AL USUARIO QUE INGRESE 

num1 = int(input("INGRESE EL VALOR 1: "))
num2 = int(input("INGRESE EL VALOR 2: "))

resultado = num1 + num2
print("EL RESULTADO ES ",resultado)


def sumar (a,b):
    r = a + b
    return r
#########################################################

num1 = int(input("INGRESE EL VALOR 1: "))
num2 = int(input("INGRESE EL VALOR 2: "))

print (sumar(num1 + num2))