from db.db import conn

#Para que no esten vacios se utiliza el NOT NULL
#Varchar es para guardar taxto
sql_schema = """
CREATE TABLE iF NOT EXISTS ToDo_List(
   id SERIAL PRIMARY KEY,
   nombre_actividad VARCHAR(100) NOT NULL,    
   descripcion VARCHAR(50) NOT NULL,
   fecha_actividad VARCHAR(100) NOT NULL
   );
"""

def iniciar_db():
    try:
        cursor = conn.cursor()
        cursor.execute(sql_schema)
        conn.commit()
        print("tabla crada con exito :P")
    except Exception as e:
        print("Error ocurrido: ", e)

iniciar_db()