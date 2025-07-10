from db.db import conn

cursor = conn.cursor()

"""data = {
    "nombre_actividad" = "Projecto-UTMA",
    "descripcion" = "Projecto de la universidad",
    "fecha_actividad " = "dd/mm/yy"
}"""

# la dunción recibe un diccionario y devuelve una tupla
# La tupla tiene 2 parametros, el primero el estado y el segundo el mensaje
        
def crear_tarea(data):
    if not data["nombre_actividad"] or not data ["descripcion"] or not data ["fecha_actividad"]:
        return (False, "es necesario enviar todos los parametros")
    cursor.execute("INSERT INTO ToDoList(nombre_actividad, descripcion, fecha_actividad) VALUES (%s,%s,%s,%s)",(data["nombre_actividad"],data["descripcion"],data["fecha_actividad"]))
    conn.commit()
    return (True, "tarea almacenada con exito")

##
def actualizar_tarea(ToDoList_id, data_udate):
    if not ToDoList_id:
        return (False, "Es necesario enviar el ID de la Tarea")
    
    query = "UPDATE nombre_actividad SET=%s, descripcion=%s, fecha_actividad=%s, WHERE id=%s"
    variables = (
        data_udate["nombre_actividad"],
        data_udate["descripcion"],
        data_udate["fecha_actividad"],
        ToDoList_id
    )
    cursor.execute(query, variables)
    conn.commit()
    return (True, "ToDo_List actualizado con exito")

def eliminar_tarea(ToDo_List_id):
    query = "DELETE FROM ToDo_List WHERE id=%s"
    variable = (ToDo_List_id)
    cursor.execute(query, variable)
    conn.commit()
    return (True,"Tarea eliminada con exito")

 
def buscar_tarea(ToDo_List_id):
    query = "SELECT * FROM ToDo_List WHERE id=%"
    variable = (ToDo_List_id)
    ToDo_List = cursor.fetchone
    if not ToDo_List:
        return(False, "no se encontro la tarea con ese id")
    return(True, ToDo_List)

def buscar_tarea():
    query = "SELECT * FROM ToDo_List ORDER BY id"
    cursor.execute(query)
    ToDo_List = cursor.fetchall()
    return(True,ToDo_List)