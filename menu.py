menu = {
    "lunes": ("Sopa de verduras", "Pollo a la plancha", "Fruta"),
    "martes": ("Ensalada", "Pasta", "Pay"),
    "miércoles": ("Pechuga", "Pescado", "Yogurt"),
    "jueves": ("Jamon con huevo", "Lentejas", "Sopa azteca"),
    "viernes": ("Hamburguesa", "Pizza", "Helado")
}

dia = input("¿Qué día quieres consultar el menú? ").lower()

if dia in menu:
    entrada, principal, postre = menu[dia]
    print(f"\nMenú de {dia.capitalize()}:\nEntrada: {entrada}\nPlato principal: {principal}\nPostre: {postre}")
else:
    print("Día no válido o sin menú disponible.")
