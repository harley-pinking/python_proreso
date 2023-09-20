#   counter

# ejemplos
    # Ejemplo 1

string = 'La culpa es una prisión sin barrotes'
contador = string.count('a')
print(f'La letra a, se encontro {contador} de veces en la cadena: {string}')

    # ejemplo 2
var2 = 'El viento es el aliento de la tierra'
contador2 = var2.count('e', 6)
print(f'La letra e, se encontro {contador2} de veces en la cadena: {var2}')

    # ejemplo 3
var3 = 'El fuego es el cabello del sol en la tierra'
contador3 = var3.count('i', -32)
print(f'La letra i, se encontro {contador3} de veces en la cadena: {var3}')

    # ejemplo 4
var4 = 'La nieve son las plumas del invierno que caen del cielo'
contador4 = var4.count('o', 6, 40)
print(f'La letra o, se encontro {contador4} de veces en la cadena: {var4}')

