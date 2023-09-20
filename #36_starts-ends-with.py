# metodo startswith() y endswith()
# sirve para comprobrar si una cadena, inicia con una subcadena en particular:  muestra un valor booleano
# sirve para comprobrar si una cadena, termina con una subcadena en particular: muestra un valor booleano

resultado = 0
var13 = "La luna es el faro de la noche."
var16 = "Las olas son las caricias del mar"

start_with = 'metodo startwith():'
ends_with = 'metodo endswith():'

print(f'\n{start_with.rjust(30, "=")}\n')
print(f'\n{var13.center(100, "-")}\n')

resultado = var13.startswith('L')
print(f'{var13} empieza con la subcadena L: {resultado}')

resultado = var13.startswith('La')
print(f'{var13} empieza con la subcadena La: {resultado}')

resultado = var13.startswith('l')
print(f'{var13} empieza con la subcadena l: {resultado}')

resultado = var13.startswith('La caballa')
print(f'{var13} empieza con la subcadena La caballa: {resultado}')

resultado = var13.startswith('l', 4)
print(f'{var13} empieza con la subcadena l: {resultado}')




print(f'\n\n{ends_with.ljust(30, "=")}\n')
print(f'\n{var16.center(100, "-")}\n')


resultado = var16.endswith('r')
print(f'{var16} termina con la subcadena r.: {resultado}')
resultado = var16.endswith('mar')
print(f'{var16} termina con la subcadena mar: {resultado}')
resultado = var16.endswith('lol', 100, 100) # se ve asi xd
print(f'{var16} termina con la subcadena lol: {resultado}')
resultado = var16.endswith('R')
print(f'{var16} termina con la subcadena R: {resultado}')
resultado = var16.endswith('caricias', -17, -8)
print(f'{var16} termina con la subcadena caricias: {resultado}')
