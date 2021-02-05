import usuarios.conexion as conexion
import datetime
import hashlib

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuarios:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        password = cifrado.hexdigest()
        fecha = datetime.datetime.now()

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, password, fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]

        except:
            result = [0, self]

        return result

    def identificar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        password = cifrado.hexdigest()

        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        usuario = (self.email, password)

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
