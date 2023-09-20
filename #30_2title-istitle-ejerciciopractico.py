# ejercicio practico: metodo title() & istitle()

first_name = input('Nombre: ')
last_name = input('Apellido: ')
full_name = f'{first_name} {last_name}'

print()
print(f'El metodo title se ha aplicado?: {full_name.istitle()}')
print(f'\nAplicando el metodo title: {full_name}\n'.title())
print(f'Volviendo a escribir el nombre: {full_name}')
print()

full_name  = full_name.title()
print(f'El metodo title se ha aplicado?: {full_name.istitle()}')
print(f'El Metodo title se ha aplicaod permanentemente: {full_name}')
print()

