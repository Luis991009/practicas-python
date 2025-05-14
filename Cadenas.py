# Texto_variado = 'Palabra 123 +-* $%&'
# print (type(Texto_variado))
# Podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
# print ("""
# funcionamiento de \
# programa: (opciones)
# -1 Para acceder a opciones
# -2 Para salir"""      ) 
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Suscripting e indexado 
# texto = 'Python' 
# # print (texto [0]) 
# # print (texto [5])
# # print (texto [-1])
# # Error no podemos acceder a una posición que no existe en las lineas 
# letra= texto[0]
# print (letra)
# # texto[0]='p' # error no podemos modificar una cadena
# letra = 'p'
# print (letra)

# texto_compuesto = letra + texto [1] #Concatenación
# print (texto_compuesto) 
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#Slicing o Subtrining 
# texto= 'Python'
# print (texto [0:3])
# print (texto [0:-3])
# print(texto [0:-2] )
# print (texto [2: ])
# print (texto [ :3 ])
# print (texto [-3 :: -1])
# print (texto[::-1])
# print (texto [1:50]) 
# print (texto [2:2])
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Cadenas y formatos

# texto = 'Hola mundo Buenastardes'
# print (texto.lower ())
# print (texto.upper())
# print (texto.capitalize())
# print (texto.title())
# print (texto.swapcase())
# texto=texto.upper()
# print (texto)
print ('{} + {}= {}'.format(2, 3, 2+3))
print ('{}+{}={}'.format('Hola', 'mundo', 'Hola mundo'))
print ('{:.3f}+{:.4f}={}'.format (2, 3, 2+3))
print ('{1}+{0}={2}'.format(2, 3, 2+3))
print ('{2}+{1}={2}'.format('Hola', 'mundo', 'Hola mundo'))
print ('{:d}= {:b}= {:o} = {:x}'.format (15, 15, 15, 15))