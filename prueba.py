import tkinter as tk
import sqlite3

# Función para actualizar el texto del label desde la base de datos
def update_label():
    # Conectar a la base de datos
    conn = sqlite3.connect('C:/Users/mateo/Documents/POO184/Examen3/Ferreteria.db')
    c = conn.cursor()

    # Ejecutar una consulta y obtener el resultado
    c.execute('SELECT Material FROM MatConstruccion WHERE IDMat = 1')
    result = c.fetchone()

    # Cerrar la conexión a la base de datos
    conn.close()

    # Actualizar el texto del label con el resultado de la consulta
    label.config(text=result[0])

# Crear la ventana principal
root = tk.Tk()

# Crear un label y colocarlo en la ventana
label = tk.Label(root, text="Texto inicial")
label.pack()

# Crear un botón y asignarle la función update_label
button = tk.Button(root, text="Actualizar", command=update_label)
button.pack()

# Iniciar el loop de la ventana
root.mainloop()