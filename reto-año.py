from datetime import datetime

año_actual = datetime.now().year
print(f"Año actual: {año_actual}")

# Comparar con el año 2000
if año_actual == 2000:
    print("Estamos en el año 2000.")
elif año_actual > 2000:
    años_pasados = año_actual - 2000
    print(f"Han pasado {años_pasados} años desde el 2000.")
else:
    diferencia = 2000 - año_actual
    print(f"Faltan {diferencia} años para el año 2000.")

# Comparar con el año 2040
if año_actual == 2040:
    print("¡Ya estamos en el año 2040!")
elif año_actual < 2040:
    años_faltantes = 2040 - año_actual
    print(f"Faltan {años_faltantes} años para llegar al 2040.")
else:
    pasados = año_actual - 2040
    print(f"Ya han pasado {pasados} años desde el 2040.")
