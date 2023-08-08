from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'tu_secret_key'  # Cambia esto por tu propia clave secreta


@app.route('/')
def index():
    conn = sqlite3.connect("Agenda.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    cursor.execute('SELECT * FROM contactos')
    contactos = cursor.fetchall()

    cursor.execute('SELECT * FROM incidentes')
    incidentes = cursor.fetchall()

    conn.close()

    return render_template('index.html', usuarios=usuarios, contactos=contactos, incidentes=incidentes)


# Ruta y vista para registro de usuario
@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        telefono = request.form['telefono']
        correo = request.form['correo']
        direccion = request.form['direccion']
        
        # Conectar a la base de datos y ejecutar un INSERT en la tabla de usuarios
        conn = sqlite3.connect("Agenda.db")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, apellido_paterno, apellido_materno, telefono, correo, direccion) VALUES (?, ?, ?, ?, ?, ?)',
                       (nombre, apellido_paterno, apellido_materno, telefono, correo, direccion))
        conn.commit()
        conn.close()
        flash('Usuario registrado exitosamente', 'success')
    return render_template('registro_usuario.html')

# Ruta y vista para registro de contacto
@app.route('/registro_contacto', methods=['GET', 'POST'])
def registro_contacto():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        
        usuario_id = None
        if 'usuario_id' in request.form:
            usuario_id = request.form['usuario_id']
        # Conectar a la base de datos y ejecutar un INSERT en la tabla de contactos
        conn = sqlite3.connect("Agenda.db")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contactos (usuario_id, nombre, telefono) VALUES (?, ?, ?)',
                       (usuario_id, nombre, telefono))
        conn.commit()
        conn.close()
        flash('Contacto registrado exitosamente', 'success')
    return render_template('registro_contacto.html')

# Ruta y vista para registro de incidente
@app.route('/registro_incidente', methods=['GET', 'POST'])
def registro_incidente():
    if request.method == 'POST':
        # Obtener datos del formulario
        usuario_id = request.form['usuario_id']
        fecha_hora = request.form['fecha_hora']
        tipo_incidente = request.form['tipo_incidente']
        direccion = request.form['direccion']
        
        # Conectar a la base de datos y ejecutar un INSERT en la tabla de incidentes
        conn = sqlite3.connect("Agenda.db")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO incidentes (usuario_id, fecha_hora, tipo_incidente, direccion) VALUES (?, ?, ?, ?)',
                       (usuario_id, fecha_hora, tipo_incidente, direccion))
        conn.commit()
        conn.close()
        flash('Incidente registrado exitosamente', 'success')
    return render_template('registro_incidente.html')
# ... (importaciones y configuraciones)

@app.route('/lista_usuarios')
def lista_usuarios():
    conn = sqlite3.connect("Agenda.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

def lista_contactos():
    conn = sqlite3.connect("Agenda.db")
    cursor = conn.cursor()
    
    cursor.execute('SELECT c.id, u.nombre || " " || u.apellido_paterno || " " || u.apellido_materno AS usuario, c.nombre, c.telefono FROM contactos c INNER JOIN usuarios u ON c.usuario_id = u.id')
    contactos = cursor.fetchall()
    
    conn.close()
    
    return contactos

def lista_incidentes():
    conn = sqlite3.connect("Agenda.db")
    cursor = conn.cursor()
    
    cursor.execute('SELECT i.id, u.nombre || " " || u.apellido_paterno || " " || u.apellido_materno AS usuario, i.fecha_hora, i.tipo_incidente, i.direccion FROM incidentes i INNER JOIN usuarios u ON i.usuario_id = u.id')
    incidentes = cursor.fetchall()
    
    conn.close()
    
    return incidentes

# Ruta y vista para eliminar usuario
@app.route('/eliminar_usuario/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    conn = sqlite3.connect("Agenda.db")
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()
    
    flash('Usuario eliminado exitosamente', 'success')
    
    return redirect(url_for('index'))  # Redirigir a la página principal

# Ruta y vista para eliminar contacto
@app.route('/eliminar_contacto/<int:id>', methods=['POST'])
def eliminar_contacto(id):
    conn = sqlite3.connect("Agenda.db")
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM contactos WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()
    
    flash('Contacto eliminado exitosamente', 'success')
    
    return redirect(url_for('index'))  # Redirigir a la página principal

# Ruta y vista para eliminar incidente
@app.route('/eliminar_incidente/<int:id>', methods=['POST'])
def eliminar_incidente(id):
    conn = sqlite3.connect("Agenda.db")
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM incidentes WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()
    
    flash('Incidente eliminado exitosamente', 'success')
    
    return redirect(url_for('index'))  # Redirigir a la página principal

# ... (código anterior)


# ... (resto de rutas y vistas)

if __name__ == '__main__':
    app.run(debug=True)
