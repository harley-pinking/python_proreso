# Metodo title()
# corrige las palabras para que el inicio de estas esten con mayuscula y el resto este en minusculas


nombre = 'RoSa MeLaNO'
print(nombre)
print('metodo title()')

print(nombre.title())



# Metodo istitle()
# retorna un valor booleano
# True > si las palabras comienzan con mayuscula
# False > si no empiezan con mayuscula

print('\nmetodo istitle(): \n')

nombre = 'moNica galiNdO'
print(nombre.istitle())
print(nombre)



# ejemplo 1
print('ejemplo 1\n')

nombre = 'roSa MelaNO'
print(nombre.istitle())

nombre = nombre.title()
print(nombre)