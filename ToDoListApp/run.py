from db.db_init import iniciar_db
from views.main import ventana
from views.tareas.home import mostrar_home_tareas

iniciar_db()
mostrar_home_tareas(ventana)
