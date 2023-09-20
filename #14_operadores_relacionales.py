# Operadores Relaciones
import msvcrt

import keyboard


print("""
╤║══════════════════════════════════║╤
╞║      Comparadpr de números       ║╡
╧║══════════════════════════════════║╧
      
      ¿quieres comparar 2 números?


                  (s/n)
""")

sn = msvcrt.getch().decode().strip()

if sn == 's':
    print("muy bien, vamos a empezar.")
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    print(f'los numeros a comparar son {num1} y {num2}\n')
    print('                 presiona [ENTER]..............')

    while not keyboard.is_pressed('enter'):

        pass
    if num1!=num2:
        print("\nes diferente...")
    if num1==num2:
        print('\nes excatamente igual...')
    if num1<num2 and num1<=num2:
        print('es menor...')
        print('es menor o igual...')
    if num1>num2 and num1>=num2:
        print('es mayor...')
        print('es mayor o igual...')
    else:
        print("\nel programa a terminado")

else:
    print("\nel programa a terminado\n")

print("\npresiona una tecla para salir")
msvcrt.getch()