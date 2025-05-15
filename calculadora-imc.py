# Calculadora de IMC 

def calcular_imc (peso,altura):
    imc = peso / (altura ** 2)
    return imc 


def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad" 
    # Solicitar datos personales
nombre = input("Ingresa tu nombre: ")
edad = int (input("Ingresa tu edad: "))
telefono = input("Ingresa tu número de teléfono: ")
correo = input("Ingresa tu correo electrónico: ")
# Solicitar datos físicos
peso = float(input("Ingresa tu peso en kilogramos: "))
estatura = float(input("Ingresa tu estatura en metros: "))
# Calcular IMC
imc = calcular_imc(peso, estatura)
clasificacion = clasificar_imc(imc)
# Mostrar resultados
print("\n----- Resultado -----")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Teléfono: {telefono}")
print(f"Correo: {correo}")
print(f"Tu IMC es: {imc:.2f} ({clasificacion})")
