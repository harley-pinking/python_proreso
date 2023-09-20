# metodos islower() y lower(), isupper() y upper()



# metodo islower()

# Verifica si todas las letras de una cadena de caracteres, estan en minusculas
# Retorna un valor booleano: True-False


# Caso 1: metodo islower()
print('Caso 1: metodo islower()')
print()
test_islower1 = 'Hola, me lLAmO CeSAr'
print(f'contenido de la variable: {test_islower1}')
print(f'La variable cumple con el metodo islower()?: {test_islower1.islower()}')
print()

# Caso 2: metodo islower()
print('Caso 2: metodo islower()')
print()
test_islower2 = 'hola, me llamo cesar'
print(f'contenido de la variable: {test_islower2}')
print(f'La variable cumple con el metodo islower()?: {test_islower2.islower()}')
print()



# metodo lower()

# modifica la cadena de caracteres
# convierte las letras de la cadena de caracteres a letras minusculas


# Caso 1: metodo lower()
print('Caso 1: metodo lower()')
print()
test_lower1 = 'Hola, me lLAmO CeSAr'
print(f'contenido de la variable: {test_lower1}')
print(f'La variable cumple con el metodo lower()?: {test_lower1.islower()}')
print()

# se invoca el metodo lower()
print('\t > se invoca el metodo lower()\n')
test_lower1 = test_lower1.lower()

print(f'La variable cumple con el metodo lower()?: {test_lower1.islower()}')
print(f'contenido de la variable: {test_lower1}')

print()




# metodo isupper()

# verifica si todas las letras de una cadena de caracteres, se encuentran en mayusculas
# retorna un valor booleano: True-False

# Caso 1: metodo isupper()
print('Caso 1: metodo isupper()')
print()
test_isupper1 = 'los sueños son burbujas de jabón que flotan en el aire'
print(f'contenido de la variable: {test_isupper1}')
print(f'La variable cumple con el metodo isupper()?: {test_isupper1.isupper()}')
print()

# Caso 2: metodo isupper()
print('Caso 2: metodo isupper()')
print()
test_isupper2 = 'LOS SUEÑOS SON BURBUJAS DE JABÓN QUE FLOTAN EN EL AIRE'
print(f'contenido de la variable: {test_isupper2}')
print(f'La variable cumple con el metodo isupper()?: {test_isupper2.isupper()}')
print()


# metodo upper()

# modifica las cadenas de caracteres
# convierte las letras de la cadena de caracteres a letras mayusculas

# Caso 1: metodo upper()
print('Caso 1: metodo upper()')
print()
test_upper1 = 'las sombras susurran secretos olvidados en la oscuridad'
print(f'contenido de la variable: {test_upper1}')
print(f'La variable cumple con el metodo upper()?: {test_upper1.isupper()}')
print()

# se invoca el metodo upper()
print('\t > se invoca el metodo upper()\n')
test_upper1 = test_upper1.upper()

print(f'La variable cumple con el metodo upper()?: {test_upper1.isupper()}')
print(f'contenido de la variable: {test_upper1}')
