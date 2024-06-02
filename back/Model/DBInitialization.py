import mysql.connector

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="abm_masc"
)

# Se crea un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Creación de tablas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(25) NOT NULL,
        email VARCHAR(25) NOT NULL,
        password VARCHAR(20) NOT NULL,
        telefono VARCHAR(15) UNIQUE NOT NULL,
        token VARCHAR(30),
        bio TEXT,
        fotodeperfil VARCHAR(255),
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categorias (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS subcategorias (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        categoria_id INT,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        descripcion TEXT,
        precio DECIMAL(10, 2) NOT NULL,
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        subcategoria_id INT,
        FOREIGN KEY (subcategoria_id) REFERENCES subcategorias(id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS carritos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        usuario_id INT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS carrito_productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        carrito_id INT,
        producto_id INT,
        cantidad INT NOT NULL,
        FOREIGN KEY (carrito_id) REFERENCES carritos(id),
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS historial_carrito (
        id INT AUTO_INCREMENT PRIMARY KEY,
        carrito_id INT,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (carrito_id) REFERENCES carritos(id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS facturacion (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario_id INT,
        total DECIMAL(10, 2) NOT NULL,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario_id INT,
        metodo_pago VARCHAR(255) NOT NULL,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
''')

# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
conexion.close()