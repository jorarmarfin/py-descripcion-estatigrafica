import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('fichas_arqueologicas.db')

# Crear un objeto cursor
cursor = conn.cursor()

# Consultar todo el contenido de la tabla 'fichas'
cursor.execute('SELECT * FROM fichas')

# Recuperar todos los resultados
fichas = cursor.fetchall()

# Verificar si la tabla tiene contenido
if fichas:
    print("Contenido de la tabla 'fichas':")
    for ficha in fichas:
        print(ficha)
else:
    print("La tabla 'fichas' está vacía.")

# Cerrar la conexión a la base de datos
conn.close()
