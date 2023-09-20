# Practica con los mmétodos islower(), lower(), isupper(), upper()

palabra = input('ingrese una oracion o palabra:> ')

true_false = f'cumple el texto ingresado, con el metodo islower?:  {palabra.islower()}'
print(true_false)

while true_false.islower() == False:
    print('el texto que has ingresado, no cumple con el metodo islower()')
    print()
    print('haremos una conversion...')
    print()
    print(f'Palabra ingresada> {palabra}')
    print()
    print('\t >Invocamos el metodo lower()')
    print()
    palabra = palabra.lower()
    print(f'cumple el texto ingresado, con el metodo islower?:  {palabra.islower()}')
    if palabra.islower() == True:
            print('el texto ingresado, cumple con el metodo islower()')
            print('pasaremos al metodo isupper()')
            break

true_false = f'cumple el texto ingresado, con el metodo isupper?:  {palabra.isupper()}'
print(true_false)

while true_false.isupper() == False:
    print('el texto que has ingresado, no cumple con el metodo isupper()')
    print()
    print('haremos una conversion...')
    print()
    print(f'Palabra ingresada> {palabra}')
    print()
    print('\t >Invocamos el metodo upper()')
    print()
    palabra = palabra.upper()
    print(f'cumple el texto ingresado, con el metodo isupper?:  {palabra.isupper()}')
    if palabra.isupper() == True:
            print('el texto ingresado, cumple con el metodo isupper()')
            break

print(f'resultado final> {palabra}')
print('gracias por el apoyo  :)')


            