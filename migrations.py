import sqlite3

# Conectar a la base de datos SQLite, la crea si no existe
conn = sqlite3.connect('fichas_arqueologicas.db')

# Crear un cursor para ejecutar comandos SQL
c = conn.cursor()

# Crear la tabla 'fichas'
c.execute('''
CREATE TABLE IF NOT EXISTS fichas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_ficha TEXT NOT NULL,
    numero_ue TEXT,
    coordenadas TEXT,
    titulo_descripcion TEXT,
    tipo_estructura TEXT,
    descripcion TEXT,
    dimensiones TEXT,
    otros_comentarios TEXT,
    diagrama_estratificado TEXT,
    relaciones_fisicas TEXT,
    fiabilidad_estrategica TEXT,
    estado_conservacion TEXT,
    interpretacion_discusion TEXT,
    muestras TEXT,
    muro_asociado TEXT,
    planos TEXT,
    otros_dibujos TEXT,
    fotografias TEXT,
    ubicacion_diagrama TEXT,
    plataforma TEXT,
    periodo_fase TEXT,
)
''')

# Guardar (commit) los cambios y cerrar la conexión a la base de datos
conn.commit()
conn.close()

print("Tabla 'fichas_arqueologicas' creada exitosamente.")
