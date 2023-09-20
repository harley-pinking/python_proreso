# Strings

    # Método 1
mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)

    # Método 2
Mensaje = "Hola "
Mensaje2 = "Soy "
Mensaje3 = "César"
print(Mensaje + Mensaje2 + Mensaje3)

    # Método 3
print("Concatenación:")

o1 = "Hola"
o2 =  "_"
o3 =  "César"
print(o1 + o2 + o3)
# ================================
num_uno2 = 16
num_dos2 = 16
resultado2 = num_uno2  + num_dos2
resultado2 = str(resultado2) # aqui se declara el valor de la variable como un valor de tipo "string".
print("El resultado de la suma es: " + resultado2)

print("Búsqueda:")

uno = "Me llamo Cesar"
buscar_find = uno.find("Cesar")
print(buscar_find)

print("Extracción:")
yoo = "llora el telefono"
extraer_cadena = yoo[0:4]
print(extraer_cadena)

print("Comparación")
mensaje_uno = 35
mensaje_dos = 35
print(mensaje_uno==mensaje_dos)


mensaje_uno4 = "hola"
mensaje_dos5 = "adis"
print(mensaje_uno4==mensaje_dos5)