from termcolor import colored

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
titulo = input("Ingresa el título: ")

# Mostrar la información recopilada
informacion = (f"Opción elegida: {opcion_elegida}\n"
               f"Número de UE: {numero_ue}\n"
               f"Coordenadas: {coordenadas}\n"
               f"Título: {titulo}\n"
               "Aquí puedes añadir más líneas de texto según sea necesario, "
               "usando la misma estructura para incluir variables si es preciso. "
               "Este método facilita la adición de texto extendido manteniendo "
               "el código organizado y legible.\n")

# Preguntar al usuario si desea eliminar el contenido anterior o añadir al archivo
accion = input("¿Deseas eliminar el contenido anterior del archivo? (sí/no): ").strip().lower()

if accion == 'sí' or accion == 'si':
    # Abrir el archivo informe.txt en modo 'w' para sobrescribir (o 'eliminar' su contenido)
    with open('informe.txt', 'w') as archivo:
        archivo.write(informacion)
else:
    # Abrir el archivo informe.txt en modo 'a' para añadir al final, incluyendo un salto de línea al inicio para separar entradas
    with open('informe.txt', 'a') as archivo:
        archivo.write('\n' + informacion)

print(colored(informacion, 'green'))
# Abrir el archivo informe.txt en modo 'a' para añadir al final
with open('informe.txt', 'a') as archivo:
    archivo.write(informacion)