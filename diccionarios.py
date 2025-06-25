d1 = {
    "Ilse": {
        "profesion": "Fisica",
        "ciudad": "Estado de México",
        "telefono": "55292089"
    },
    "Luis": {
        "profesion": "Ingeniero",
        "ciudad": "Ciudad de México",
        "telefono": "57684847"
    },
    "Julio": {
        "profesion": "Sistemas",
        "ciudad": "Nuevo León",
        "telefono": "658676485"
    },
    "Cesar": {
        "profesion": "Ing. en Mantenimiento",
        "ciudad": "Guadalajara",
        "telefono": "65757564"
    }
}
nombre = input("Ingrese su nombre: ")

if nombre in d1:
    print(f"\nInformación de {nombre}:")
    print(f"Profesión: {d1[nombre]['profesion']}")
    print(f"Ciudad: {d1[nombre]['ciudad']}")
    print(f"Teléfono: {d1[nombre]['telefono']}")
else:
    print(f"\nLo siento, {nombre} no se encontró.")


