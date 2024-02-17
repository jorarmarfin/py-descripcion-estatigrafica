import sqlite3

def insertar_ficha(
        tipo_ficha,
        numero_ue,
        coordenadas,
        titulo_descripcion,
        tipo_estructura,
        descripcion):
    # Establece conexión con la base de datos SQLite
    conn = sqlite3.connect('fichas_arqueologicas.db')
    cursor = conn.cursor()

    # Ejecuta la instrucción SQL para insertar los datos en la tabla fichas
    cursor.execute('''
    INSERT INTO fichas (
    tipo_ficha,
    numero_ue, 
    coordenadas, 
    titulo_descripcion, 
    tipo_estructura,
    descripcion)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (tipo_ficha, numero_ue, coordenadas, titulo_descripcion, tipo_estructura, descripcion))

    # Confirma los cambios en la base de datos
    conn.commit()

    # Cierra la conexión con la base de datos
    conn.close()
