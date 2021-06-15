#1
def a():
    return 5
print(a())

# devuelve 5 en la pantalla

#2
def a():
    return 5
print(a()+a())

# devuelve 10 la suma de ambos llamados

#3
def a():
    return 5
    return 10
print(a())

# este devuelve solo 5 porque el 10 que esta en el segundo return no sale. porq se corta siempte en el primer return. HASTA AQUI LLEGAMOS

#4
def a():
    return 5
    print(10)
print(a())

# devuelve 5 porq lo de abajo del return no se contabiliza.

#5
def a():
    print(5)
x = a()
print(x)

#devuelve 5 y none porq llama al print(5) pero la funcion (a) no tiene return entonces x no tiene nada de valor.


#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))


#no funciona esta funcion porque le faltra un return(b+c) para que entregara algo en pantalla . pero la funcion
#solo imprime la suma

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#devuelve 25 pero no los suma sino que los concatena porque los convierte en un texto 'str'

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#devuvelve 100, 10 porque imprime el valor de 'b' y luego evalua si es menor o mayor y elige 10 porque no se cumple
#la condicion, luego no baja al siguiente return por regla. no lo hace. y ahi se frena el programa.

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# retorna 7, 14, 21 porque imprime la formula de la funciona a(b,) y evalua quien ees mayor o menor e imprime eventuialmente cada resultado


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# retorna solo 8 porque hace solo la funcion return b+c lo de abajo se omite por unreachable

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# imprime 500 despues imprime 300 luego imprime la funcion de a con 300 y luego imprime 500 del valor la variable libre b inicial

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# lo primero que imprime es el valor de b que es 500 y luego se imprime el valor de b que es 500 otra vez y se llama la funciona 
#la cual imprime el valro de b interna que es 300 y retorna el valor de b variable libre que es 500
# entonces imprime 500,500,300,500 explicalo Carlos (OJO NO TOMA EL VALOR DE return b)


#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#lo primero que hace es imprimir el valor de b libre que es 500, luego 
#pasa sobre la funcion b sin activarla y mas abajo imprime b libre que es 500 otra vez,
#luego b lla a funcion a(), esta le da un valor a b local de 300 y lo imprime, y lo retorna el valor  de 300 a b
#al finalizar la funcion la variable b se imprime con un valor de 300 porque el valor de retorno se almaceno en el valor de la variable b=a() == b = 300
#imprimiria el valor de b 500,500,300,300 

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# devuelve 1,3,2 porque lanza la funcion a que imprime 1 y luego llama a la funcion b que tiene imprime 3 y luego impime 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# esto es y llama la funcion a y esta funcion imprime 1, crea una variable x que llama 
# funcion b que imprime 3 y retorna 5 y finalmente imprime y que es el valor de retorno de la funciona a
#entones imprime 1, 3,5

