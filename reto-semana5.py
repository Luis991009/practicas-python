entrada= input ("Hola introduce tu edad: ")
edad = 0 
if entrada.isnumeric() :
    edad = int (entrada)
else : 
    print ("Dato incorrecto. Debes ingresar un número")
    exit ()
    
if edad <= 0 :
    print("WOOOWWW!!" "Que joven eres, pero lo siento, eso no es posible")

elif edad > 115 :
    print ("Vaya, ¿Cómo le hiciste para vivir tanto?, eso no es posible")
elif edad < 18 :
    print("Eres menor de edad no puede comprar tu cigarrillo")
else : 
    print ("Eres mayor de edad toma tu cigarrillo")
