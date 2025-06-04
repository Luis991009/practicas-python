Vocales = ['a', 'e', 'i','o', 'u']
Vocales [1:4] = ('E', 'I', 'O') 
print (Vocales) 
print (Vocales, len(Vocales))

Vocales [1:4] = ()
print (Vocales, len(Vocales)) 

Vocales [1:2] = ('e', 'i', 'o', 'u')
print (Vocales, len (Vocales))

Vocales.extend (('i','i'))
print (Vocales, len (Vocales))
Vocales.index 
print (Vocales.index ('i'))
print(Vocales.count('i'))
print(Vocales.index('i', 6))
Vocales.reverse ()
print (Vocales, len(Vocales))
Vocales.sort ()
print (Vocales, len(Vocales))

carros = ['Audi', 'Ford', 'BMW', 'Mazda']
carros.sort(key=len)
print (carros)

listas= [(0, 1,), (2, 3, 4), (5, 6)]
print ( listas [0], listas   [1:3] )
print (listas [2] [1] )
x= [3, 2.5, 6, 6.3]

Vocales1 = ['a', 'e', 'i', 'o', 'u']
Vocales2 = Vocales1
print(Vocales1, Vocales2)

print(id(Vocales1), id(Vocales2))

Vocales3= Vocales1.copy
print(Vocales1, Vocales3)
print(id(Vocales1), id(Vocales3))

print(id(Vocales1 [2]), id(Vocales2 [2]))
del Vocales1 [2]
print (Vocales2, Vocales3)