import psycopg2 as psq

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "ToDoList",
    "user": "postgres",
    "password": "42001217",
    "host": "localhost",
    "port": "5432"
}

conn = psq.connect(
    dbname = DB_CONFIG['dbname'],
    user = DB_CONFIG['user'],
    password = DB_CONFIG['password'],
    host = DB_CONFIG['host'],
    port = DB_CONFIG['port']
)