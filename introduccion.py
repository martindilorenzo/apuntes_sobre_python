#!/usr/bin/env python3


# Tuplas no pueden modificarse
mi_tupla = ('Hola', 356, 'que tal')
print('tupla:', mi_tupla, '\n')

# Listas si pueden modificarse
mi_lista = ["funciona o que", 3.5, 15, 'hola']
mi_lista[1] = 6.2
print("lista: ", mi_lista, "\n")

# Diccionarios si pueden modificarse
mi_dicc = {
    'nombre': "Martin",
    'apellido': "Dilorenzo",
    'edad': 28
}
print("dicc: ", mi_dicc, "\n")


# uso del for en un rango de numeros
def imprimir_informes(comienzo, final):
    print('Uso de for y un rango:')
    for year in range(comienzo, final):
        print('informe del', year)


# Recorrido de una tupla
def recorrer_tupla(tupla):
    print('Recorrido tupla:')
    for elemento in tupla:
        print(elemento)
    print()


# Recorrido de un diccionario
def recorrer_dicc(dicc):
    print('Recorrido diccionario:')
    for elemento in dicc:
        print(dicc[elemento])
    print()


# uso de parametros por omision, alicuota puede no estar
def calcular_neto(bruto, alicuota=21):
    iva = bruto * float(alicuota) / 100
    neto = bruto + iva
    return neto


# Uso de parametros arbitrarios, opcional pasa como tupla
def param_arbitrarios(obligatorio, *opcional):
    suma = 0
    for elemento in opcional:
        suma += elemento
    return suma + obligatorio


# Uso de parametros arbitrarios como pares de clave=valor
# opcional pasa como diccionario
def param_arb_clave_valor(obligatorio, **opcional):
    suma = 0
    for elemento in opcional:
        suma += opcional[elemento]
    return suma + obligatorio


# Desempaquetado de listas, ver llamado a funcion
def desempaquetado(a, b, c):
    return a + b + c


# Inyeccion de variables

cadena1 = "Cadena con modifcadores sin nombre, recibe: {} y {}."
resultado1 = cadena1.format(45, 'hola')

cadena2 = "Cadena con modifcadores con nombre, recibe: {dato1} y {dato2}."
resultado2 = cadena2.format(dato1=38, dato2='lalala')


"""
#Este codigo termina cuando se ingresa algo por teclado
while True:
	nombre = input("Ingrese su nombre: ")
	if nombre:
		break
"""

colores = ('negro', 'marron', 'celeste', 'verde', 'amarillo')

recorrer_tupla(colores)
recorrer_dicc(mi_dicc)
imprimir_informes(2020, 2023)
print()
print('Uso de parametros por omision:')
print('neto: ', calcular_neto(100))
print('neto: ', calcular_neto(100, 10.5), '\n')
print('Uso de parametros arbitrarios:')
print('suma: ', param_arbitrarios(10))
print('suma: ', param_arbitrarios(10, 3, 3, 3, 3), '\n')
print('Uso de parametros arbitrarios como clave=valor')
print('suma: ', param_arb_clave_valor(5))
print('suma: ', param_arb_clave_valor(5, a=1, b=2, c=3), '\n')
print('Desempaquetado de listas')
parametros = [1, 2, 3]
print('suma: ', desempaquetado(*parametros), '\n')
parametros = dict(a=4, b=5, c=6)
print('Desempaquetado de diccionario')
print('suma: ', desempaquetado(**parametros), '\n')
print(resultado1)
print(resultado2)
