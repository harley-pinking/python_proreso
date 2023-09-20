string = '0123456789'
substring = ''

print(f'Cadena principal: {string}')

substring = string[0]
print(f'Subcadena con indice, en la posicion 0 es: {substring}')

substring = string[5]
print(f'Subcadena con indice, en la posicion 5 es: {substring}')

substring = string[8]
print(f'Subcadena con indice, en la posicion 8 es: {substring}')

substring = string[-4]
print(f'Subcadena con indice, en la posicion -4 es: {substring}')

substring = string[0 : 3]
print(f'Subcadena con indices, en las posiciones del 0 al 3 es: {substring}')

substring = string[:3]
print(f'Subcadena con indices, en las posiciones del 0 al 3 es: {substring}')

substring = string[5:]
print(f'Subcadena con indice, en las posiciones del 5 al 10 es: {substring}')

substring = string[-4 : -1]
print(f'Subcadena con indice, en las posiciones del -4 al -1 es: {substring}')

substring = string[:]
print(f'Subcadena con indice, en las posiciones de principio a fin es: {substring}')

substring = string[1 : 6 : 2]
print(f'Subcadena con indice, en las posiciones y salto [1 : 6 : 2]: {substring}')

substring = string[ :  :3]
print(f'Subcadena con indice, en las posiciones y salto [ : : 3]: {substring}')