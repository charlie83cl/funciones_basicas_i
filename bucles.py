#EN ESTE EPISODIO USAERMOS BUCLES
# UN BUCLE ES UN ESTRUCTURA DE CODIGO QUE ME PERMITE REPETIR
# UN BLOQUE DE CODIGO EN LA N CANTIDA DE VECES RECORRER UNA LISTA

#while
respuesta = 's'
contador = 0

while contador <= 2:
    try:
        edad = int(input(f"Ingrese su Edad en Numeros. Intento Nro.{contador}: "))
        if edad >= 18:
            print("eres Mayor de Edad")
        else:
            print("ere Menor de Edad")
        contador += 1
    except ValueError:
            print("Algo Malo Hiciste Mortal")

    respuesta = input("Desea ingresar una nueva edad  [s|n]: ")
