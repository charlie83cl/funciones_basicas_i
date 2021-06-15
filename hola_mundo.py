#CREANDO UN ARCHIVO PYTHON CON EL CLASICO HOLA MUNDO
#PASOS DE LA TAREA DEL MICHAEL CHOW

# 1. TAREA: imprimir "Hola mundo"
print( "Hola Mundo" )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Charlie"
print( "Hola", name,"!")	# con una coma
print( "Hola"+" "+ name +" "+"!")	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
name = 42
print( "Edad", name )	# con una coma
#print( "Edad"+ name)	# con un + - !Este debería darnos un error! #lo omiti para que no me diera error el comando completo
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "Completo"
fave_food2 = "Chorrillana"
restorant = "la Flor de Chile" # esta la agregue yo para probar adicion de variables nada mas 
print("Me encanta comer {} y {}".format(fave_food1, fave_food2)) # con .format()
print(f"Me encantan comer {fave_food1} y {fave_food2}-en verdad me encanta mas la {fave_food2} de {restorant}") # con una cadena f

