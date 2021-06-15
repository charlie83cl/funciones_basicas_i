#activida bucle for del coding dojo!

#Básico : imprime todos los enteros del 0 al 150.
for i in range(0,151,1):
    print(i)
print("*****************************")

#Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for i in range(5,1005,5):
    print(i)
print("*****************************")

#Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, 
# imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".

for i in range(1,101):
    if i % 10 == 0:
        print(i,"Coding Dojo!")
    elif i % 5 == 0:
        print(i,"Coding!")
    else:
        print(i)
print("*****************************")

#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.


acumSumaImpares = 0
for i in range(500001):
    if i % 2 == 1:
        acumSumaImpares += i
else:
        print("termine de sumar numeros impares... ")
print(f"la Suma de los numero impares entre 0 y 500000 es: {acumSumaImpares}")

#Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.

for i in range(2018,0,-4):
    print(i)

#Contador flexible : establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. 
# Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum = int(input("INGRESZE UN PRIMER VALOR : "))
highNum = int(input("INGRESA UN SERUNDO VALOR: "))
mult = int(input("INGRESE EL MULTIPLO: "))

for i in range(lowNum, highNum + 1, 1):
    if (i % mult == 0):
        print(i)

        