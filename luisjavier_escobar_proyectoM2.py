# Ingresa una palabra 
palabra = input ("Ingresa una palabra: ")
# Calcular la longitud de la palabara
longitud = len (palabra)
if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:  # longitud > 8
    print(f"Sobran letras. Tiene {longitud} letras.")

#Cuadrante 
x = float (input ("Ingrese x: "))
y = float (input ("Ingresa la y: "))
#Verificar si hay alguna cordenada en 0
if x == 0 or y == 0:
    print ("Las coordenadas no pueden ser 0, el punto  no está en ningún cuadrante")
    # Determinamos el cuadrante según el signo de X e Y
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I")
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II")
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III")
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuadrante IV")
