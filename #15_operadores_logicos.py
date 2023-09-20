import msvcrt


print("operadores logicos:")

print('conjuncion con el O.L (and):')

num1 = int(input('ingrese un numero "mayor a 2" y "menor que 7":>  '))

if num1>=2 and num1<= 7:
    print(f'{num1} es mayor o igual a 2')
    print(f'{num1} es menor o igual a 7')
    print('la condicion se cumple')

else:
    print('ninguna condicion se cumple.')

print('negacion con el O.L (not):')

num2 = int(input('Ingrese un valor "mayor" o "menor" a "5" para la variable "num2":>  '))
print('\n\nSi el valor asignado en la variable "num2" es menor a "5", se niega la condicion')
print('Si el valor asignado en la variable "num2" es mayor a "5", se cumple la condicon.')

if not num2 <= 5:
    print('La condicion no se cumple, se ejecute la instrucci[on]')
else:
    print('La condici[on se ha cumplido, se cancela la condici[on]]')


print('disyuncion con el O.L (or):')

palabra = input('Ingrese "si" o "yes" pra cumplir la condicion:> ')

if palabra.lower() =='si' or 'yes':
    print('la condicion ha sido complida con eficiencia 50%')

else:
    print('la condici[on no ha podido ser cumplida..]')

print('Gracias por pasarte a movistar')
print("\n\npresiona una tecla para salir...........")
msvcrt.getch()