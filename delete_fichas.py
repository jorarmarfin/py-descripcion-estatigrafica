import sqlite3

def eliminar_registro_por_id(id_ficha):
    conn = sqlite3.connect('fichas_arqueologicas.db')
    cursor = conn.cursor()

    # Elimina el registro con el ID especificado
    cursor.execute('DELETE FROM fichas WHERE id = ?', (id_ficha,))

    conn.commit()
    conn.close()
    print(f"Registro con ID {id_ficha} eliminado.")

def eliminar_todos_los_registros():
    conn = sqlite3.connect('fichas_arqueologicas.db')
    cursor = conn.cursor()

    # Elimina todos los registros de la tabla
    cursor.execute('DELETE FROM fichas')

    conn.commit()
    conn.close()
    print("Todos los registros han sido eliminados.")

# Ejemplo de uso
opcion = input("¿Deseas eliminar un registro específico (ingresa '1'), o todos los registros (ingresa '2')?: ")

if opcion == '1':
    id_ficha = input("Ingresa el ID del registro a eliminar: ")
    eliminar_registro_por_id(id_ficha)
elif opcion == '2':
    confirmacion = input("Estás seguro que deseas eliminar TODOS los registros? (sí/no): ").lower()
    if confirmacion == 'sí' or confirmacion == 'si':
        eliminar_todos_los_registros()
    else:
        print("Operación cancelada.")
else:
    print("Opción no válida.")
