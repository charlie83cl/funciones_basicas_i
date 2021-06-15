#Contador flexible : establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. 
# Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum = int(input("INGRESZE UN PRIMER VALOR : "))
highNum = int(input("INGRESA UN SERUNDO VALOR: "))
mult = int(input("INGRESE EL MULTIPLO: "))

for i in range(lowNum, highNum + 1, 1):
    if (i % mult == 0):
        print(i)