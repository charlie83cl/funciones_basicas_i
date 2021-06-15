#IMPRIMIR UNA LINEA DE TEXTO STRING
print("CADENA DE TEXTO")

nombre="Carlos"
edad=37
calle="avenida gomez carreño"

print("hola, mi nombre es", nombre, edad, calle)
print("Nombre:",nombre,"Edad:",edad,"años", "Domicilio",calle)

print(f"Hola, este nuevo ejemplo es {nombre} y tengo {edad}")

print("Mi nombre es {} mi edad es {} años y vivo en {} asi que esos son mis datos".format(nombre,edad,calle))

a = 10
b = 15
print(f"{a} + {b} = {a+b}")

print("%d + %d = %d"% (a,b,(a+b)))
