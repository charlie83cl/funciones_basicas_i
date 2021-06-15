
def sumar (a,b):
    r = a + b
    return r

def primos(a,b):
    primos =[]
    for num in range(a, (b + 1)):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)

    return primos

num1 = int(input("INGRESE EL VALOR 1: "))
num2 = int(input("INGRESE EL VALOR 2: "))

print(f"la suma de los 2 digitos ingresados es:{sumar(num1,num2)}")
print(f"los numeros primos contenidos entre los digitos ingresados es: {primos(num1,num2)}")
