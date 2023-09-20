#Condicionales anidadas
import msvcrt
from num2words import num2words

print ("""

╔══════════════════════════════════════════════════╗
║          Convertidor de números a letras         ║
╚══════════════════════════════════════════════════╝
""")


opciones =int(input("""

Seleccione una opción:
                    
Presione '1' para convertir un número a letra
Presione '2' para convertir una letra a número 

"""))

if opciones==1:
    demu = input("¡Muy Bien! escribe un número para convertirlo a letra: ")
    convertir = num2words(demu, lang= 'es')
    print(f"el número {demu} es: ", convertir)
elif opciones ==2:
    demu= input("¡Muy Bien! elige un número de entre uno y diez para convertirlo a número:  ")
    if demu.lower() =='uno':
        print("\nTu número es: '1'")
    elif demu.lower()=='dos':
        print("\nTu número es: '2'")
    elif demu.lower()=='tres':
        print("\nTu número es: '3'")
    elif demu.lower()=='cuatro':
        print("\nTu número es: '4'")
    elif demu.lower()=='cinco':
        print("\nTu número es: '5'")
    elif demu.lower()=='seis':
        print("\nTu número es: '6'")
    elif demu.lower()=='siete':
        print("\nTu número es: '7'")
    elif demu.lower()=='ocho':
        print("\nTu número es: '8'")
    elif demu.lower()=='nueve':
        print("\nTu número es: '9'")
    elif demu.lower()=='diez':
        print("\nTu número es: '10'")
    else:
        print(f"\nel numero '{demu}', está fuera de los parámetros\n")
else:
    print("tu opción no es valida")

print("\n-----el programa ha finalizado")
print("\n           presiona una tecla para salir..........")
msvcrt.getch()