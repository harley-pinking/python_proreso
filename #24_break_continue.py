# ejemplo para brake 
# la sentencia if se ejecuta 1 vez, y el bucle termina
print('while con la sentencia brake\n')
contador = int(input('INGRESE UN NUMERO:>   ')) 
jastar = (0)

while jastar <= contador :
    print(jastar, end=' ')
    jastar += 1
    if jastar == contador:
        break
print('\n el programa ha finalizado, la sentencia break se ha ejecutado..')
print('\n el valor actual de la variable es: ', jastar)


# ejemplo para  continue
# la sentencia if se ejecuta 2 veces
print('\nwhile con la sentencia continue')
contador = int(input('INGRESE UN NUMERO:>   ')) 
jastar = (0)

while jastar <= contador :
    print(jastar, end=' ')
    jastar += 1
    if jastar == contador:
        continue
print('\n el programa ha finalizado, la sentencia continue se ha ejecutado.')
print('\n el valor actual de la variable es: ', jastar)
