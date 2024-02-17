from termcolor import colored
from insertar_fichas import insertar_ficha

# Lista de opciones para el usuario
opciones = [
    "Ficha de registro de estructuras diversas",
    "Ficha de registro de muros de piedra",
    "Ficha de registro de estructuras (muros de material vegetal)",
    "Ficha de registro de estructuras (muros de adobe)",
    "Ficha de registro de estructuras Diversas",
    "Ficha de registro de depósitos"
]

# Mostrar opciones al usuario
print("Por favor, elige una opción escribiendo el número correspondiente:\n")
for i, opcion in enumerate(opciones, 1):
    print(f"{i}. {opcion}")

# Pedir al usuario que elija una opción
eleccion = int(input("\nTu elección: ")) - 1
opcion_elegida = opciones[eleccion]

# Solicitar más información
numero_ue = input("Ingresa el número de UE: ")
coordenadas = input("Ingresa las coordenadas: ")
titulo_descripcion = input("Ingresa el título: ")
tipo_de_estructura = input("Ingresa tipo de estructura: ")
descripcion = input("Ingresa la descripcion: ")

insertar_ficha(
    opcion_elegida,
    numero_ue,
    coordenadas,
    titulo_descripcion,
    tipo_de_estructura,
    descripcion)
