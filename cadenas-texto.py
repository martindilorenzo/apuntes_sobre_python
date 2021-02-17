#!/usr/bin/env python3

# Manipulacion de cadenas de texto
print("Manipulacion de cadenas de texto \n")
cadena = "hola mundo"
resultado = cadena.capitalize()
print("capitalize: ", cadena, " >>> ", resultado, '\n')
cadena = "HoLa MuNdO"
print("lower: ", cadena, " >>> ", cadena.lower(), '\n')
print("upper: ", cadena, " >>> ", cadena.upper(), '\n')
print("swapcase: ", cadena, " >>> ", cadena.swapcase(), '\n')
print("title: ", cadena, " >>> ", cadena.title(), '\n')
cadena2 = "Bienvenido a mi aplicacion"
print("center: ")
print(cadena2)
print(cadena2.center(50, "-"), "\n")
print("ljust: ")
print(cadena2.ljust(50, "="), "\n")
print("rjust: ")
print(cadena2.rjust(50, "="), "\n")
cadena3 = "1867"
print("zfill: ")
print(cadena3, " >>> ", cadena3.zfill(10), "\n")
print("count 'a': ")
print(cadena2, ">>>", cadena2.count("a"), "\n")
print("find 'mi': ")
print(cadena2, ">>>", cadena2.find("mi"), "\n")
print("startswith 'Bien': ")
print(cadena2, ">>>", cadena2.startswith("Bien"), "\n")
print("endswith 'Bien': ")
print(cadena2, ">>>", cadena2.endswith("Bien"), "\n")
cadena5 = "alberto1867"
print("isalnum: ")
print(cadena2, ">>>", cadena2.isalnum())
print(cadena5, ">>>", cadena5.isalnum())
print(cadena3, ">>>", cadena3.isalnum(), "\n")
cadena4 = "HolaTodoJunto"
print("isalpha: ")
print(cadena4, ">>>", cadena4.isalpha())
print(cadena2, ">>>", cadena2.isalpha())
print(cadena3, ">>>", cadena3.isalpha(), "\n")
print("isdigit: ")
print(cadena5, ">>>", cadena5.isdigit())
print(cadena2, ">>>", cadena2.isdigit())
print(cadena3, ">>>", cadena3.isdigit(), "\n")
print("islower: ")
print(cadena5, ">>>", cadena5.islower())
print(cadena2, ">>>", cadena2.islower(), "\n")
cadena6 = "AH BUENO"
print("isupper: ")
print(cadena5, ">>>", cadena5.isupper())
print(cadena2, ">>>", cadena2.isupper())
print(cadena6, ">>>", cadena6.isupper(), "\n")
cadena7 = "     "
print("isspace: ")
print(cadena2, ">>>", cadena2.isspace())
print(cadena7, ">>>", cadena7.isspace(), "\n")
print("istitle: ")
print(cadena2, ">>>", cadena2.istitle())
print(cadena2.title(), ">>>", cadena2.title().istitle(), "\n")
print("format:")
cadena2 = "Bienvenido a mi aplicacion {0}"
print(cadena2, ">>>", cadena2.format("en Python"))
cadena8 = "Importe bruto: ${0} + IVA: ${1} = Importe neto: ${2}"
print(cadena8)
print(cadena8.format(100, 21, 121))
cadena8 = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: ${neto}"
print(cadena8)
print(cadena8.format(bruto=100, iva=21, neto=121))
print(cadena8.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21 / 100 + 100), "\n")
print("replace: ")
cadena2 = "Bienvenido a mi aplicacion"
buscada = "aplicacion"
reemplazo = "sitio web"
print(cadena2, ">>>", cadena2.replace(buscada, reemplazo), "\n")
print("strip, lstrip y rstrip: ")
cadena = "   www.hola.com    "
print(cadena)
print(cadena.strip())
print(cadena.lstrip())
print(cadena.rstrip(), "\n")
print("join: ")
rellenos = ("Nº 000-0", "-000 (ID: ", ")")
numero = "123"
numero_factura = numero.join(rellenos)
print(rellenos, "\n", numero_factura, "\n")
print("partition: ")
url = "https://www.google.com"
tupla = url.partition("www.")
print("url: ", url, "\ntupla: ", tupla)
protocolo, separador, dominio = tupla
print("Protocolo: {0}\nDominio: {1}".format(protocolo, dominio), "\n")
print("split:")
palabras = "manzana, pera, banana, frutilla"
print(palabras, "\n", palabras.split(", "), "\n")
print("splitlines:")
# Tambien funciona con \n
texto = """Linea 1
Linea 2
Linea 3
Linea 4
"""
print(texto, texto.splitlines())
