#con el profe aprenderemos a hacer un indicador de masa corporral

def calculoImc(altura, peso):
    imc = round(peso / pow(altura,2),2)
    estado = ""
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc < 25:
        estado = "Normal"
    elif imc < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obeso"
    estado += "(" + str(imc) + ")"
    return estado


print("Calculo IMC")
altura = float(input("INGRESE SU ALTURA: "))
peso = float(input("INGRESE SU PESO: "))

print(f"LOS RESULTADOS DEL IMC ES: {calculoImc(altura, peso)}")

