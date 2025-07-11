import tkinter as tk
from tkinter import messagebox as mb
from views.resources import PRIMARY_COLOR, SECONDARY_COLOR, THIRD_COLOR, TITLES, TEXTS
from db.operations import crear_tarea

def mostrar_crear_tarea(ventana:tk.Tk):
    # Borrar lo que habia antes 
    for widget in ventana.winfo_children():
        widget.destroy()
    # Inicio de Ventana para crear tareas 
    for i in range(9):
        ventana.rowconfigure(i, weight=1)
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1)
    ventana.columnconfigure(2, weight=1)

    tk.Label(ventana, text="Crear Tarea", bg=PRIMARY_COLOR, font=TITLES, fg=SECONDARY_COLOR).grid(row=0, column=0, pady=20, columnspan=3, sticky="n")

    tk.Label(ventana, text="Ingresa nombre de la actividad: ", bg=PRIMARY_COLOR, fg=THIRD_COLOR, font=TEXTS).grid(row=1, column=1)

    tk.Label(ventana, text="Ingresa Descripcion: ", bg=PRIMARY_COLOR, fg=THIRD_COLOR, font=TEXTS).grid(row=3, column=1)

    tk.Label(ventana, text="Ingresa la fecha: ", bg=PRIMARY_COLOR, fg=THIRD_COLOR, font=TEXTS).grid(row=5, column=1)

    # Creacion de Entradas para los datos de las tareas
    entry_name = tk.Entry(ventana, relief="flat", font=TEXTS,)
    entry_name.grid(column=1, row=2)

    entry_email = tk.Entry(ventana, relief="flat", font=TEXTS,)
    entry_email.grid(column=1, row=4)

    entry_password = tk.Entry(ventana, relief="flat", font=TEXTS,)
    entry_password.grid(column=1, row=6)

    # Guardar Tareas
    def enviar():
        data = {}
        data["nombre"] =entry_name.get()
        data["correo"] =entry_email.get()
        data["password"] =entry_password.get()
        data["estado"] = "activo"

        status, msg = crear_tarea(data)
        if not status:
            mb.showerror("ocurrio un error", msg)
            return
        mb.showinfo("Exito!", msg)

    tk.Button(ventana, text="Guardar", command=enviar, relief="flat", font=TEXTS, fg=THIRD_COLOR, bg=SECONDARY_COLOR).grid(column=1, row=7)
    ventana.mainloop()
    